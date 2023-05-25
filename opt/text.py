import mysql.connector
from get_text import extract_text_from_file
import glob
import datetime
import pytz
import pandas as pd
import os

#upload_dataは実行時の日時
dt_now = datetime.datetime.now(pytz.timezone('Asia/Tokyo')).strftime('%Y%m%d%H%M%S')

# データベースに保存するpandasを作成
output_df  = pd.DataFrame(columns=["project_name","path","file_name","text"])
    

dir_list = glob.glob('./file_dir/**/') #ディレクトリを探す
for dir in dir_list:
    project_name = dir[11:-1]  #文字列から./file_dirの部分を削除
    print(project_name)
    files = glob.glob(os.path.join("./file_dir", project_name,"**","*.*"),recursive=True)

    for filepath in files:
        print(filepath)
        text = extract_text_from_file(filepath)
        file_name  = os.path.basename(filepath)
        data = [[project_name,filepath,file_name,text[:15000]]]
        df_tmp = pd.DataFrame(data = data,
                            columns=["project_name","path","file_name","text"])
        output_df = pd.concat([output_df,df_tmp],ignore_index=True)


single_file_list = glob.glob('./file_dir/*.*') #シングルファイルを探す
if len(single_file_list)!=0:
    for filepath in single_file_list:
        print(filepath)
        text = extract_text_from_file(filepath)
        file_name  = os.path.basename(filepath)
        data = [["single_file",filepath,file_name,text[:15000]]]
        df_tmp = pd.DataFrame(data = data,
                            columns=["project_name","path","file_name","text"])
        output_df = pd.concat([output_df,df_tmp],ignore_index=True)

print(output_df)


# データベースに接続
connection = mysql.connector.connect(user='kouki',  # ユーザー名
                                    password='password',  # パスワード
                                    # host = "host.docker.internal"#hostは下記とどっちでも良い
                                    host = "db",
                                    database = "demo_db",
                                )

# text_tableにテキストデータを保存
with connection:
    with connection.cursor(buffered=True) as cursor:
        for index,row in output_df.iterrows():
            # レコードを挿入
            sql = "INSERT INTO text_table(project_name,path,file_name,text) VALUES (%s,%s,%s,%s)"
            cursor.execute(sql, (row["project_name"],row["path"],row["file_name"],row["text"]))

    # コミットしてトランザクション実行
    connection.commit()
    print("text_tableにデータ保存")