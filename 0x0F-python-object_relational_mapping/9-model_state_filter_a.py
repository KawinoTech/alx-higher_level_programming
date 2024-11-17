#!/usr/bin/python3

# Import necessary libraries and modules
from model_state import Base, State  # Importing the SQLAlchemy model and Base class
from sqlalchemy import create_engine  # For creating the engine to interact with the database
from sqlalchemy.orm import sessionmaker  # For creating a session to interact with the database
import sys  # To access command line arguments

# Entry point of the script
if __name__ == "__main__":
    # Establishing a connection to the MySQL database using credentials passed via command-line arguments
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(sys.argv[1],  # Database user
                                                                       sys.argv[2],  # Database password
                                                                       sys.argv[3]),  # Database name
                                                                       pool_pre_ping=True)  # Ensures that connections are alive before usage
    
    # Create the tables in the database based on the SQLAlchemy models
    Base.metadata.create_all(engine)

    # Creating a session to interact with the database
    Session = sessionmaker(bind=engine)
    session = Session()

    # Querying the 'states' table for records where the state name contains the letter 'a'
    all_states = session.query(State).filter(State.name.like('%a%')).all()
    
    # If any states are found, print their names with a counter
    if all_states:
        i = 1
        for state in all_states:
            print("{:d}:".format(i), state.name)  # Print the index and state name
            i += 1
    session.close()
