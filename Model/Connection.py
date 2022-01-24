import mysql.connector
from Config.Settings import DATABASE_NAME, DATABASE_PASSWORD, DATABASE_USER, DATABASE_HOST

try:
    connection = mysql.connector.connect(
        host=DATABASE_HOST,
        user=DATABASE_USER,
        password=DATABASE_PASSWORD,
        database=DATABASE_NAME
    )
except mysql.connector.Error as e:
    print("Connection Failed", e)


def querySQL(sql):
    cursor = connection.cursor()
    cursor.execute(sql)
    records = cursor.fetchall()
    return records
