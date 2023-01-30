# Receipt Processor Coding Challenge

This is a receipt processing web service that allows users to input receipts, store them in a JSON file, and calculate the points awarded for each receipt based on certain conditions. It is built using Python 3, Flask, and JSON data, and requires Python 3.6 or higher, Flask, and JSON to be installed. The application is designed to work with receipt data, which is loaded from a JSON file called "receipts.json" when the server starts up.

## Requirements

- Python 3.6 or higher
- Flask
- Install JSON if using lower python version because it might not be include json module, in which case install using `pip install json` 

## Installing
- Clone the repository: https://github.com/Maryamabdulle/receipt-processor-coding-challenge.git

Create a virtual environment and activate it:
- `virtualenv env`
- `source env/bin/activate`

- Install the required package: `pip install -r requirements.txt`

- The code uses a JSON file called receipts.json to store the receipts. If this file is not found in the same directory as the code, the code will create an empty JSON file with that name.

## Running the code

- To run the code, use the following command: `python3 server.py`

- To run the model.py, use the following command: `python3 model.py`

- To run the database.py, use the following command: `python3 database.py`

The code will start a local server on port 5000.


## Server.py defines several routes, each of which maps to a specific function

- /receipts (POST): This route allows to add a new receipt to the database. When a client makes a POST request to this route with a JSON body, the function add_receipt() is executed. This function extracts the 'points' from the JSON body and creates a new receipt object that includes an 'id' field (which is the next id in the database) and the 'points' field. The new receipt is then added to the database and written to the 'receipts.json' file.

- /receipts (GET): This route allows to retrieve all receipts from the database. When a client makes a GET request to this route, the function get_all_receipts() is executed. This function returns all the receipts in the JSON format.

- /receipts/<receipt_id> (GET): This route allows to retrieve a single receipt by its id from the database. When a client makes a GET request to this route, the function get_receipt(receipt_id) is executed. This function takes the receipt_id from the route and matches it to the id field of receipts. It returns the matched receipt in the JSON format.

- /receipts/process (POST): This route allows to process a receipt by inserting it into the JSON file and calculating the points awarded. When a client makes a POST request to this route with a JSON body, the function process_receipt() is executed. This function extracts the receipt data from the JSON body and validates it. If valid, it then calculates the points awarded for the receipt using different logic. It then inserts the receipt into the JSON file and returns the point awarded.

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
- Make sure server is running before testing the endpoints 

For example, you can use the following command to send a POST request to the /receipts endpoint:
- `import flask`
- `import requests`
- `import json`
- `response = requests.post("http://127.0.0.1:5000/receipts",json=data)`
- `print(response)`

- If successful, this will be the outcome: Response [201]
- If successful, this will be the outcome: {'receipt': {'id': 4, 'points': 20}, 'status': 'success'}

- It will return a JSON object containing all the receipts data. You can also test the other endpoints in a similar way.

To make a Get requests to the /receipts endpoints:
- `import flask`
- `import requests`
- `import json`
- `response = requests.get("http://127.0.0.1:5000/receipts")`
- `print(response)`
- If successful, this will be the outcome: Response [200]
- `print(response.json())`
- If successful, this will be the outcome: 
`print(response.json())`
- [{'id': 0, 'items': [{'name': 'item1', 'price': 10.0}, {'name': 'item2', 'price': 20.0}], 'points': 99, 'purchase_date': '2022-01-01', 'purchase_time': '12:00:00', 'retailer': 'Walmart', 'total': 30.0}, {'id': 2, 'points': 0}]

For example, you can use the following command to send a POST request to the /receipts/process endpoint:
- `import flask`
- `import requests`
- `import json`
- `response = requests.post("http://127.0.0.1:5000/receipts/process", json={"retailer": "Walmart","purchase_date": "2022-01-01", "purchase_time": "12:00:00","items":[{"name": "item1","price": 10.0},{"name": "item2","price": 20.0}],"total": 30.0,"points":0})`
- `print(response)`
- It should return a Response [200] if successful, but if there's an error it will return Response [500].
- `print(response.json())`
- If successful, this will be the outcome: 
- {'points': 99, 'status': 'success'}

To make a Get requests to the /receipts/<receipt_id>/points endpoint:
- `import flask`
- `import requests`
- `import json`
- `response = requests.get("http://127.0.0.1:5000/receipts/0/points")` make sure to change the receipt_id to match an existing receipt's ID
- `print(response)`
If successful, this will be the outcome: Response [200]
- `print(response.json())`
- If successful, this will be the outcome: {'points': 99}

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