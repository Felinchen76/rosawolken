import os
import psycopg
from dotenv import load_dotenv

load_dotenv()

database_url = os.environ("DATABASE_URL")

def get_connection():
    return psycopg.connect(database_url)