from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

# load .env file
load_dotenv()

# Define .env file for sales database
DB_USER = os.getenv('POSTGRES_USER')
DB_PASSWORD = os.getenv('POSTGRES_PASSWORD')
DB_HOST = os.getenv('POSTGRES_HOST')
DB_PORT = os.getenv('POSTGRES_PORT')
DB_NAME = os.getenv('POSTGRES_DB')

def sales_database_engine():
    """
    This function creates a PostgreSQL engine, which is used to load data into the sales database.
    
    """
    engine = create_engine(f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}")

    return engine

# Define .env file for load database
DB_USER_LOAD = os.getenv('POSTGRES_USER_LOAD')
DB_PASSWORD_LOAD = os.getenv('POSTGRES_PASSWORD_LOAD')
DB_HOST_LOAD = os.getenv('POSTGRES_HOST_LOAD')
DB_PORT_LOAD = os.getenv('POSTGRES_PORT_LOAD')
DB_NAME_LOAD = os.getenv('POSTGRES_DB_LOAD')


def dwh_load_engine():
    """
    This function creates a PostgreSQL engine, which is used to load data into the data warehouse.
   
    """
    engine = create_engine(f"postgresql://{DB_USER_LOAD}:{DB_PASSWORD_LOAD}@{DB_HOST_LOAD}:{DB_PORT_LOAD}/{DB_NAME_LOAD}")

    return engine