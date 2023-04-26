import mysql.connector

# cnx = None

# try:
#     cnx = mysql.connector.connect(
#         user='kouki',  # ユーザー名
#         password='password',  # パスワード
#         # host = "host.docker.internal"#hostは下記とどっちでも良い
#         host = "db"
#         database = "demo_db"
#     )
#     if cnx.is_connected:
#         print("Connected!")

#     with cnx.cursor() as cursor:


# except Exception as e:
#     print(f"Error Occurred: {e}")

# finally:
#     if cnx is not None and cnx.is_connected():
#         print("終了します")
#         cnx.close()

# Connect to the database
# データベースに接続
connection = mysql.connector.connect(user='kouki',  # ユーザー名
                                                password='password',  # パスワード
                                                # host = "host.docker.internal"#hostは下記とどっちでも良い
                                                host = "db",
                                                database = "demo_db"
                                            )


with connection:
    with connection.cursor() as cursor:
        # レコードを挿入
        sql = "INSERT INTO `honya` (`id`, `name`) VALUES (%s, %s)"
        cursor.execute(sql, (1, "test"))
 
    # コミットしてトランザクション実行
    connection.commit()
    print("終了")

