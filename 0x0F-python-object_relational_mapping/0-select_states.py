#!/usr/bin/python3
"""
This script connects to a MySQL database using command-line arguments for
username, password, and database name.
It retrieves all records from the 'states'
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
    - If executed directly (i.e., when __name__ == "__main__"),
    the script will do nothing.
"""
from sys import argv
import MySQLdb

if __name__ == "__main__":

    # Unpack command-line arguments
    username, password, database = argv[1], argv[2], argv[3]

    # Connect to the MySQL database on localhost at port 3306
    db = MySQLdb.connect(
        host="localhost",
        user=username,
        passwd=password,
        db=database,
        port=3306
    )

    # Creating a cursor object to interact with the database
    cur = db.cursor()

    # Executing an SQL query to retrieve all rows from the 'states' table
    cur.execute("SELECT * FROM states ORDER BY states.id ASC")

    # Fetching all rows from the result of the query
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
