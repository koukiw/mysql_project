import glob
import os
import openpyxl

#更新するExcelシート番号（左から0,1,2)
Sheet_Num = 0

#Excelファイル
#
#テキスト情報抽出処理
#
process_name = "excelからのテキスト情報抽出"
# files = glob.glob(os.path.join("./excel", "*.xlsx"))
files = glob.glob(os.path.join('./file_dir/**', "*.xlsx"),recursive=True)
cnt = 0
Input_path = "./excel"
print(files[0])
# ExcelFileName = FileName + Extension
#ワークブック読込
workbook = openpyxl.load_workbook(files[0])
#ワークシート読込
# Selectworksheet = workbook.get_sheet_names()[Sheet_Num]
Selectworksheet = workbook.sheetnames
# worksheet = workbook.get_sheet_by_name(Selectworksheet[0])
worksheet = workbook[Selectworksheet[0]]

print(Selectworksheet)
print(worksheet)