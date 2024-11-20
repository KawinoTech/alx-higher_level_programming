#!/usr/bin/python3
"""
This script connects to a MySQL database using command-line arguments for
username, password, and database name.
It retrieves all records from the 'states'
where the name of the state starts with N.

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
    - This scrip is designed to be run directly, not as an imported module.
    - If executed directly (i.e., when __name__ == "__main__"),
    the script will do nothing.
"""
from sys import argv
import MySQLdb

if __name__ == "__main__":

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

    # Using parameterized query to prevent SQL injection
    cur.execute("""SELECT s.id, c.name, s.name \
                FROM `states` AS s \
                JOIN `cities` as c \
                ON s.id = c.state_id""")

    # Fetching all rows from the result of the query
    rows = cur.fetchall()
    for row in rows:
        print(row)