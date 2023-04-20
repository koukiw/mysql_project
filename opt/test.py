from docx import Document
import os
import re
import sys
import csv
import json
import glob
import shutil
import warnings

#これからやりたいこと
# 添付画像がある場合はそれも格納、ある場合のみjsonのkeyを増やす
# files = glob.glob(os.path.join('./file_dir/**', "*.docx"),recursive=True)
# files = glob.glob(os.path.join("./file_dir/project1/**", "*.pdf"),recursive=True)
# print(files)
# print(os.path.join("./file_dir/project1/**", "*.pdf"))

# collections_name = glob.glob('./file_dir/**/')
# for collection_name in collections_name:
#     print(collection_name)

collections_list = glob.glob('./file_dir/**/')
for collection_name in collections_list:
    print(collection_name[11:-1])
    pro_path = os.path.join("./file_dir", collection_name[11:-1],"**","*.pdf")
    print(pro_path)
    files = glob.glob(pro_path,recursive=True)
    print(files)
# db_name = glob.glob('./file_dir/**/')
# # print(glob.glob('temp/**/', recursive=True))
# print(pro_path)