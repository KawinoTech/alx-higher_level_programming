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
import sys

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

    # Querying the 'states' table for a state with a name
    # matching the 4th command-line argument
    state = session.query(State).filter_by(name=sys.argv[4]).first()

    # If the state is found, print its ID. If not, print "Not Found"
    if state:
        print(state.id)  # Print the ID of the found state
    else:
        print("Not Found")  # If no state is found, print "Not Found"
    session.close()
