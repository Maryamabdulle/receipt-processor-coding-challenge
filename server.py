from flask import Flask, jsonify, request
from sqlalchemy import create_engine, String, Time, ARRAY
from sqlalchemy.orm import sessionmaker
from model import Receipt, Base
import uuid

app = Flask(__name__)

# Create an engine to connect to the database
engine = create_engine("postgresql://maryam:mypassword@localhost:5000/testdb")
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

@app.route('/receipts', methods=['GET'])
def get_all_receipts():
    """
    Returns all receipts in the database
    """
    receipts = session.query(Receipt).all()
    return jsonify([receipt.serialize for receipt in receipts]), 200

@app.route('/receipts/<receipt_id>', methods=['GET'])
def get_receipt(receipt_id):
    """
    Returns a single receipt with the given ID
    """
    receipt = session.query(Receipt).filter_by(id=receipt_id).first()
    if receipt:
        return jsonify(receipt.serialize), 200
    else:
        return jsonify({'error': 'Receipt not found'}), 404

@app.route('/receipts/process', methods=['POST'])
def process_receipt():
    """
    Processes a receipt by inserting it into the database and calculating the points awarded
    """
    data = request.get_json()
    # Validate receipt data
    if (data.get('retailer') and data.get('purchase_date') and data.get('purchase_time') and data.get('items') and data.get('total') and isinstance(data.get('total'), (int, float))):
        for item in data.get('items'):
            if not (item.get('name') and item.get('price') and isinstance(item.get('price'), (int, float))):
                return jsonify({'error': 'Invalid receipt data'}), 400
    # Assign ID to receipt
    receipt_id = str(uuid.uuid4())
    receipt = Receipt(id=receipt_id, retailer=data.get('retailer'), purchase_date=data.get('purchase_date'), purchase_time=data.get('purchase_time'), items=data.get('items'), total=data.get('total'))
    session.add(receipt)
    session.commit()
    
    # Calculate points based on receipt data
    items = data.get('items')
    points = 0
    for item in items:
        points += int(float(item['price']) * 100)
    
    # Return receipt ID
        return jsonify({'id': receipt_id,'points': points}), 200
    else:
        return jsonify({'error': 'Invalid receipt data'}), 400
@app.route('/receipts/<receipt_id>/points', methods=['GET'])
def get_points(receipt_id):
    """
    Returns the points awarded for a receipt with the given ID
    """
    receipt = session.query(Receipt).filter_by(id=receipt_id).first()
    if receipt:
        points = 0
        for item in receipt.items:
            points += item.get('price') * 100
        return jsonify({'points': points}), 200
    else:
        return jsonify({'error': 'Receipt not found'}), 404

if __name__ == "__main__":
    app.run(debug=True)   
    
   














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