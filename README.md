# Receipt Processor Coding Challenge

This is a receipt processing web service built using Python 3, Flask, and JSON data. The service allows users to input receipts, store them in a JSON file, and calculate the points awarded for each receipt based on certain conditions.

## Requirements

- Python 3.6 or higher
- Flask
- JSON
- datetime

## Installing

- Clone the repository: https://github.com/Maryamabdulle/receipt-processor-coding-challenge.git
- Create a virtual environment and activate it:
`virtualenv env`
`source env/bin/activate`

- Install the required packages: `pip install -r requirements.txt`

- The code uses a JSON file called receipts.json to store the receipts. If this file is not found in the same directory as the code, the code will create an empty JSON file with that name.

## Running the code

- To run the code, use the following command: `python3 server.py`

- To run the model.py, use the following command: `python3 model.py` and expected output should be:
`{'receipts': [{'id': 1, 'retailer': 'Walmart', 'purchase_date': '2022-01-01', 'purchase_time': '10:00:00', 'items': [{'name': 'Toothpaste', 'price': 2.99}, {'name': 'Toothbrush', 'price': 4.99}], 'total': 7.98, 'points': 0}, {'id': 2, 'retailer': 'Costco', 'purchase_date': '2022-01-02', 'purchase_time': '11:00:00', 'items': [{'name': 'Shampoo', 'price': 6.99}, {'name': 'Conditioner', 'price': 8.99}], 'total': 15.98, 'points': 0}], 'd5a34eb7-0838-4384-9051-fca0c224158a': {'id': 'd5a34eb7-0838-4384-9051-fca0c224158a', 'retailer': 'Walmart', 'purchase_date': '2022-01-01', 'purchase_time': '12:00:00', 'items': [{'name': 'item1', 'price': 10.0, 'points': 1}, {'name': 'item2', 'price': 20.0, 'points': 2}], 'total': 30.0, 'points': 0}, 'ab841729-eba2-4c45-821f-408b18bae219': {'id': 'ab841729-eba2-4c45-821f-408b18bae219', 'retailer': 'Walmart', 'purchase_date': '2022-01-01', 'purchase_time': '12:00:00', 'items': [{'name': 'item1', 'price': 10.0, 'points': 1}, {'name': 'item2', 'price': 20.0, 'points': 2}], 'total': 30.0, 'points': 0}, '01306e83-f7dc-4d72-8258-a320004ec662': {'id': '01306e83-f7dc-4d72-8258-a320004ec662', 'retailer': 'Walmart', 'purchase_date': '2022-01-01', 'purchase_time': '12:00:00', 'items': [{'name': 'item1', 'price': 10.0, 'points': 1}, {'name': 'item2', 'price': 20.0, 'points': 2}], 'total': 30.0, 'points': 0}, '744e44a9-ea08-4971-b4ba-b50f486b6bc7': {'id': '744e44a9-ea08-4971-b4ba-b50f486b6bc7', 'retailer': 'Walmart', 'purchase_date': '2022-01-01', 'purchase_time': '12:00:00', 'items': [{'name': 'item1', 'price': 10.0, 'points': 1}, {'name': 'item2', 'price': 20.0, 'points': 2}], 'total': 30.0, 'points': 0}}`

- The code will start a local server on port 5000.

## Endpoints

The following endpoints are available:

- POST /receipts: Adds a new receipt to the JSON file. The request body should contain a JSON object with the following keys: retailer_name, total, items, date, and time.
- GET /receipts: Returns all receipts in the JSON file.
- GET /receipts/<receipt_id>: Returns a single receipt with the given ID.
- POST /receipts/process: Processes a receipt by inserting it into the JSON file and calculating the points awarded.

## Error Handling

- In case of invalid data, the server will return a JSON object with an error key and a relevant message.

- In case of any other error, the server will return a JSON object with a status key with the value error and a message key with a relevant message.

## Testing the endpoints

- You can use any tool that allows you to make HTTP requests, such as CURL, to test the various request types (GET, POST, PATCH, DELETE) to the correct endpoint URLs.

- For example, you can use the following command to send a GET request to the /receipts endpoint:

`curl -X GET http://127.0.0.1:5000/receipts`

- It will return a JSON object containing all the receipts data. You can also test the other endpoints in a similar way.

- For example, you can use the following command to send a POST request to the /receipts/process endpoint:

`import flask`
`import requests`
`import json`
`response = requests.post("http://127.0.0.1:5000/receipts/process", json={"retailer": "Walmart","purchase_date": "2022-01-01", "purchase_time": "12:00:00","items":[{"name": "item1","price": 10.0},{"name": "item2","price": 20.0}],"total": 30.0,"points":0})`
`print(response)`

- It should return a Response [200] if successful, but if there's an error it will return Response [500].



## Note:

Please contact me at iammaryamabdulle@gmail.com if you have any questions. 

Thank you 




























<!-- 
################

# Installing

1. Clone the repository 
- `https://github.com/Maryamabdulle/receipt-processor-coding-challenge.git`


2. Create a virtual environment and activate it

- `virtualenv env`
- `source env/bin/activate`


3. Install the required packages 
- `pip install -r requirements.txt`

4. Create a new database and update the SQLAlchemy connection string in server.py with your own database credentials

- `engine = create_engine("postgresql://maryamabdulle:mypassword@localhost:5432/testdb")`


5. Create the necessary tables by running the following command:

- `python3 database.py`
- `python2 model.py`

6. Run the server
- `python3 server.py`

7. Test the endpoints 

## Usage

# The Project routes:

- GET /receipts: Returns all receipts in the database
- GET /receipts/<receipt_id>: Returns a single receipt with the given ID
- POST /receipts/process: Processes a receipt by inserting it into the database and calculating the points awarded


## Test the endpoints by making requests to the URLs 

- You can use any tool that allows you to make HTTP requests, such as CURL so that user is able to make the various request types (GET, POST, PATCH, DELETE) to the correct endpoint URLs.

## For example, I can use the following command to send a GET request to the /receipts endpoint:
- `curl -X GET http://127.0.0.1:5001/receipts`
- It will return a JSON object containing all the receipts data
- You can also test the other endpoints in a similar way.

## For example, I  can use the following command To sent a POST request to the /receipts/process and before that run these interactively on terminal:
- `python`
- `import flask`
- `import requests`
- `response = requests.post("http://127.0.0.1:5001/receipts/process",json={"retailer": "Walmart","purchase_date": "2022-01-01" "purchase_time": "12:00:00","items":[{"name": "item1","price": 10.0},{"name": "item2","price": 20.0}],"total": 30.0,"points":0})`
- `print(response)`

- It should be returning: Response[200] if its successful but if there's an error than it will return Response[500]


## Note:

Please contact me at iammaryamabdulle@gmail.com if you have any questions. 

Thank you  -->