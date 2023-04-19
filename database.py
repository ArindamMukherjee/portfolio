import pymysql

# Establishing a connection to the database
connection = pymysql.connect(
    host='hanuman.chwhvj7eb3bv.us-east-1.rds.amazonaws.com',
    user='admin',
    password='12345678',
    db='mydatabase',
    connect_timeout=30
)

# Creating a cursor object
cursor = connection.cursor()

# Creating a table for storing sensor data
table_create_query = '''
    CREATE TABLE IF NOT EXISTS arindam_project (
    ID INT NOT NULL AUTO_INCREMENT,
    Projects VARCHAR(255) NOT NULL,
    PRIMARY KEY (ID)
);
'''
cursor.execute(table_create_query)



with connection.cursor() as cursor:
# Read a single record
  sql = "select * from arindam_project"
  cursor.execute(sql)
  result = cursor.fetchone()
  print(result)




# Closing the cursor and connection
cursor.close()
connection.close()