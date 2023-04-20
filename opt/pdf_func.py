import os
import re
import sys
import csv
import json
import glob
import shutil
import warnings
import pdfminer

from pdfminer.high_level import extract_text

CONFIG_KEY_PDF_FOLDER = "../pdf"


# PDFからテキストを抜き出してjson形式で情報を整理（keyはtitle、text,file_format）
def func_pdf2text(collection_name,dt_now):
    process_name = ""
    try:
        #
        # PDF→テキスト情報抽出処理
        #
        process_name = "PDFからのテキスト情報抽出"
        if collection_name =="":
            files = glob.glob(os.path.join("./file_dir","*.pdf"),recursive=True)
        else:
            files = glob.glob(os.path.join("./file_dir", collection_name,"**","*.pdf"),recursive=True)
        cnt = 0
        Input_path = "./pdf"
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
            result = {"プロジェクト名":collection_name,"パス":file[11:],"ファイル名":filename,"text": text,"ファイル拡張子":"pdf","upload_data":dt_now}
            results.append(result)

        return results
            
    except Exception as e:
        print("pdf2textにてerror発生")
        return -1


# メイン処理
if __name__ == "__main__":
    # print("pdfminer.six ver.{}".format(pdfminer.__version__))
    results = func_pdf2text()
    print(results)



