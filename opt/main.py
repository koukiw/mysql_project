from pymongo import MongoClient
from pdf_func import func_pdf2text
from word_func import word2text
from csv_func import csv2text
import pdfminer
import glob
import datetime
import pytz

#upload_dataは実行時の日時
dt_now = datetime.datetime.now(pytz.timezone('Asia/Tokyo')).strftime('%Y%m%d%H%M%S')

HOST = 'localhost'
PORT = 27017
USERNAME = 'root'
PASSWORD = 'password'
MONGODB_URL= "mongodb://127.0.0.1:27017"
DB_NAME = 'demo_db'
COLLECTION_NAME = 'demo_collection'


if __name__ == '__main__':
    # ローカルのmongodb用リンク
    # client = MongoClient(host=HOST, port=PORT, username=USERNAME, password=PASSWORD)
    #　ローカルの場合は以下で接続できる
    # client = MongoClient(username=USERNAME, password=PASSWORD)

    # dockerコンテナ用リンク
    #以下2行どちらでも接続可能
    # client = MongoClient('mongodb://root:password@host.docker.internal:27017/')
    client = MongoClient('mongodb://root:password@mongo:27017/')
    
    dir_list = glob.glob('./file_dir/**/')
    db = client[DB_NAME]
    for dir in dir_list:
        collection_name = dir[11:-1]
        print("ディレクトリ選択")
        print(collection_name)
        collection = db[COLLECTION_NAME]
        results = func_pdf2text(collection_name,dt_now)
        results.extend(word2text(collection_name,dt_now))
        csv,excel = csv2text(collection_name,dt_now)
        results.extend(csv)
        results.extend(excel)
        collection.insert_many(results)
        print(collection_name[11:-1] + "完了")
    
    single_file_list = glob.glob('./file_dir/*.*')
    if len(single_file_list)!=0:
        collection = db[COLLECTION_NAME]
        for single_file in single_file_list:
            idx = single_file.rfind(".")
            file_format = single_file[idx+1:]
            if file_format =="pdf":
                results = func_pdf2text("",dt_now)
                collection.insert_many(results)
            elif file_format =="docx":
                results = word2text("",dt_now)
                collection.insert_one(results)
            elif file_format =="csv":
                results = csv2text("",dt_now)
                collection.insert_one(results)

