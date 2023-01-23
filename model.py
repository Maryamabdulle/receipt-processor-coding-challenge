from sqlalchemy import create_engine, Column, String, ARRAY, Integer, Time
from sqlalchemy.ext.declarative import declarative_base
import uuid
from sqlalchemy import JSON


# Create an engine to connect to the database
engine = create_engine("postgresql://maryamabdulle:mypassword@localhost:5432/testdb")


Base = declarative_base()

class Receipt(Base):
    __tablename__ = "receipts"
    id = Column (String, primary_key=True)
    retailer = Column(String)
    purchase_date = Column(String)
    purchase_time = Column(Time)
    items = Column(JSON)
    total = Column(Integer)
    points= Column(Integer) #default=0)


    def __init__(self, id,retailer, purchase_date, purchase_time, items, total,points):
        self.id=id
        self.retailer = retailer
        self.purchase_date = purchase_date
        self.purchase_time = purchase_time
        self.items = items
        self.total = total
        self.points=points


    def serialize(self):
        return {
            'id': self.id,
            'retailer': self.retailer,
            'purchase_date': self.purchase_date,
            'purchase_time': self.purchase_time,
            'items': self.items,
            'total': self.total,
            'points': self.points
        }

# Create the receipts table
#Base.metadata.create_all(engine)