from sqlalchemy import create_engine, Column, String, ARRAY
from sqlalchemy.ext.declarative import declarative_base
import uuid


# Create an engine to connect to the database
engine = create_engine("postgresql://maryam:mypassword@localhost:5000/testdb")

Base = declarative_base()

class Receipt(Base):
    __tablename__ = "receipts"
    id = Column(String, primary_key=True, default=str(uuid.uuid4()))
    retailer = Column(String)
    purchase_date = Column(String)
    purchase_time = Column(String)
    items = Column(ARRAY)
    total = Column(String)


    def __init__(self, retailer, purchase_date, purchase_time, items, total):
        self.retailer = retailer
        self.purchase_date = purchase_date
        self.purchase_time = purchase_time
        self.items = items
        self.total = total

    def serialize(self):
        return {
            'id': self.id,
            'retailer': self.retailer,
            'purchase_date': self.purchase_date,
            'purchase_time': self.purchase_time,
            'items': self.items,
            'total': self.total
        }

# Create the receipts table
Base.metadata.create_all(engine)