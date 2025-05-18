import mysql.connector
from mysql.connector import Error

try:
    # Connect to the database
    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password='your_password',
        database='your_database_name'
    )

    if connection.is_connected():
        cursor = connection.cursor()

        # SQL command to add a new table
        create_table_query = """
        CREATE TABLE IF NOT EXISTS employees (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(100),
            department VARCHAR(50),
            hire_date DATE
        );
        """
        cursor.execute(create_table_query)
        connection.commit()
        print("Table 'employees' has been created or already exists.")

except Error as e:
    print(f"Error: {e}")

finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("Database connection closed.")
