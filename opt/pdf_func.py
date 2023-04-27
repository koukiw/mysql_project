import os
import re
import sys
import csv
import json
import glob
import shutil
import warnings
import pdfminer
import pandas as pd

from pdfminer.high_level import extract_text

CONFIG_KEY_PDF_FOLDER = "../pdf"


# PDFからテキストを抜き出してjson形式で情報を整理（keyはtitle、text,file_format）
def func_pdf2text(project_name,dt_now,output_df):
    try:
        #
        # PDF→テキスト情報抽出処理
        #
        if project_name =="":
            files = glob.glob(os.path.join("./file_dir","*.pdf"),recursive=True)
        else:
            files = glob.glob(os.path.join("./file_dir", project_name,"**","*.pdf"),recursive=True)
        cnt = 0
        print("pdffiles",files)
        results = []
        for file in files:
            cnt += 1
            print("pdfテキスト抽出処理中…（{}/{}）".format(cnt, len(files)))
            # PDFのテキスト取り出し
            # print(file)

            # テキストの抜き出し
            text = extract_text(file)
            # テキストの加工
            text = text.replace("\n","").replace("\r","").replace("\t","").strip()

            filename  = os.path.basename(file)

            # result = {"ファイル名":filename,"text": text,"ファイル拡張子":"pdf","パス":file[11:]}
            file_path  =file[11:]

            df_tmp  =pd.Series([10,file_path,filename,"pdf","text",dt_now,dt_now,'{"test":"hoge"}'],
                               index=["project_id","path","file_name","file_format","text","create_date","upload_date","json_data"])
            output_df = output_df.append(df_tmp,ignore_index=True)
            # result = {"プロジェクト名":project_name,"パス":file[11:],"ファイル名":filename,"ファイル拡張子":"pdf","text": "text","create_data":dt_now,"upload_data":dt_now}
            # results.append(result)

        return output_df
            
    except Exception as e:
        print("pdf2textにてerror発生")
        return -1


# メイン処理
if __name__ == "__main__":
    # print("pdfminer.six ver.{}".format(pdfminer.__version__))
    results = func_pdf2text()
    print(results)



