import mysql.connector

try:
    dbcon=mysql.connector.connect(host='localhost',user='root',password='root',database='9am')
    cursor=dbcon.cursor()
    sql_st='select * from employee;'
    cursor.execute(sql_st)
    employee_data=cursor.fetchall()

 

    for emp in employee_data:
        print(emp)

except mysql.connector.Error as err:
    print(err)
finally:
    cursor.close()
    dbcon.close()
