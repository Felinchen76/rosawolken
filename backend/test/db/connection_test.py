import os
import psycopg # python driver for postgres
from dotenv import load_dotenv

load_dotenv()

database_url = os.environ["DATABASE_URL"]

with psycopg.connect(database_url) as connection:
    print("Database connection successful!")