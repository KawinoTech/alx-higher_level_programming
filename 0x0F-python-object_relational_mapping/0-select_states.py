#!/usr/bin/python3
"""
This script connects to a MySQL database using command-line arguments for
username, password, and database name. It retrieves all records from the 'states'
table and displays them in ascending order by their 'id'.

Usage:
    python script_name.py <username> <password> <database>

Positional arguments:
    username    The MySQL username.
    password    The MySQL password.
    database    The name of the MySQL database to connect to.

Example:
    python script_name.py root mypassword mydatabase

Dependencies:
    - MySQLdb (You can install it via: pip install mysqlclient)

Notes:
    - This script is designed to be run directly, not as an imported module.
    - If executed directly (i.e., when __name__ == "__main__"), the script will do nothing.
"""

if __name__ != "__main__":
    pass
else:
    from sys import argv
    import MySQLdb

    # Establishing a connection to the MySQL database
    db = MySQLdb.connect(
        host="localhost",
        user=f"{argv[1]}",
        passwd=f"{argv[2]}",
        db=f"{argv[3]}",
        port=3306
    )

    # Creating a cursor object to interact with the database
    cur = db.cursor()

    # Executing an SQL query to retrieve all rows from the 'states' table
    cur.execute("SELECT * FROM states ORDER BY id ASC")

    # Fetching all rows from the result of the query
    data = cur.fetchall()

    # Printing each row
    for i in data:
        print(i)
