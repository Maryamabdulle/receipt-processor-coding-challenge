
# from sqlalchemy import create_engine, Column, String, ARRAY, Integer, Time
# from sqlalchemy.ext.declarative import declarative_base
# import uuid
# from sqlalchemy import JSON
# Create an engine to connect to the database
# engine = create_engine("postgresql://maryamabdulle:mypassword@localhost:5432/testdb")
# Base = declarative_base()
#Changed the receipt class to store its data as a python dictionary, instead of using SQLAlchemy's ORM to map it to a database table. 
# I used the json module to read and wrire the data to a JSON file.

import json
import uuid

class Receipt():
    def __init__(self, id,retailer, purchase_date, purchase_time, items, total,points):
        self.data = {
            'id': id,
            'retailer': retailer,
            'purchase_date': purchase_date,
            'purchase_time': purchase_time,
            'items': items,
            'total': total,
            'points': points
        }

    @classmethod
    def from_json(cls, data):
        data = json.loads(data)
        return cls(**data)

    def to_json(self):
        return json.dumps(self.data)

    @staticmethod
    def load_data():
        try:
            with open('receipts.json', 'r') as file:
                data = json.load(file)
            return data
        except:
         return {}
        
    @staticmethod
    def save_data(data):
        with open('receipts.json', 'w') as file:
            json.dump(data, file)

def add_receipt(retailer, purchase_date, purchase_time, items, total,points):
    new_receipt = Receipt(uuid.uuid4().hex, retailer, purchase_date, purchase_time, items, total,points)
    existing_data = Receipt.load_data()
    existing_data.update({new_receipt.data['id']: new_receipt.data})
    try:
        Receipt.save_data(existing_data)
        print("Data saved successfully!")
    except:
        print("Error: Could not save data to json file.")


#Create a new receipt object
#new_receipt = Receipt(str(uuid.uuid4()),"Walmart", "2022-01-01", "12:00:00", [{"name": "item1","price": 10.0,"points":1},{"name": "item2","price": 20.0,"points":2}], 30.0,0)

#Load existing data from the json file
#existing_data = Receipt.load_data()

#Add the new receipt to the existing data
#existing_data.update({new_receipt.data['id']: new_receipt.data})

#Save the updated data back to the json file
#Receipt.save_data(existing_data)

#Print the data to check if the new receipt has been added
#print(existing_data)









# import json
# import uuid

# class Receipt():
#     def __init__(self, id,retailer, purchase_date, purchase_time, items, total,points):
#         self.data = {
#             'id': id,
#             'retailer': retailer,
#             'purchase_date': purchase_date,
#             'purchase_time': purchase_time,
#             'items': items,
#             'total': total,
#             'points': points
#         }

#     @classmethod
#     def from_json(cls, data):
#         data = json.loads(data)
#         return cls(**data)

#     def to_json(self):
#         return json.dumps(self.data)

#     @staticmethod
#     def load_data():
#         try:
#             with open('receipts.json', 'r') as file:
#                 data = json.load(file)
#             return data
#         except:
#          return []
        
#     @staticmethod
#     def save_data(data):
#         with open('receipts.json', 'w') as file:
#             json.dump(data, file)

# def add_receipt(retailer, purchase_date, purchase_time, items, total,points):
#     new_receipt = Receipt(uuid.uuid4().hex, retailer, purchase_date, purchase_time, items, total,points)
#     existing_data = Receipt.load_data()
#     existing_data.append(new_receipt.data)
#     try:
#         Receipt.save_data(existing_data)
#         print("Data saved successfully!")
#     except:
#         print("Error: Could not save data to json file.")


# #Create a new receipt object
# new_receipt = Receipt(str(uuid.uuid4()),"Walmart", "2022-01-01", "12:00:00", [{"name": "item1","price": 10.0,"points":1},{"name": "item2","price": 20.0,"points":2}], 30.0,0)

# #Load existing data from the json file
# existing_data = Receipt.load_data()

# #Add the new receipt to the existing data
# existing_data.append(new_receipt.data)

# #Save the updated data back to the json file
# Receipt.save_data(existing_data)

# #Print the data to check if the new receipt has been added
# print(existing_data)


















# import json
# import uuid

# class Receipt():
#     def __init__(self, id,retailer, purchase_date, purchase_time, items, total,points):
#         self.data = {
#             'id': id,
#             'retailer': retailer,
#             'purchase_date': purchase_date,
#             'purchase_time': purchase_time,
#             'items': items,
#             'total': total,
#             'points': points
#         }

#     @classmethod
#     def from_json(cls, data):
#         data = json.loads(data)
#         return cls(**data)

#     def to_json(self):
#         return json.dumps(self.data)

#     @staticmethod
#     def load_data():
#         try:
#             with open('receipts.json', 'r') as file:
#                 data = json.load(file)
#             return data
#         except:
#          return []
        
#     @staticmethod
#     def save_data(data):
#         with open('receipts.json', 'w') as file:
#             json.dump(data, file)

# def add_receipt(retailer, purchase_date, purchase_time, items, total):
#     new_receipt = Receipt(uuid.uuid4().hex, retailer, purchase_date, purchase_time, items, total,0)
#     existing_data = Receipt.load_data()
#     existing_data.update({new_receipt.data['id']: new_receipt.data})
#     try:
#         Receipt.save_data(existing_data)
#         print("Data saved successfully!")
#     except:
#         print("Error: Could not save data to json file.")


# #Create a new receipt object
# new_receipt = Receipt(str(uuid.uuid4()),"Walmart", "2022-01-01", "12:00:00", [{"name": "item1","price": 10.0},{"name": "item2","price": 20.0}], 30.0,0)

# #Load existing data from the json file
# existing_data = Receipt.load_data()

# #Add the new receipt to the existing data
# #existing_data.append(new_receipt.data)

# existing_data.update({new_receipt.data["id"]:new_receipt.data})

# #Save the updated data back to the json file
# Receipt.save_data(existing_data)

# #Print the data to check if the new receipt has been added
# print(existing_data)


















#####

# Call the add_receipt function
#     add_receipt("Walmart", "2022-01-01", "12:00:00", [{"name": "item1","price": 10.0},{"name": "item2","price": 20.0}], 30.0)

# # Save the updated data to the json file
#     Receipt.save_data(existing_data)

# # Load the data from the json file
#     existing_data = Receipt.load_data()

# # Print the data to check if the new receipt has been added
#     print(existing_data)



# # Example usage

# # Create a new receipt object
# new_receipt = Receipt(str(uuid.uuid4()),"Walmart", "2022-01-01", "12:00:00", [{"name": "item1","price": 10.0},{"name": "item2","price": 20.0}], 30.0,0)

# # Load existing data from the json file
# existing_data = Receipt.load_data()

# # Add the new receipt to the existing data
# #existing_data.append(new_receipt.data)

# # Save the updated data back to the json file
# Receipt.save_data(existing_data)

# # Load the data again to check that the new receipt was saved successfully
# loaded_data = Receipt.load_data()
# print(loaded_data)




























# Example usage

# Create a new receipt object
       # new_receipt = Receipt(str(uuid.uuid4()),"Walmart", "2022-01-01", "12:00:00", [{"name": "item1","price": 10.0},{"name": "item2","price": 20.0}], 30.0,0)
# Convert the receipt object to json format
# class Receipt(Base):
#     __tablename__ = "receipts"
#     id = Column (String, primary_key=True)
#     retailer = Column(String)
#     purchase_date = Column(String)
#     purchase_time = Column(Time)
#     items = Column(JSON)
#     total = Column(Integer)
#     points= Column(Integer) #default=0)


#     def __init__(self, id,retailer, purchase_date, purchase_time, items, total,points):
#         self.id=id
#         self.retailer = retailer
#         self.purchase_date = purchase_date
#         self.purchase_time = purchase_time
#         self.items = items
#         self.total = total
#         self.points=points


#     def serialize(self):
#         return {
#             'id': self.id,
#             'retailer': self.retailer,
#             'purchase_date': self.purchase_date,
#             'purchase_time': self.purchase_time,
#             'items': self.items,
#             'total': self.total,
#             'points': self.points
#         }

# Create the receipts table
#Base.metadata.create_all(engine)