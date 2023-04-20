import os
import glob
import pandas as pd
import csv

# csv_file = "./csv/dummyfile.csv"
# save_data_from_file(csv_file,",",)

# final_dict = [dic for index, dic in pd_dic.to_dict(orient="index").items() if index!=0]

# data = {}
# for index, dic in pd_dic.to_dict(orient="index").items():
#     data[index] = dic 
# print(data)


# CSVからテキストを抜き出してjson形式で情報を整理（keyはtitle、text,file_format）
def csv2text():
    process_name = ""
    try:
        #
        # PDF→テキスト情報抽出処理
        #
        process_name = "CSVからのテキスト情報抽出"
        files = glob.glob(os.path.join("./csv", "*.csv"))
        cnt = 0
        print(files)
        results = []
        for file in files:
            cnt += 1
            print("テキスト抽出処理中…（{}/{}）".format(cnt, len(files)))
            # PDFのテキスト取り出し
            print(file)

            pd_dic = pd.read_csv(file, sep=",")

            data = {}
            for index, dic in pd_dic.to_dict(orient="index").items():
                data["{}".format(index)] = dic 
            filename  = os.path.basename(file)
            # result = {"title":filename,"text": text,"file_format":"pdf"}
            result = {"title":filename,"text": data,"file_format":"csv"}
            results.append(result)


        return results
            
    except Exception as e:
        print("csv2textにてerror発生")
        return -1


# メイン処理
if __name__ == "__main__":
    # results = csv2text()
    files = glob.glob(os.path.join("./csv", "*.csv"))
    for file in files:
        print(file)
        with open(file, 'r') as f:
            reader = csv.reader(f)
            for line in reader:
                print(line)
                print(line[0])
    # print(len(results))
    # print(results)