#import mysql.connector
import pymysql.cursors


#connection = mysql.connector.connect(host="law-7", database="addressbook", user="root", password="")
connection = pymysql.connect(host="law-7", database="addressbook", user="root", password="")
try:
    cursor = connection.cursor()
    cursor.execute("select * from group_list")
    for row in cursor.fetchall():
        print(row)
finally:
    connection.close