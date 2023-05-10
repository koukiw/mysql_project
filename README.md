# mysql_project
mysqlにフォルダごとファイル情報を保存していく



今後やること

1.pymsqlを用いてpythonからmysqlに接続（docker上に書き換える）

2.table修正

ローカルのpython上からmysql-connectorを使ってdocker上のmongoDBに接続.  

リポジトリをクローンして、   
/opt/file_dirに保存したいファイル・ディレクトリをアップロードしたのち   
./mysql_project配下にて
```python
docker-compose build --no-cache
```
にてコンテナ作成。それができたら、
```python
docker-compose up -d
```
でコンテナ起動。　　　
```python
docker-compose exec python3 bash
cd opt
python main.py
```


demo_db.demo_tableとdemo_db.text_tableテーブルにデータが格納されていることが確認できればOK
```python
docker-compose exec db bin/bash
```
でmysqlコンテナに入って
```python
mysql -u kouki -p password
```
でmysqlへ接続

```mysql
use demo_db
select * from demo_db;
```
