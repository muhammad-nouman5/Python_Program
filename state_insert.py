import pymysql as mq
conn=mq.connect(
    host='localhost',
    user='root',
    password='',
    database='school'
)
cursorobj=conn.cursor()
ins="insert into state(state_name, country_id)values(%s, %s)"
data=[('Rajasthan', '1'),
        ('Delhi', '1'),
        ('Victoria', '3'),
        ('Western_Australia', '3'),
        ('Colombo', '2'),
        ('Kandy', '2')]
try:
    cursorobj.executemany(ins, data)
    conn.commit()
    print("Data Inserted")
except:
    print("Error in Data Insertion")