from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Database configuration
DATABASE_URL = "sqlite:///./addresses.db"

# Create the database engine with SQLite
engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False}
)

# This creates our session factory - we'll use it to talk to the database
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class that all our database models will inherit from
Base = declarative_base()


def get_db():
    """
    Create a new database session for each request.
    After the request is done, we clean up the session.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
