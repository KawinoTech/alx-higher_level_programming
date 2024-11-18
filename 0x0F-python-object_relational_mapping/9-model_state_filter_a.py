#!/usr/bin/python3
"""
A script to connect to a MySQL database using SQLAlchemy,
retrieve the first record from the 'states' table ordered by 'id',
and print it.

Usage:
    ./script_name.py <mysql_username> <mysql_password> <database_name>

Example:
    ./script_name.py root password my_database
"""
# Import necessary libraries and modules
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys  # To access command line arguments

# Entry point of the script
if __name__ == "__main__":
    # Establishing a connection to the MySQL
    # database using credentials passed via command-line arguments
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1],
                                   sys.argv[2],
                                   sys.argv[3]), pool_pre_ping=True)

    # Create the tables in the database based on the SQLAlchemy models
    Base.metadata.create_all(engine)

    # Creating a session to interact with the database
    Session = sessionmaker(bind=engine)
    session = Session()

    all_states = session.query(State).filter(State.name.like('%a%')).all()

    # If any states are found, print their names with a counter
    if all_states:
        i = 1
        for state in all_states:
            print("{:d}:".format(i), state.name)
            i += 1
    session.close()
