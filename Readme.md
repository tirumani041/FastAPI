# FastAPI Address Book Application

Simple address book - create, update, delete


## Requirements

- Python 3.7+
- FastAPI
- SQLAlchemy
- Uvicorn

## Installation

1. Create a virtual environment:
   ```bash
   python -m venv .venv
   ```

2. Activate the virtual environment:
   - On Windows:
     ```bash
     .venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source .venv/bin/activate
     ```

3. Install dependencies:
   ```bash
   pip install fastapi sqlalchemy uvicorn
   ```

## Running the Application

```bash
uvicorn app.main:app --reload
```

The server will start at `http://127.0.0.1:8000`

## API Documentation

Once the application is running, access the interactive API documentation at:
- **Swagger UI**: http://127.0.0.1:8000/docs
- **ReDoc**: http://127.0.0.1:8000/redoc

## API Endpoints

### Create an Address
```bash
POST /addresses/
Content-Type: application/json

{
  "name": "Main Office",
  "latitude": 40.7128,
  "longitude": -74.0060
}
```

### Get All Addresses
```bash
GET /addresses/
```

### Get a Specific Address
```bash
GET /addresses/{address_id}
```

### Update an Address
```bash
PUT /addresses/{address_id}
Content-Type: application/json

{
  "name": "Updated Name",
  "latitude": 40.7128,
  "longitude": -74.0060
}
```

### Delete an Address
```bash
DELETE /addresses/{address_id}
```

### Find Addresses Within a Distance
```bash
GET /addresses/search/nearby?latitude=40.7128&longitude=-74.0060&distance=10
```

This endpoint returns all addresses within the specified distance (in kilometers) from the given coordinates.

## Project Structure

```
FastAPI/
├── app/
│   ├── __init__.py
│   ├── main.py          # FastAPI application and endpoints
│   ├── models.py        # SQLAlchemy and Pydantic models
│   └── database.py      # Database configuration and session management
├── addresses.db         # SQLite database (created automatically)
└── README.md
```

## Database

The application uses SQLite for data persistence. The database file (`addresses.db`) is created automatically in the project root directory when you first run the application.

## Logging

The application includes comprehensive logging for debugging and monitoring:
- INFO level logs for major operations (create, update, delete, search)
- WARNING level logs for not found errors
- DEBUG level logs for detailed search results

## Best Practices Implemented

- ✅ **SQLAlchemy ORM** for type-safe database operations
- ✅ **Dependency Injection** using FastAPI's `Depends` for database sessions
- ✅ **Pydantic Models** for API request/response validation
- ✅ **Structured Logging** for debugging and monitoring
- ✅ **Error Handling** with appropriate HTTP status codes
- ✅ **Documentation** with docstrings and API tags
- ✅ **Distance Calculation** using accurate Haversine formula
- ✅ **Separation of Concerns** with dedicated modules for database, models, and application logic
3. Access the API documentation at `http://127.0.0.1:8000/docs`


## Owner words

