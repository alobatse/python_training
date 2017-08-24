#import mysql.connector
import pymysql.cursors
#from fixture.db import DbFixture
from fixture.orm import ORMFixture
from model.group import Group


#connection = mysql.connector.connect(host="law-7", database="addressbook", user="root", password="")
#connection = pymysql.connect(host="law-7", database="addressbook", user="root", password="")
#db = DbFixture(host="law-7", name="addressbook", user="root", password="")
db = ORMFixture(host="law-7", name="addressbook", user="root", password="")


try:
    #cursor = connection.cursor()
    #cursor.execute("select * from group_list")
    #for row in cursor.fetchall():
    #    print(row)
    #groups = db.get_group_list()
    #groups = db.get_contact_list()
    groups = db.get_contacts_not_in_group(Group(id='113'))
    for group in groups:
        print (group)
    print (str(len(groups)))
finally:
    pass #db.destroy()
    #connection.close