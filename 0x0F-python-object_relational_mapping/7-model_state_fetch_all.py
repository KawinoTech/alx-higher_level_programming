#!/usr/bin/python3
"""
A script to connect to a MySQL database using SQLAlchemy, retrieve all records
from the 'states' table, and print them in ascending order by state name.

Usage:
    ./script_name.py <mysql_username> <mysql_password> <database_name>

    Example:
    ./script_name.py root password my_database
"""

from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys

# Ensure the script runs only if executed directly
if __name__ == "__main__":
    # Create a connection to the MySQL database
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(
            sys.argv[1],  # MySQL username
            sys.argv[2],  # MySQL password
            sys.argv[3]   # Database name
        ),
        pool_pre_ping=True
    )

    # Create all tables in the database (if they do not exist)
    Base.metadata.create_all(engine)

    # Create a session to interact with the database
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query all records from the 'states'
    # table, ordered by state name (ascending)
    all_states = session.query(State).order_by(State.id).all()

    # Loop through the query results and
    # print each state's name with an index
    i = 1
    for state in all_states:
        print("{:d}:".format(state.id), state.name)
        i += 1

    # Close the session to free up resources
    session.close()
