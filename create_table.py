import pymysql as mq
conn=mq.connect(
    host='localhost',
    user='root',
    password='',
    database='school'
)
cursorobj=conn.cursor()
try:
    tb='''create table student(
        st_id INT AUTO_INCREMENT PRIMARY KEY,
        st_name VARCHAR(50),
        st_class VARCHAR(10),
        st_email VARCHAR(20)
    )'''
    cursorobj.execute(tb)
    print("Successfully Table Created")
except:
    print("Error in Table Creation")