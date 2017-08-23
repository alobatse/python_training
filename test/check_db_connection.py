#import mysql.connector
import pymysql.cursors
from fixture.db import DbFixture


#connection = mysql.connector.connect(host="law-7", database="addressbook", user="root", password="")
#connection = pymysql.connect(host="law-7", database="addressbook", user="root", password="")
db = DbFixture(host="law-7", name="addressbook", user="root", password="")

try:
    #cursor = connection.cursor()
    #cursor.execute("select * from group_list")
    #for row in cursor.fetchall():
    #    print(row)
    groups = db.get_group_list()
    for group in groups:
        print (group)
    print (str(len(groups)))
finally:
    db.destroy()
    #connection.close