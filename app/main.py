from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
import logging
import os

from .database import engine, Base, get_db
from .models import Address, AddressCreate, AddressUpdate

# Set up logging to save to file and console
log_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
log_file = os.path.join(log_dir, "app.log")

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(log_file),  # Save to file
        logging.StreamHandler()  # Also print to console
    ]
)
logger = logging.getLogger(__name__)

# Create the database tables if they don't exist yet
Base.metadata.create_all(bind=engine)

# amin fast api
app = FastAPI(
    title="Address Book API",
    description="A simple API to perform update,create and delete",
    version="1.0.0"
)


@app.post("/addresses/", tags=["Addresses"])
def create_address(address: AddressCreate, db: Session = Depends(get_db)):
    """
    Add a new address to your book.
    """
    logger.info(f"Creating address: {address.name}")
    
    db_address = Address(
        name=address.name,
        latitude=address.latitude,
        longitude=address.longitude
    )
    db.add(db_address)
    db.commit()
    db.refresh(db_address)
    
    logger.info(f"Address created with ID: {db_address.id}")
    return db_address


@app.get("/addresses/", tags=["Addresses"])
def get_all_addresses(db: Session = Depends(get_db)):
    """
    Get all your addresses.
    """
    logger.info("Fetching all addresses")
    addresses = db.query(Address).all()
    return addresses


@app.get("/addresses/{address_id}", tags=["Addresses"])
def get_address(address_id: int, db: Session = Depends(get_db)):
    """
    Get a specific address by ID.
    """
    logger.info(f"Fetching address {address_id}")
    
    db_address = db.query(Address).filter(Address.id == address_id).first()
    if not db_address:
        logger.warning(f"Address {address_id} not found")
        raise HTTPException(status_code=404, detail="Address not found")
    
    return db_address


@app.put("/addresses/{address_id}", tags=["Addresses"])
def update_address(
    address_id: int,
    address_update: AddressUpdate,
    db: Session = Depends(get_db)
):
    """
    Update an address.
    """
    logger.info(f"Updating address {address_id}")
    
    db_address = db.query(Address).filter(Address.id == address_id).first()
    if not db_address:
        logger.warning(f"Address {address_id} not found")
        raise HTTPException(status_code=404, detail="Address not found")
    
    if address_update.name is not None:
        db_address.name = address_update.name
    if address_update.latitude is not None:
        db_address.latitude = address_update.latitude
    if address_update.longitude is not None:
        db_address.longitude = address_update.longitude
    
    db.commit()
    db.refresh(db_address)
    
    logger.info(f"Address {address_id} updated")
    return db_address


@app.delete("/addresses/{address_id}", tags=["Addresses"])
def delete_address(address_id: int, db: Session = Depends(get_db)):
    """
    Delete an address.
    """
    logger.info(f"Deleting address {address_id}")
    
    db_address = db.query(Address).filter(Address.id == address_id).first()
    if not db_address:
        logger.warning(f"Address {address_id} not found")
        raise HTTPException(status_code=404, detail="Address not found")
    
    db.delete(db_address)
    db.commit()
    
    logger.info(f"Address {address_id} deleted")
    return {"message": "Address deleted"}
