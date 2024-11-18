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
        pool_pre_ping=True  # Ensures the connection is checked before use
    )

    # Create all tables defined by the Base's metadata (if they do not exist)
    Base.metadata.create_all(engine)

    # Create a session to interact with the database
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query the first record from the 'states' table, ordered by 'id'
    state = session.query(State).order_by(State.id).first()

    # If a state is found, print its details
    if state:
        print("{:d}:".format(1), state.name)

    # Close the session
    session.close()
