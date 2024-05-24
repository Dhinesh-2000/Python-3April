import mysql.connector
import requests

resp=requests.get('https://jsonplaceholder.typicode.com/users')
user_list=resp.json()

print(type(user_list))
data=[]
for user in user_list:
    data.append((user['id'],user['name'],user['email'],user['address']['city'],user['phone']))


try:
    dbcon=mysql.connector.connect(host='localhost',user='root',password='root',database='9am')
    cursor=dbcon.cursor()
    sql_st='''
            insert into users values(%s,%s,%s,%s,%s);
           '''
    cursor.executemany(sql_st,data)
    dbcon.commit()
    print("Data inserted successfully")
except mysql.connector.Error as err:
    print(err)
finally:
    cursor.close()
    dbcon.close()