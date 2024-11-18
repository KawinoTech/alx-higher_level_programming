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
                           .format(sys.argv[1],
                                   sys.argv[2],
                                   sys.argv[3]), pool_pre_ping=True)

    # Create the tables in the database based on the SQLAlchemy models
    Base.metadata.create_all(engine)

    # Creating a session to interact with the database
    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State).filter(State.name.like('%a%')).all()

    if states:
        # Updating the state's name to the new name passed as the 5th argument
        for state in states:
            session.delete(state)
        # Committing the changes to the database
    session.commit()
    session.close()
