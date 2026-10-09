from fastapi import FastAPI, Depends, Request
from rosawolken.database import get_connection
from psycopg import Connection

from fastapi.responses import JSONResponse

app = FastAPI()

@app.middleware("http")
async def public_test_only(request: Request, call_next):
    if request.url.path != "/":
        return JSONResponse(
            status_code=404,
            content={"detail": "Not found"}
        )

    return await call_next(request)

@app.get("/")
def root():
    return {"message": "hello from rosawolken:)"}

@app.get("/users")
def get_users(connection: Connection = Depends(get_connection)):
    with connection.cursor() as cursor:
        cursor.execute("SELECT id, username FROM users;")
        users = cursor.fetchall()
    return users

@app.get("/images")
def get_images(connection: Connection = Depends(get_connection)):
    with connection.cursor() as cursor:
        cursor.execute("SELECT id, filename FROM images;")
        images = cursor.fetchall()
    return images

@app.get("/folders")
def get_folders(connection: Connection = Depends(get_connection)):
    with connection.cursor() as cursor:
        cursor.execute("SELECT id, name FROM folders;")
        folders = cursor.fetchall()
    return folders
