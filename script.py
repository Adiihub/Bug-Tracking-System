import mysql.connector
from mysql.connector import Error

try:
    # Establish a connection to MySQL
    conn = mysql.connector.connect(
        host="localhost",
        user="admin",  # Replace with your MySQL username
        password="password"  # Replace with your MySQL password
    )

    if conn.is_connected():
        print("Successfully connected to MySQL")

        cursor = conn.cursor()

        # Create the BTS database
        cursor.execute("CREATE DATABASE IF NOT EXISTS BTS;")
        cursor.execute("USE BTS;")

        # Create the employee table
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS employee (
            empLoginId VARCHAR(10) PRIMARY KEY,
            empPassword VARCHAR(20),
            empType VARCHAR(20),
            empName VARCHAR(45),
            empPhone VARCHAR(10),
            empEmail VARCHAR(45),
            empStatus VARCHAR(20) DEFAULT 'ACTIVE'
        );
        """)

        # Insert data into employee table
        cursor.execute("""
        INSERT INTO employee(empLoginId, empPassword, empType, empName, empPhone, empEmail)
        VALUES('AD1001', 'password', 'ADMIN', 'Priti Singh', '9998887776', 'help@admin.com');
        """)

        cursor.execute("""
        INSERT INTO employee(empLoginId, empPassword, empType, empName, empPhone, empEmail)
        VALUES('EX3001', 'password', 'EXPERT', 'DemoUser', '4444444', 'expert@admin.com');
        """)

        # Create the customer table
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS customer (
            custLoginId VARCHAR(10) PRIMARY KEY,
            custPassword VARCHAR(20),
            custName VARCHAR(45),
            custAge INT,
            custPhone VARCHAR(10),
            custEmail VARCHAR(45)
        );
        """)

        # Insert data into customer table
        cursor.execute("""
        INSERT INTO customer(custLoginId, custPassword, custName, custAge, custPhone, custEmail)
        VALUES('CU2001', 'password', 'Priya', 21, '9998887776', 'priya@demo.com');
        """)

        cursor.execute("""
        INSERT INTO customer(custLoginId, custPassword, custName, custAge, custPhone, custEmail)
        VALUES('CU2002', 'password', 'Anjali', 22, '9998887776', 'anjali@demo.com');
        """)

        # Create the Bug table
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS Bug (
            bugId INT PRIMARY KEY AUTO_INCREMENT,
            bugPostingDate DATETIME DEFAULT NOW(),
            custLoginId VARCHAR(10) NOT NULL,
            bugStatus VARCHAR(20) DEFAULT 'New Bug',
            productName VARCHAR(45) NOT NULL,
            bugDesc TEXT NOT NULL,
            expertAssignedDate DATETIME DEFAULT NULL,
            expertLoginId VARCHAR(10) DEFAULT NULL,
            bugSolvedDate DATETIME DEFAULT NULL,
            solution TEXT DEFAULT NULL,
            FOREIGN KEY (custLoginId) REFERENCES customer(custLoginId),
            FOREIGN KEY (expertLoginId) REFERENCES employee(empLoginId)
        );
        """)

        # Insert data into Bug table
        cursor.execute("""
        INSERT INTO Bug(custLoginId, productName, bugDesc)
        VALUES('CU2001', 'Laptop', 'Screen is flickering');
        """)

        cursor.execute("""
        INSERT INTO Bug(custLoginId, productName, bugDesc)
        VALUES('CU2001', 'Mobile', 'Keyboard not working.');
        """)

        cursor.execute("""
        INSERT INTO Bug(custLoginId, productName, bugDesc)
        VALUES('CU2002', 'Laptop', 'Wifi connection issues');
        """)

        # Commit the changes
        conn.commit()
        print("Tables created and data inserted successfully.")

except Error as e:
    print(f"Error: {e}")

finally:
    if conn.is_connected():
        cursor.close()
        conn.close()
        print("MySQL connection is closed")
