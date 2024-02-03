import pymysql as mq 
conn=mq.connect(
    host='localhost',
    user='root',
    password='',
    database='school'
)
cursorobj=conn.cursor()
st_name=input("Enter Name:- ")
st_class=input("Enter Class:- ")
st_email=input("Enter Email:- ")
st_id=input("Enter ID:- ")
try:
    sql='''update student set st_name=%s, st_class=%s, st_email=%s
         where st_id=%s'''
    data=(st_name, st_class, st_email, st_id)
    cursorobj.execute(sql, data)
    conn.commit()
    print("Data Successfully Updated")
except:
    print("Error in Data Updation")