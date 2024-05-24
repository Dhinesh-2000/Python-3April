import mysql.connector
from mysql import *

try:
    dbcon=mysql.connector.connect(host='localhost',user='root',password='root',database='9am')
    cur=dbcon.cursor()
    sql_st='''
            insert into employee values(%s,%s,%s)
           '''
    data=[(102,'Sonia',65000),(103,'Priyanka',55000)]
    cur.executemany(sql_st,data)
    dbcon.commit()
    print("Data Inserted successfully")

except mysql.connector.Error as err:
    print(err)

finally:
    cur.close()
    dbcon.close()

