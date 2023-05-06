import pymysql

def load_data_from_db():
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

    # Read data from the table
    sql = "SELECT * FROM projects"
    cursor.execute(sql)
    result = cursor.fetchall()

    # Convert the data to a list of dictionaries
    data = []
    for row in result:
        data.append({
            'id': row[0],
            'title': row[1]
        })

    # Closing the cursor and connection
    cursor.close()
    connection.close()

    return data
