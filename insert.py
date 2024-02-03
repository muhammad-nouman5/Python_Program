import pymysql as mq
conn=mq.connect(
    host='localhost',
    user='root',
    password='',
    database='school'
)
cursorobj=conn.cursor()
try:
    ins='insert into student(st_name, st_class, st_email) values(%s,%s,%s)'
    t=[('Aziz','12th', 'zaheer@gmail.com'),
        ('NoMi', '12th', 'nomi@gmail.com'), ('Asad', '12th', 'asad@gmail.com'),
        ('Faizan', '12th', 'faizan@gmail.com')]
    cursorobj.executemany(ins, t)
    conn.commit()
    print("Successfully Data Inserted")
except:
    print("Error in Data Insertion")