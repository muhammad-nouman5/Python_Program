import pymysql as mq
conn=mq.connect(
    host='localhost',
    user='root',
    password='',
    database='school'
)
cursorobj=conn.cursor()
print('{:<15}{:<20}{:<20}'.format('STATE_ID', 'STATE_NAME',
        'COUNTRY_ID'))
try:
    select='select * from state'
    cursorobj.execute(select)
    row=cursorobj.fetchall()
    for n in row:
        print('{:<15}{:<20}{:<20}'.format(n[0],n[1],n[2]))
except:    
    print("Error in Data Printing")
       