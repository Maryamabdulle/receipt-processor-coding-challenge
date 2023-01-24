# Receipt Processor Coding Challenge

This is a receipt processing web service build using Python 3, Flask, and SQLAlchemy for the back-end. This project allows users to submit receipts for processing,retrieve the points awarded for a receipt and get all receipts using API endpoints. The API endpoints are build using Python, and communication bewteem the API and the database is handled using SQLAlchemy. 


# Requirements
- Python 3.6 or higher
- pip
- Flask
- SQLAlchemy
- PostgreSQL
- psycopg2


# Installing

1. Clone the repository 
`https://github.com/Maryamabdulle/receipt-processor-coding-challenge.git`


2. Create a virtual environment and activate it

`virtualenv env`
`source env/bin/activate`


3. Install the required packages 
`pip install -r requirements.txt`

4. Create a new database and update the SQLAlchemy connection string in server.py with your own database credentials

`engine = create_engine("postgresql://maryamabdulle:mypassword@localhost:5432/testdb")`


5. Create the necessary tables by running the following command:

`python3 database.py`

6. Run the server
`python3 server.py`

7. Test the endpoints using 

## Usage

# Some of the Project routes:

- GET /receipts: Returns all receipts in the database
- GET /receipts/<receipt_id>: Returns a single receipt with the given ID
- POST /receipts/process: Processes a receipt by inserting it into the database and calculating the points awarded


## Test the endpoints by making requests to the URLs 

- You can use any tool that allows you to make HTTP requests, such as cURL in this case so that user is able to make the various request types (GET, POST, PATCH, DELETE) to the correct endpoint URLs.

# For example, I can use the following command to send a GET request to the /receipts endpoint:
`curl -X GET http://127.0.0.1:5001/receipts`
- It will return a JSON object containing all the receipts data
- You can also test the other endpoints in a similar way.

# For example, I  can use the following command To sent a POST request to the /receipts/process and before that run these interactively on terminal:
`python`
`import flask`
`import requests`
`response = requests.post("http://127.0.0.1:5001/receipts/process",json={"retailer": "Walmart","purchase_date": "2022-01-01","purchase_time": "12:00:00","items":[{"name": "item1","price": 10.0},{"name": "item2","price": 20.0}],"total": 30.0,"points":0})`
`print(response)`

- It should be returning: Response[200] if its successful but if there's error than it will return Response[500]
