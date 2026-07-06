import pymysql

try:
    connection = pymysql.connect(
        host="localhost",
        user="root",
        password="Pass@123",
        database="medimind_ai"
    )

    print("Connected Successfully!")

    connection.close()

except Exception as e:
    print(e)