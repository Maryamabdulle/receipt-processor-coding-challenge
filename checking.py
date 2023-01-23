# note to myself: testing to check if the receipts table exists in my database which it gave me that table exist so that's good

from sqlalchemy import create_engine
from database import engine
from database import Base

#Create an engine to connect to the database

engine=create_engine("postgresql://maryamabdulle:mypassword@localhost:5432/testdb")
Base.metadata.bind = engine
from sqlalchemy import MetaData

meta = MetaData()
meta.reflect(bind=engine)
if 'receipts' in meta.tables:
    print("table exist")
else:
    print("table does not exist")

