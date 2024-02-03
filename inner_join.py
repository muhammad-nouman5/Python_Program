import pymysql as mq
conn=mq.connect(
    host='localhost',
    user='root',
    password='',
    database='school'
)
cursorobj=conn.cursor()
print("{:<15}{:<20}{:<15}" .format('STATE_ID', 'STATE_NAME', 'COUNTRY_ID'))
try:
    sql='''select state.state_id, state.state_name, country.country_name
            from state inner join country on
            state.country_id=country.country_id'''
    cursorobj.execute(sql)
    sdata=cursorobj.fetchall()
    for n in sdata:
        print("{:<15}{:<20}{:<15}" .format(n[0], n[1], n[2]))
except:
    print("Error...")