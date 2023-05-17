import pandas as pd
from pdfminer.high_level import extract_text
from docx import Document
from openpyxl import load_workbook

# PDFからテキストを抜き出す
def pdf2text(file):
    try:
        # テキストの抜き出し
        text = extract_text(file)
        # テキストの加工
        text = text.replace("\n","").replace("\r","").replace("\t","").strip()
        print(text[:50])
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


#  wordからテキストを抜き出す
def word2text(file):
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

# メイン処理
if __name__ == "__main__":
    # print("pdfminer.six ver.{}".format(pdfminer.__version__))
    results = pdf2text()
    print(results)

