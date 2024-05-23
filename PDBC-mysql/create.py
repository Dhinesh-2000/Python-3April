import mysql.connector

try:
    dbcon=mysql.connector.connect(user='root', password='root',
                              host='127.0.0.1', database='9am',
                              auth_plugin='mysql_native_password')
    cur=dbcon.cursor()
    sql_st=''' 
        create table employee(
            eid int, 
            ename varchar(32),
            esal int
        );
       ''' 
    cur.execute(sql_st)
    print('Table created successfully')
except mysql.connector.Error as err:
    print(err)
    print('Unable to connect')