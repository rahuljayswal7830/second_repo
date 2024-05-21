import pymysql


con=pymysql.connect(host="localhost",port=3306,user="admin",password="admin@123",database="ICJS")
cursor=con.cursor()
command='''CREATE TABLE prod(
    id int  ,
    name CHAR(255)
    )'''


sql ='''CREATE TABLE EMPLOYEE(
   FIRST_NAME CHAR(20) NOT NULL,
   LAST_NAME CHAR(20),
   AGE INT,
   SEX CHAR(1),
   INCOME FLOAT
)'''
cursor.execute(command)
# cursor.commit()
cursor.close()
con.close()