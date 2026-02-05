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
3. Install dependencies:
   ```bash
   pip install fastapi sqlalchemy uvicorn
   ```

## Running the Application

```bash
uvicorn app.main:app --reload
```

The server will start at `http://127.0.0.1:8000`




