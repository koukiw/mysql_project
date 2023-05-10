#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import mysql.connector
from pdf_func import func_pdf2text
from word_func import word2text
from csv_func import csv2text
import glob
import datetime
import pytz
import pandas as pd

#upload_dataは実行時の日時
dt_now = datetime.datetime.now(pytz.timezone('Asia/Tokyo')).strftime('%Y%m%d%H%M%S')

# データベースに保存するpandasを作成
output_df  = pd.DataFrame(columns=["project_name","path","file_name","file_format","text","create_date","upload_date","json_data"])
print(output_df)

dir_list = glob.glob('./file_dir/**/')
for dir in dir_list:
    project_name = dir[11:-1]  #文字列から./file_dirの部分を削除
    print("ディレクトリ選択")
    print(project_name)
    output_df = func_pdf2text(project_name,dt_now,output_df)
    # results.extend(word2text(project_name,dt_now))
    # csv,excel = csv2text(project_name,dt_now)
    # results.extend(csv)
    # results.extend(excel)


    # print(project_name[11:-1] + "完了")
    # print(output_df)
    # print(type(output_df))

single_file_list = glob.glob('./file_dir/*.*')
if len(single_file_list)!=0:
    for single_file in single_file_list:
        idx = single_file.rfind(".")
        file_format = single_file[idx+1:]
        if file_format =="pdf":
            output_df = func_pdf2text("",dt_now,output_df)
        # elif file_format =="docx":
        #     results = word2text("",dt_now)
        #     print(results)
        # elif file_format =="csv":
        #     results = csv2text("",dt_now)
        #     print(results)
print("output_df")
print(output_df)
# output_df.to_csv("./output.csv",index=False)
# df = pd.read_csv("./output.csv")
# データベースに接続
connection = mysql.connector.connect(user='kouki',  # ユーザー名
                                    password='password',  # パスワード
                                    # host = "host.docker.internal"#hostは下記とどっちでも良い
                                    host = "db",
                                    database = "demo_db",
                                    charset = "utf8mb4", # 設定を追加
                                )



# project_nameの親テーブルを先に保存
# s = 0
with connection:
    with connection.cursor() as cursor:
        for index,row in output_df.iterrows():
            # レコードを挿入
            sql = "INSERT INTO demo_table(project_name,path,file_name,file_format,text,create_date,upload_date,json_data) VALUES (%s,%s,%s, %s,%s,%s,%s,%s)"
            cursor.execute(sql, (row["project_name"],row["path"],row["file_name"],row["file_format"],"test",row["create_date"],row["upload_date"],row["json_data"]))

            sql = "INSERT INTO text_table(project_name,text_data) VALUES (%s,%s)"
            cursor.execute(sql, (row["project_name"],row["text"]))

    # コミットしてトランザクション実行
    connection.commit()
    print("demo_table,text_tableにデータ保存")