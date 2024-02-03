import pymysql as mq
conn=mq.connect(
    host='localhost',
    user='root',
    password='',
    database='school'
)
cursorobj=conn.cursor()
try:
    sql='''create table state(
        state_id INT PRIMARY KEY AUTO_INCREMENT,
        state_name VARCHAR(25),
        country_id VARCHAR(10)
    )
    '''
    cursorobj.execute(sql)
    print("State Table Successfully Created")
except:
    print("Error in Table Creation")