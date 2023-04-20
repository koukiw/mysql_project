import os
import glob
import pandas as pd

# csv_file = "./csv/dummyfile.csv"
# save_data_from_file(csv_file,",",)

# final_dict = [dic for index, dic in pd_dic.to_dict(orient="index").items() if index!=0]

# data = {}
# for index, dic in pd_dic.to_dict(orient="index").items():
#     data[index] = dic 
# print(data)


# CSVからテキストを抜き出してjson形式で情報を整理（keyはtitle、text,file_format）
def csv2text(collection_name,dt_now):
    process_name = ""
    try:
        #
        # PDF→テキスト情報抽出処理
        #
        process_name = "CSVからのテキスト情報抽出"
        # files = glob.glob(os.path.join("./csv", "*.csv"))
        # files = glob.glob(os.path.join('./file_dir/**', "*.csv"),recursive=True)
        if collection_name =="":
            files = glob.glob(os.path.join("./file_dir","*.csv"),recursive=True)
        else:
            files = glob.glob(os.path.join("./file_dir", collection_name,"**","*.csv"),recursive=True)
        cnt = 0
        print(files)
        results = []
        results_excel = []
        for file in files:
            cnt += 1
            print("csvテキスト抽出処理中…（{}/{}）".format(cnt, len(files)))

            pd_dic = pd.read_csv(file, sep=",")

            data = {}
            for index, dic in pd_dic.to_dict(orient="index").items():
                data["{}".format(index)] = dic
            # テキストの加工
            data = str(data)
            data = data.replace("\n","").replace("\r","").replace("\t","").strip()

            filename  = os.path.basename(file)
            columns = pd_dic.columns.tolist()
            # result = {"title":filename,"text": text,"file_format":"pdf"}
            result = {"プロジェクト名":collection_name,"パス":file[11:],"ファイル名":filename,"text": data,"ファイル拡張子":"csv","upload_data":"2022/4/19"}
            results.append(result)
            filename_excel = filename[:-3] + "xlsx"
            result_excel = {"プロジェクト名":collection_name,"パス":file[11:],"ファイル名":filename,"text": data,"ファイル拡張子":"excel","upload_data":dt_now}
            results_excel.append(result_excel)

            


        return results,results_excel
            
    except Exception as e:
        print("csv2textにてerror発生")
        return -1


# メイン処理
if __name__ == "__main__":
    results = csv2text()
    # print(len(results))
    # print(results)