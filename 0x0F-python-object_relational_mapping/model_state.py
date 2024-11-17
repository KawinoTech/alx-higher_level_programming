from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base

# Define a base class for all models
Base = declarative_base()

class State(Base):
    """
    A class to represent the 'states' table in a database.
    
    Attributes:
    ----------
    id : int
        The primary key for each state (auto-incremented).
    name : str
        The name of the state (non-null, up to 128 characters).
    """

    __tablename__ = 'states'

    id = Column('id', Integer, primary_key=True, nullable=False, unique=True, autoincrement=True)
    """
    Column: id
    ----------
    - Type: Integer
    - Primary Key: Yes
    - Nullable: No
    - Unique: Yes
    - Auto-Increment: Yes

    Represents the unique identifier for each state.
    """

    name = Column('name', String(128), nullable=False)
    """
    Column: name
    ----------
    - Type: String (with a max length of 128 characters)
    - Nullable: No

    Represents the name of the state.
    """
