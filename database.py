import json
from datetime import datetime, time
import uuid

# Create a new receipt in the json file
def create_receipt(retailer, purchase_date, purchase_time, items, total,points=0):
    id = str(uuid.uuid4())
    new_receipt = {
        "id": id,
        "retailer": retailer,
        "purchase_date": purchase_date,
        "purchase_time": purchase_time,
        "items": items,
        "total": total,
        "points": points
    }
    with open("receipts.json", "r") as json_file:
        data = json.load(json_file)
    data["receipts"].append(new_receipt)
    with open("receipts.json", "w") as json_file:
        json.dump(data, json_file)
    return id

# Get a receipt from the json file
def get_receipt(receipt_id):
    with open("receipts.json", "r") as json_file:
        data = json.load(json_file)
    for receipt in data["receipts"]:
        if receipt["id"] == receipt_id:
            return receipt
    return None

def add_receipt(new_receipt):
    try:
        with open('receipts.json', 'r') as json_file:
            data = json.load(json_file)
    except:
        # Handle the exception here, for example by returning a message to the user
        return "Error: Could not read json file"
    # Append the new receipt data to the existing data
    data['receipts'].append(new_receipt)
    # Save the updated data to the json file
    with open("receipts.json","w") as json_file:
        json.dump(data,json_file)


def update_receipt(receipt_id, retailer, purchase_date, purchase_time, items, total):
    with open("receipts.json", "r") as json_file:
        data = json.load(json_file)
    for i, receipt in enumerate(data["receipts"]):
        if receipt["id"] == receipt_id:
            data["receipts"][i]["retailer"] = retailer
            data["receipts"][i]["purchase_date"] = purchase_date
            data["receipts"][i]["purchase_time"] = purchase_time
            data["receipts"][i]["items"] = items
            data["receipts"][i]["total"] = total
            with open("receipts.json", "w") as json_file:
                json.dump(data, json_file)
            return True
    return False

def delete_receipt(receipt_id):
    with open("receipts.json", "r") as json_file:
        data = json.load(json_file)
    for i, receipt in enumerate(data["receipts"]):
        if receipt["id"] == receipt_id:
            del data["receipts"][i]
            with open("receipts.json", "w") as json_file:
                json.dump(data, json_file)
            return True
    return False

def get_all_receipts():
    with open("receipts.json", "r") as json_file:
        data = json.load(json_file)
    return data["receipts"]

# def get_receipt(receipt_id):
#     with open("receipts.json", "r") as json_file:
#         data = json.load(json_file)
#     for receipt in data["receipts"]:
#         if receipt["id"] == receipt_id:
#             return receipt
#     return None

   

























# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker, scoped_session
# from model import Base, Receipt
# from datetime import datetime, time
# import uuid
# from sqlalchemy import JSON


# # Connect to the database
# engine = create_engine("postgresql://maryamabdulle:mypassword@localhost:5432/testdb")
# Base.metadata.create_all(bind=engine)

# # Create a session
# session_factory = sessionmaker(bind=engine)
# Session = scoped_session(session_factory)
# session = Session()

# def create_receipt(retailer, purchase_date, purchase_time, items, total,points=0):
#     id = str(uuid.uuid4())
#     new_receipt = Receipt(id=id, retailer=retailer, purchase_date=purchase_date, purchase_time=purchase_time, items=items, total=total,points=points)
#     session.add(new_receipt)
#     session.commit()
#     return new_receipt.id


# def get_receipt(receipt_id):
#     receipt = session.query(Receipt).filter_by(id=receipt_id).first()
#     if receipt:
#         return receipt.serialize
#     else:
#         return None

# def update_receipt(receipt_id, retailer, purchase_date, purchase_time, items, total):
#     receipt_to_update = session.query(Receipt).filter_by(id=receipt_id).first()
#     if receipt_to_update:
#         receipt_to_update.retailer = retailer
#         receipt_to_update.purchase_date = purchase_date
#         receipt_to_update.purchase_time = purchase_time
#         receipt_to_update.items = items
#         receipt_to_update.total = total
#         session.commit()
#         return True
#     else:
#         return False

# def delete_receipt(receipt_id):
#     receipt_to_delete = session.query(Receipt).filter_by(id=receipt_id).first()
#     if receipt_to_delete:
#         session.delete(receipt_to_delete)
#         session.commit()
#         return True
#     else:
#         return False

# def close_session():
#     session.close()


# def process_receipt(receipt_id):
#     receipt = session.query(Receipt).filter_by(id=receipt_id).first()
#     date_object = datetime.strptime(receipt.purchase_date, '%Y-%m-%d')
#     if receipt:
#         points = 0
#         # Check if the total is a round dollar amount with no cents
#         if receipt.total % 1 == 0:
#             points += 50
#         # Check if the total is a multiple of 0.25
#         if receipt.total * 4 % 1 == 0:
#             points += 25
#         # Add 5 points for every two items on the receipt
#         points += (len(receipt.items) // 2) * 5
#         for item in receipt.items:
#             # Check if the trimmed length of the item description is a multiple of 3
#             if len(item.get("name").strip()) % 3 == 0:
#                 points += int(float(item.get("price")) * 0.2)
#         # Check if the day in the purchase date is odd
#         #if int(receipt.purchase_date.day) % 2 != 0:
#         if datetime.strptime(receipt.purchase_date, '%Y-%m-%d').day % 2 != 0:
#             points += 6
#         # Check if the time of purchase is after 2:00pm and before 4:00pm
#         if receipt.purchase_time >= time(14,0,0) and receipt.purchase_time < time(16,0,0):
#             points += 10
#         receipt.points = points
#         session.commit()
#         return points
#     else:
#         return None


# def close_session():
#     session.close() 


# if __name__ == "__main__":

#     # # Test the process_receipt function
#     receipt_id = create_receipt("Walmart", "2022-01-01", time(12,0,0), [{"name": "item1", "price": 10.0}, {"name": "item2", "price": 20.0}], 30.0)
#     points = process_receipt(receipt_id)
#     print(points)
#     close_session()

    # # Test the process_receipt function
    # points = process_receipt("Walmart", "2022-01-01", datetime.time(12,0,0), [{"name": "item1", "price": 10.0}, {"name": "item2", "price": 20.0}], 30.0)
    # print(points)

    # # # Test the create_receipt function
    # new_receipt_id = create_receipt("Walmart", "2022-01-01", datetime.time(12,0,0), [{"name": "item1", "price": 10.0}, {"name": "item2", "price": 20.0}], 30.0, points) 
    # print(new_receipt_id)

    # # # Test the get_receipt function
    # receipt = get_receipt(new_receipt_id)
    # print(receipt)
    
    # # # Test the update_receipt function
    # update_receipt(new_receipt_id, "New Retailer", "2022-01-01", "12:00:00", [{"name": "item1", "price": 10.0}, {"name": "item2", "price": 20.0}], 30.0)
    # receipt = get_receipt(new_receipt_id)
    # print(receipt)
    
    # # # Test the delete_receipt function
    # delete_receipt(new_receipt_id)
    # receipt = get_receipt(new_receipt_id)
    # print(receipt)
    

    # # # Close the session
    # close_session()












    # # Test the create_receipt function
    # new_receipt_id = create_receipt("Walmart", "2022-01-01", datetime.time(12,0,0), [{"name": "item1", "price": 10.0}, {"name": "item2", "price": 20.0}], 30.0) 
    # print(new_receipt_id)

    # # Test the process_receipt function
    # points = process_receipt(new_receipt_id)
    # print(points)

    # Test the get_receipt function
    # receipt = get_receipt(new_receipt_id)
    # print(receipt)
    
    # # Test the update_receipt function
    # update_receipt(new_receipt_id, "New Retailer", "2022-01-01", "12:00:00", [{"name": "item1", "price": 10.0}, {"name": "item2", "price": 20.0}], 30.0)
    # receipt = get_receipt(new_receipt_id)
    # print(receipt)
    
    # # Test the delete_receipt function
    # delete_receipt(new_receipt_id)
    # receipt = get_receipt(new_receipt_id)
    # print(receipt)
    




    # # Close the session
    # close_session()


    # Test the create_receipt function
    #new_receipt_id = create_receipt("Walmart", "2022-01-01", datetime.time(12,0,0), [{"name": "item1", "price": 10.0}, {"name": "item2", "price": 20.0}], 30.0) 
    #print(new_receipt_id)
        
    #     ("Walmart", "2022-01-01", datetime.time(12,0,0), [{"name": "item1", "price": 10.0}, {"name": "item2", "price": 20.0}], 30.0, 0)
    # print(new_receipt_id)

    # Test the get_receipt function
    # receipt = get_receipt(new_receipt_id)
    # print(receipt)
    
    # # Test the update_receipt function
    # update_receipt(new_receipt_id, "New Retailer", "2022-01-01", "12:00:00", [{"name": "item1", "price": 10.0}, {"name": "item2", "price": 20.0}], 30.0)
    # receipt = get_receipt(new_receipt_id)
    # print(receipt)
    
    # # Test the delete_receipt function
    # delete_receipt(new_receipt_id)
    # receipt = get_receipt(new_receipt_id)
    # print(receipt)
    
    # Close the session
    #close_session()