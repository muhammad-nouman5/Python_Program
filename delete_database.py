
import pymysql as mq

# Connect to MySQL server (replace 'username', 'password', and 'database_name' with your own details)
conn = mq.connect(user='root', password='', host='localhost', database='school')

# Create a cursor object to execute SQL queries
cursor = conn.cursor()

# Define the database name to be deleted
database_name = 'your_database_name'

# Delete the database
delete_database_query = f"DROP DATABASE IF EXISTS school"
cursor.execute(delete_database_query)

# Commit the changes
conn.commit()

# Close the cursor and connection
cursor.close()
conn.close()
