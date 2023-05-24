import mysql.connector
from get_text import pdf2text,word2text,csv2text,excel2text,pptx2text
import glob
import datetime
import pytz
import pandas as pd
import os

#upload_dataは実行時の日時
dt_now = datetime.datetime.now(pytz.timezone('Asia/Tokyo')).strftime('%Y%m%d%H%M%S')

# データベースに保存するpandasを作成
output_df  = pd.DataFrame(columns=["project_name","path","file_name","text"])

def get_text(project_name):
    try:
        if project_name =="":
            files = glob.glob(os.path.join("./test_file_dir","*.*"),recursive=True)
            # files = glob.glob(os.path.join("./file_dir","*.*"),recursive=True)
            project_name= "single_file"
        else:
            files = glob.glob(os.path.join("./test_file_dir", project_name,"**","*.*"),recursive=True)
            # files = glob.glob(os.path.join("./file_dir", project_name,"**","*.*"),recursive=True)
        print(project_name)
        cnt = 0
        data = []
        print(files)
        for file in files:
            cnt += 1
            print("テキスト抽出中…（{}/{}）".format(cnt, len(files)))
            print(file)
            file_name  = os.path.basename(file)
            file_path  =file[11:]
            file_format = os.path.splitext(file)[1] [1:]
            if file_format =="pdf":
                text = pdf2text(file)
            elif file_format =="csv":
                text = csv2text(file)
            elif file_format =="xlsx":
                text = excel2text(file)
            elif file_format =="docx" or file_format =="doc":
                text = word2text(file)
            elif file_format =="pptx":
                text = pptx2text(file)
            data.append([project_name,file_path,file_name,text[:15000]]) 
        df_tmp =pd.DataFrame(data = data,
                            columns=["project_name","path","file_name","text"])
        return df_tmp
    
    except Exception as e:
        print("get_textにてerror発生")
        return -1
    

dir_list = glob.glob('./file_dir/**/') #ディレクトリを探す
for dir in dir_list:
    project_name = dir[11:-1]  #文字列から./file_dirの部分を削除
    df_tmp = get_text(project_name)
    output_df = pd.concat([output_df,df_tmp],ignore_index=True)

single_file_list = glob.glob('./file_dir/*.*') #シングルファイルを探す
if len(single_file_list)!=0:
    for single_file in single_file_list:
        df_tmp = get_text("")
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