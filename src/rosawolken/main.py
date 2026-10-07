from fastapi import FastAPI 

app = FastAPI()

@app.get("/")
def root():
    return {"message": "hello from rosawolken:)"}

@app.get("/images")
def get_images():
    return [
    {"id": "1", "filename": "urlaub.jpg"},
    {"id": "2", "filename": "katze.jpg"},
]