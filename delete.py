import pymysql as mq
conn=mq.connect(
    host='localhost',
    user='root',
    password='',
    database='school'
)
cursorobj=conn.cursor()
st_id=input("Enter Student ID for Deletions:- ")
sql_del='delete from student where st_id=%s'
try:
    cursorobj.execute(sql_del, st_id)
    conn.commit()
    print("Student Successfully Deleted")
except:
    print("Error in Student Deletion")