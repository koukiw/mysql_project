import pandas as pd
from pdfminer.high_level import extract_text
from docx import Document
from openpyxl import load_workbook
from pptx import Presentation
import subprocess
import os


def extract_text_from_file(filepath):
    try:
        file_format = os.path.splitext(filepath)[1] [1:]
        if file_format =="pdf":
            text = pdf2text(filepath)
        elif file_format =="csv":
            text = csv2text(filepath)
        elif file_format =="xlsx":
            text = excel2text(filepath)
        elif file_format =="docx":
            text = docx2text(filepath)
        elif file_format =="doc":
            text = doc2text(filepath)
        elif file_format =="pptx":
            text = pptx2text(filepath)
        return text
    
    except Exception as e:
        print("get_textにてerror発生")
        return -1
    

# PDFからテキストを抜き出す
def pdf2text(file):
    try:
        # テキストの抜き出し
        text = extract_text(file)
        # テキストの加工
        text = text.replace("\n","").replace("\r","").replace("\t","").strip()
        # print(text[:50])
        return text
            
    except Exception as e:
        print("pdf2textにてerror発生")
        return -1

# CSVからテキストを抜き出してjson形式で情報を整理
def csv2text(file):
    try:
        pd_dic = pd.read_csv(file, sep=",")
        text = {}
        for index, dic in pd_dic.to_dict(orient="index").items():
            text["{}".format(index)] = dic
        # テキストの加工
        text = str(text)
        text = text.replace("\n","").replace("\r","").replace("\t","").strip()
        # print(text)
        return text

    except Exception as e:
        print("csv2textにてerror発生")
        return -1
    
def excel2text(file):
    try:
        workbook = load_workbook(file)
        sheet_names= workbook.sheetnames
        strings={}
        for index in range(len(sheet_names)):
            sheet = workbook[sheet_names[index]]

            string = []

            for row in sheet.iter_rows(values_only=True):
                for cell in row:
                    if isinstance(cell, str):
                        string.append(cell)
            strings[sheet_names[index]] = string
            

        return str(strings)
    
    except Exception as e:
        print("excel2textにてerror発生")
        return -1


#  .docxからテキストを抜き出す
def docx2text(file):
    try:
        text = ""
        document = Document(file)
        for i, p in enumerate(document.paragraphs):
            text += p.text

        # 表中のテキスト抽出
        for i, t in enumerate(document.tables):
            for j, r in enumerate(t.rows):
                for k, c in enumerate(r.cells):
                    text += c.text
        # テキストの加工
        text = text.replace("\n","").replace("\r","").replace("\t","").strip()
        # print(text)
        return text
        
    except Exception as e:
        print("word2textにてerror発生")
        return -1

#  .docからテキストを抜き出す
def doc2text(file_path):
    try:
        command = f"antiword  {file_path}"
        print(command)
        output = subprocess.check_output(command, shell=True)
        text = output.decode('utf-8')
        text = text.replace("\n","").replace("\r","").replace("\t","").replace(" ","").replace("　","").strip()
        print(text)
        return text
    except subprocess.CalledProcessError:
        print("doc2textにてerror発生")
        return -1

def pptx2text(file):
    try:
        strings = []
        prs = Presentation(file)
        for i, sld in enumerate(prs.slides, start=1):
            for shp in sld.shapes:
                if shp.has_text_frame:
                    strings.append(shp.text)
                #テーブル（表）からも文字列抽出
                if shp.has_table:
                    tables =[]
                    for row in shp.table.rows:
                        values = [ cell.text for cell in row.cells ]
                        tables.append(values)
                    strings.append(tables)
        return str(strings)
    except Exception as e:
        print("pptx2textにてerror発生")
        return -1

# メイン処理
if __name__ == "__main__":
    # print("pdfminer.six ver.{}".format(pdfminer.__version__))
    results = pdf2text()
    print(results)

