from fastapi import FastAPI 

app = FastAPI()

@app.get("/")
def root():
    return {"message": "hello from rosawolken:)"}

@app.get("/users")
def get_users():
    from rosawolken.database import get_connection
    connection = get_connection()
    with connection.cursor() as cursor:
        cursor.execute("SELECT id, username FROM users;")
        users = cursor.fetchall()

    connection.close
    return users


