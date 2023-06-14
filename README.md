# mysql_project
mysqlにフォルダごとファイル情報を保存していく

docke上で起動させたpythonからmysql-connectorを使ってdocker上別コンテナのmysqlに保存.  


進捗

text_tableのtextカラムの最大文字数をvarchra(15000)に設定．
utf8mb4に設定しているので，最大文字数16383になると思ったが，これだと
initdb.d/reate_table.sqlから自動生成できない．

手順 

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

## データカタログ作成．　　　
```python
docker-compose exec python3 bash
cd opt
python data.py
```

## テキストデータ抽出．　　

## unoconv使用方法
コンテナ起動時にシェルスクリプトを動かそうとするとコンテナが起動できないので、手動でシェルスクリプトを実行する必要がある。

```python
docker-compose exec python3 bash /src/init.sh
```
で/usr/bin/unooncv内のshebangを書き換えることでunoconvコマンドが使用可能になる。

上記を行ったのち、
```python
docker-compose exec python3 bash
cd opt
python text.py
```


demo_db.demo_tableにデータカタログ，

demo_db.text_tableテーブルにテキストデータが格納されていることが確認できればOK
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
select * from demo_table;
select * from text_table;
```
