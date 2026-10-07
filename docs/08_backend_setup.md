# Backend Setup

## Goal

The first goal is to build a small FastAPI backend for the `rosawolken` photo cloud.

The backend will later handle:

* authentication
* image uploads
* image downloads
* image metadata
* permissions
* communication between the frontend, database, and file storage

For now, the goal is only to get a minimal API running!

---

## Project Structure

The Python project was initialized with `uv`.

Current structure:

```text
rosawolken/
├── README.md
├── docs/
├── src/
│   └── rosawolken/
│       ├── __init__.py
│       └── main.py
├── tests/
├── .gitignore
├── pyproject.toml
└── uv.lock
```

### `__init__.py`

`__init__.py` marks `rosawolken` as a Python package.

It allows modules to be imported using the package name, for example:

```python
from rosawolken.main import app
```

---

## FastAPI

FastAPI is used as the backend web framework.

Install the dependencies:

```bash
uv add fastapi uvicorn
```

* **FastAPI** provides the API framework and routing.
* **Uvicorn** is the ASGI server that runs the FastAPI application.

---

## First API Endpoint

The first endpoint is implemented in:

```text
src/rosawolken/main.py
```

```python
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def root():
    return {"message": "Hello from rosawolken!"}
```

### How routing works

The decorator

```python
@app.get("/")
```

defines a route.

It means:

> When the server receives a `GET` request for `/`, execute the `root()` function.

The basic flow is:

```text
GET /
  ↓
FastAPI routing
  ↓
root()
  ↓
JSON response
```

The `@` syntax is a Python decorator. FastAPI uses it to associate a Python function with an HTTP route.

---

## Running the Backend

From the repository root:

```bash
uv run uvicorn rosawolken.main:app --reload
```

The development server runs on:

```text
http://127.0.0.1:8000
```

`--reload` automatically restarts the development server when Python files change.

### If port 8000 is already in use

Check which process is using it:

```bash
ss -ltnp | grep :8000
```

If an old Uvicorn process is still running:

```bash
pkill -f uvicorn
```

Then start the server again!

Alternatively, use another port:

```bash
uv run uvicorn rosawolken.main:app --reload --port 8001
```

---

## Testing the API

Opening

```text
http://127.0.0.1:8000/
```

should return:

```json
{
    "message": "Hello from rosawolken!"
}
```

FastAPI also automatically generates interactive API documentation.

Open:

```text
http://127.0.0.1:8000/docs
```

The documentation provides an interactive interface for testing API endpoints directly from the browser.

---

## First Additional Endpoint

A first placeholder endpoint for images can be added:

```python
@app.get("/images")
def get_images():
    return []
```

Later this endpoint will retrieve image metadata from PostgreSQL.

---

## Planned Backend Architecture

The planned backend architecture is:

```text
Browser / Phone
       │
       │ HTTP
       ▼
   FastAPI
       │
       ├──────────────► PostgreSQL
       │                 metadata
       │
       └──────────────► File Storage
                         actual images
```

PostgreSQL will store metadata such as:

```text
id
user_id
filename
storage_path
size
mime_type
created_at
updated_at
```

The actual image files will be stored on the HDD rather than directly inside PostgreSQL.

