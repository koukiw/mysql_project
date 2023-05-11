import mysql.connector
import glob
import datetime
import pytz
import pandas as pd
import os

#upload_dataは実行時の日時
dt_now = datetime.datetime.now(pytz.timezone('Asia/Tokyo')).strftime('%Y%m%d%H%M%S')

# データベースに保存するpandasを作成
output_df  = pd.DataFrame(columns=["project_name","path","file_name","file_format","create_date","upload_date","json_data"])

def create_date_catalog(project_name):
    try:
        if project_name =="":
            files = glob.glob(os.path.join("./file_dir","*.*"),recursive=True)
            project_name= "single_file"
        else:
            files = glob.glob(os.path.join("./file_dir", project_name,"**","*.*"),recursive=True)
        print(project_name)
        cnt = 0
        data = []
        for file in files:
            cnt += 1
            print("ファイル情報抽出中…（{}/{}）".format(cnt, len(files)))
            file_name  = os.path.basename(file)
            file_path  =file[11:]
            file_format = os.path.splitext(file)[1] [1:]
            data.append([project_name,file_path,file_name,file_format,dt_now,dt_now,'{"test":"hoge"}'])
            
        df_tmp =pd.DataFrame(data = data,
                            columns=["project_name","path","file_name","file_format","create_date","upload_date","json_data"])
        return df_tmp
            
    except Exception as e:
        print("create_date_catalogにてerror発生")
        return -1
    

dir_list = glob.glob('./file_dir/**/') #ディレクトリを探す
for dir in dir_list:
    project_name = dir[11:-1]  #文字列から./file_dirの部分を削除
    df_tmp = create_date_catalog(project_name)
    output_df = pd.concat([output_df,df_tmp],ignore_index=True)

single_file_list = glob.glob('./file_dir/*.*') #シングルファイルを探す
if len(single_file_list)!=0:
    for single_file in single_file_list:
        df_tmp = create_date_catalog("")
        output_df = pd.concat([output_df,df_tmp],ignore_index=True)
        
print(output_df)

# データベースに接続
connection = mysql.connector.connect(user='kouki',  # ユーザー名
                                    password='password',  # パスワード
                                    # host = "host.docker.internal"#hostは下記とどっちでも良い
                                    host = "db",
                                    database = "demo_db",
                                )


# demo_tableにデータカタログ保存
with connection:
    with connection.cursor(buffered=True) as cursor:
        for index,row in output_df.iterrows():
            # レコードを挿入
            sql = "INSERT INTO demo_table(project_name,path,file_name,file_format,create_date,upload_date,json_data) VALUES (%s,%s,%s,%s,%s,%s,%s)"
            cursor.execute(sql, (row["project_name"],row["path"],row["file_name"],row["file_format"],row["create_date"],row["upload_date"],row["json_data"]))

            # sql = "INSERT INTO text_table(project_name,text_data) VALUES (%s,%s)"
            # cursor.execute(sql, (row["project_name"],row["text"]))

    # コミットしてトランザクション実行
    connection.commit()
    print("demo_tableにデータ保存")