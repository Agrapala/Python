import mysql.connector
query = "CREATE TABLE users(name VARCHAR(20), age INT);"
query = "INSERT INTO users VALUES ('Samitha', 23);"
try:
    connection = mysql.connector.connect(
        host='localhost',
        database='test_db',
        user= 'samitha',
        password='S*****'
    )
    cursor = connection.cursor()
    cursor.execute(query)

    connection.commit()

except :
    print("Error while connecting to MySQL")