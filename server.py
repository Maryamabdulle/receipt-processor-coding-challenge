from flask import Flask, request, jsonify
import json
import datetime

app = Flask(__name__)

# Load receipts data from JSON file
try:
    with open('receipts.json', 'r') as f:
        receipts_data = json.load(f)
except:
    receipts_data = []

@app.route('/receipts', methods=['GET'])
def get_all_receipts():
    """
    Returns all receipts in the JSON file
    """
    return jsonify(receipts_data), 200

@app.route('/receipts/<receipt_id>', methods=['GET'])
def get_receipt(receipt_id):
    """
    Returns a single receipt with the given ID
    """
    receipt = [r for r in receipts_data if r['id'] == int(receipt_id)][0]
    if receipt:
        return jsonify(receipt), 200
    else:
        return jsonify({'error': 'Receipt not found'}), 404

@app.route('/receipts/process', methods=['POST'])
def process_receipt():
    """
    Processes a receipt by inserting it into the JSON file and calculating the points awarded
    """
    data = request.get_json()
    # Validate receipt data
    if (data.get('retailer_name') and data.get('total') and data.get('items') and data.get('date') and data.get('time')):
        # Calculate points
        points = 0
        points += len([char for char in data.get('retailer_name') if char.isalnum()])
        if data.get('total') % 1 == 0:
            points += 50
        if data.get('total') % 0.25 == 0:
            points += 25
        points += (len(data.get('items')) // 2) * 5
        for item in data.get('items'):
            if (len(item.get('description').strip()) % 3 == 0):
                points += round(item.get('price') * 0.2)
        purchase_date = datetime.datetime.strptime(data.get('date'), '%Y-%m-%d')
        if purchase_date.day % 2 == 1:
            points += 6
        purchase_time = datetime.datetime.strptime(data.get('time'), '%H:%M:%S').time()
        if purchase_time > datetime.time(14, 0) and purchase_time < datetime.time(16, 0):
            points += 10
        # Insert receipt into JSON file
        data['points'] = points
        data['id'] = len(receipts_data)
        receipts_data.append(data)
        with open('receipts.json', 'w') as f:
            json.dump(receipts_data, f)
        return {"status": "success", "points": points}
    else:
        return {"status": "error", "message": "Invalid receipt data"}

@app.route('/receipts/<receipt_id>/points', methods=['GET'])
def get_points(receipt_id):
    """
    Returns the points awarded for a receipt with the given ID
    """
    receipt = [r for r in receipts_data if r['id'] == int(receipt_id)][0]
    if receipt:
        return jsonify({"points": receipt["points"]}), 200
    else:
        return jsonify({"error": "Receipt not found"}), 404

if __name__ == '__main__':
    app.run()










# import json
# from flask import Flask, jsonify, request
# import uuid
# import datetime
# app = Flask(__name__)
# #open the JSON file to read and write data
# with open("receipts.son","r") as f:
#     receipts = json.load(f)

# @app.route('/receipts', methods=['GET'])
# def get_all_receipts():
#     """
#     Returns all receipts in the database
#     """
#     receipts = session.query(Receipt).all()
#     return jsonify([receipt.serialize for receipt in receipts]), 200

# @app.route('/receipts/<receipt_id>', methods=['GET'])
# def get_receipt(receipt_id):
#     """
#     Returns a single receipt with the given ID
#     """
#     receipt = session.query(Receipt).filter_by(id=receipt_id).first()
#     if receipt:
#         return jsonify(receipt.serialize), 200
#     else:
#         return jsonify({'error': 'Receipt not found'}), 404


# @app.route('/receipts/process', methods=['POST'])
# def process_receipt():
#     """
#     Processes a receipt by inserting it into the database and calculating the points awarded
#     """
#     data = request.get_json()
#     # Validate receipt data
#     if (data.get('retailer') and data.get('purchase_date') and data.get('purchase_time') and data.get('items') and data.get('total') and isinstance(data.get('total'), (float))):
#         for item in data.get('items'):
#             if not (item.get('name') and item.get('price') and isinstance(item.get('price'), (float))):
#                 return jsonify({'error': 'Invalid receipt data'}), 400
#     # Assign ID to receipt
#     receipt_id = str(uuid.uuid4())
#     receipt = Receipt(id=receipt_id, retailer=data.get('retailor'), purchase_date=data.get('purchase_date'), purchase_time=data.get('purchase_time'), items=data.get('items'), total=data.get('total'),points=data.get('points'))
#     session.add(receipt)
#     session.commit()
#     # Calculate points based on receipt data
#     points = 0
#     #1 point for every alphanumeric character in the retailer name
#     points += sum(c.isalnum() for c in data.get('retailer'))
#     #50 points if the total is a round dollar amount with no cents
#     if data.get('total') % 1 == 0:
#         points += 50
#     #25 points if the total is a multiple of 0.25
#     if data.get('total') % 0.25 == 0:
#         points += 25
#     #5 points for every two items on the receipt
#     points += (len(data.get('items')) // 2) * 5
#     #If the trimmed length of the item description is a multiple of 3, multiply the price by 0.2 and round up to the nearest integer. The result is the number of points earned
#     for item in data.get('items'):
#         if len(item.get('name').strip()) % 3 == 0:
#             item_points = int(round(item.get('price') * 0.2))
#             points += item_points
#     #6 points if the day in the purchase date is odd
#     purchase_date = datetime.datetime.strptime(data.get('purchase_date'), '%Y-%m-%d')
#     if purchase_date.day % 2 == 1:
#         points += 6
#     #10 points if the time of purchase is after 2:00pm and before 4:00pm
#     purchase_time = datetime.datetime.strptime(data.get('purchase_time'), '%H:%M:%S').time()
#     if purchase_time >= datetime.time(14, 0) and purchase_time < datetime.time(16, 0):
#         points += 10

#     return jsonify({'id': receipt_id, 'points': points}), 200



# @app.route('/receipts/<receipt_id>/points', methods=['GET'])
# def get_points(receipt_id):
#     """
#     Returns the points awarded for a receipt with the given ID
#     """
#     receipt = session.query(Receipt).filter_by(id=receipt_id).first()
#     if receipt:
#         points = 0
#         for item in receipt.items:
#             points += item.get('price') * 100
#         return jsonify({'points': points}), 200
#     else:
#         return jsonify({'error': 'Receipt not found'}), 404

# if __name__ == "__main__":
#     app.run(debug=True,port=5001)  




















#######################
# @app.route('/receipts/process', methods=['POST'])
# def process_receipt():
#     """
#     Processes a receipt by inserting it into the database and calculating the points awarded
#     """
#     data = request.get_json()
#     # Validate receipt data
#     if (data.get('retailer') and data.get('purchase_date') and data.get('purchase_time') and data.get('items') and data.get('total') and isinstance(data.get('total'), (int, float))):
#         for item in data.get('items'):
#             if not (item.get('name') and item.get('price') and isinstance(item.get('price'), (int, float))):
#                 return jsonify({'error': 'Invalid receipt data'}), 400
#     # Assign ID to receipt
#     receipt_id = str(uuid.uuid4())
#     receipt = Receipt(id=receipt_id, retailer=data.get('retailer'), purchase_date=data.get('purchase_date'), purchase_time=data.get('purchase_time'), items=data.get('items'), total=data.get('total'))
#     session.add(receipt)
#     session.commit()

#     # Calculate points based on receipt data
#     points = 0
#     #1 point for every alphanumeric character in the retailer name
#     points += sum(c.isalnum() for c in data.get('retailer'))
#     #50 points if the total is a round dollar amount with no cents
#     if data.get('total') % 1 == 0:
#         points += 50
#     #25 points if the total is a multiple of 0.25
#     if data.get('total') % 0.25 == 0:
#      points += 25
#         #5 points for every two items on the receipt
#     points += (len(data.get('items')) // 2) * 5
#     #If the trimmed length of the item description is a multiple of 3, multiply the price by 0.2 and round up to the nearest integer. The result is the number of points earned
#     for item in data.get('items'):
#         if len(item.get('name').strip()) % 3 == 0:
#             item_points = int(round(item.get('price') * 0.2))
#             points += item_points
#     #6 points if the day in the purchase date is odd
#     import datetime
#     purchase_date = datetime.datetime.strptime(data.get('purchase_date'), '%Y-%m-%d')
#     if purchase_date.day % 2 == 1:
#         points += 6
#     #10 points if the time of purchase is after 2:00pm and before 4:00pm
#     purchase_time = datetime.datetime.strptime(data.get('purchase_time'), '%H:%M:%S')
#     if purchase_time.time() >= datetime.time(14, 0) and purchase_time.time() < datetime.time(16, 0):
#         points += 10

#     return jsonify({'id': receipt_id,'points': points}), 200













 


# from flask import Flask, jsonify, request
# from uuid import uuid4

# app = Flask(__name__)

# # In-memory storage for receipts
# receipts = {}

# @app.route('/receipts', methods=['GET'])
# def get_all_receipts():
#     return jsonify(receipts), 200

# @app.route('/receipts/<receipt_id>', methods=['GET'])
# def get_receipt(receipt_id):
#     receipt = receipts.get(receipt_id)
#     if receipt:
#         return jsonify(receipt), 200
#     else:
#         return jsonify({'error': 'Receipt not found'}), 404

# @app.route('/receipts/process', methods=['POST'])
# def process_receipt():
#     data = request.get_json()
#     # Validate receipt data
#     if (data.get('retailer') and data.get('purchaseDate') and data.get('purchaseTime') and data.get('items') and data.get('total') and all(isinstance(i, dict) for i in data.get('items')) and all(i.get('shortDescription') and i.get('price') for i in data.get('items')) and isinstance(data.get('total'), (int, float))):
#         # Assign ID to receipt
#         receipt_id = str(uuid4())
#         receipts[receipt_id] = data
#         # Calculate points based on receipt data
#         points = 0
#         for item in data['items']:
#             points += int(float(item['price']) * 100)
#         # Return receipt ID
#         return jsonify({'id': receipt_id,'points': points}), 200
#     else:
#         return jsonify({'error': 'Invalid receipt data'}), 400

# @app.route('/receipts/<receipt_id>/points', methods=['GET'])
# def get_points(receipt_id):
#     # Retrieve receipt
#     receipt = receipts.get(receipt_id)
#     if receipt:
#         # Calculate points based on receipt data
#         points = 0
#         for item in receipt['items']:
#             points += int(float(item['price']) * 100)
#         return jsonify({'points': points}), 200
#     else:
#         return jsonify({'error': 'Receipt not found'}), 404

# if __name__ == '__main__':
#     app.run(debug=True, host='0.0.0.0',port=5000)