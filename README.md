# mysql_project
mysqlにフォルダごとファイル情報を保存していく

進捗

pdfからデータカタログ，テキストデータをmysqlに保存する際に日本語データの文字化け発生中．

unicodeからutf-8に設定を変えていると思うが，文字化けが治っていない．



今後やること

1.pdfができたら，他のファイルフォーマットも同様に保存する．

2.データカタログとテキストデータの抽出コードを分ける．

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
