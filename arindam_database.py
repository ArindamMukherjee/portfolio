import pymysql
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

def load_data_from_db():
    # Read data from the table
    with connection.cursor() as cursor:
        sql = "SELECT * FROM arindam_project"
        cursor.execute(sql)
        result = cursor.fetchall()

    # Convert the data to a list of dictionaries
    data = []
    for row in result:
        data.append({
            'id': row[0],
            'title': row[1]
        })

    return data

    cursor.close()
    connection.close()
    