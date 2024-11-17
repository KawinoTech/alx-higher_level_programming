#!/usr/bin/python3

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
                           .format(sys.argv[1],  # Database user
                                    sys.argv[2],  # Database password
                                    sys.argv[3]),  # Database name
                                    pool_pre_ping=True)
    
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
