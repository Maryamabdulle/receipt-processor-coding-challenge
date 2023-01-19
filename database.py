from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from model import Base, Receipt

# Connect to the database
engine = create_engine("postgresql://maryam:mypassword@localhost:5000/testdb")
Base.metadata.create_all(bind=engine)

# Create a session
session_factory = sessionmaker(bind=engine)
Session = scoped_session(session_factory)
session = Session()

def create_receipt(retailer, purchase_date, purchase_time, items, total):
    new_receipt = Receipt(retailer=retailer, purchase_date=purchase_date, purchase_time=purchase_time, items=items, total=total)
    session.add(new_receipt)
    session.commit()
    return new_receipt.id

def get_receipt(receipt_id):
    receipt = session.query(Receipt).filter_by(id=receipt_id).first()
    if receipt:
        return receipt.serialize
    else:
        return None

def update_receipt(receipt_id, retailer, purchase_date, purchase_time, items, total):
    receipt_to_update = session.query(Receipt).filter_by(id=receipt_id).first()
    if receipt_to_update:
        receipt_to_update.retailer = retailer
        receipt_to_update.purchase_date = purchase_date
        receipt_to_update.purchase_time = purchase_time
        receipt_to_update.items = items
        receipt_to_update.total = total
        session.commit()
        return True
    else:
        return False

def delete_receipt(receipt_id):
    receipt_to_delete = session.query(Receipt).filter_by(id=receipt_id).first()
    if receipt_to_delete:
        session.delete(receipt_to_delete)
        session.commit()
        return True
    else:
        return False

def close_session():
    session.close()


if __name__ == "__main__":
    # Test the create_receipt function
    new_receipt_id = create_receipt("Walmart", "2022-01-01", "12:00:00", [{"name": "item1", "price": 10.0}, {"name": "item2", "price": 20.0}], 30.0)
    print(new_receipt_id)

    # Test the get_receipt function
    receipt = get_receipt(new_receipt_id)
    print(receipt)
    
    # Test the update_receipt function
    update_receipt(new_receipt_id, "New Retailer", "2022-01-01", "12:00:00", [{"name": "item1", "price": 10.0}, {"name": "item2", "price": 20.0}], 30.0)
    receipt = get_receipt(new_receipt_id)
    print(receipt)
    
    # Test the delete_receipt function
    delete_receipt(new_receipt_id)
    receipt = get_receipt(new_receipt_id)
    print(receipt)
    
    # Close the session
    close_session()