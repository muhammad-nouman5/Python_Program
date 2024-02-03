import pymysql as mq
conn=mq.connect(
    host='localhost',
    user='root',
    password=''
)
cursorobj=conn.cursor()
try:
    db="create database school"
    cursorobj.execute(db)
    print("Successfully Database Created")
except:
    print("Error in Database Creation")