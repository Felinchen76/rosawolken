from fastapi import FastAPI, Depends
from rosawolken.database import get_connection
from psycopg import Connection

app = FastAPI()

@app.get("/")
def root():
    return {"message": "hello from rosawolken:)"}

@app.get("/users")
def get_users(connection: Connection = Depends(get_connection)):
    with connection.cursor() as cursor:
        cursor.execute("SELECT id, username FROM users;")
        users = cursor.fetchall()

    connection.close
    return users

@app.get("/images")
def get_images(onnection: Connection = Depends(get_connection)):
    with connection.cursor() as cursor:
        cursor.execute("SELECT id, filename FROM images;")
        images = cursor.fetchall()
    return images

@app.get("/folders")
def get_folders(onnection: Connection = Depends(get_connection)):
    with connection.cursor as cursor:
        cursor.execute("SELECT id, name FROM folders")
    return folders
