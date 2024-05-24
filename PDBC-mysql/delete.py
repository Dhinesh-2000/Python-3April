import mysql.connector

try:
    dbcon=mysql.connector.connect(host='localhost',user='root',password='root',database='9am')
    cursor=dbcon.cursor() 
    sql_st='delete from employee'
    cursor.execute(sql_st)
    dbcon.commit()
    print("all rows deleted")

   

except mysql.connector.Error as err:
    print(err) 

finally:
    cursor.close()
    dbcon.close()