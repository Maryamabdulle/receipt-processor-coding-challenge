# Receipt Processor Coding Challenge

This is a receipt processing web service build using Python 3, Flask, and SQLAlchemy for the back-end. This project allows users to submit receipts for processing,retrieve the points awarded for a receipt and get all receipts using API endpoints. The API endpoints are build using Python, and communication bewteem the API and the database is handled using SQLAlchemy. 


# API Endpoints 

- `POST / receipt/process`: This endpoint is use to submit a receipt for processing. The receipt should be sent in the request body in JSON format and should include the retailer name, purchase date and time, a list of items purchase, and the total amount. The response will be a JSON object containing the ID assigned to the receipt. 

- `GET/receipts/` : This endpoint is use to retieve all the receipts

- `GET /receipts/{id}/`: This endpoint is used to retrieve a receipt by ID

- `GET /receipts/{id}/points`: This endpoint is used to retrieve the points awarded for a receipt by ID

- `PATCH /receipts/{id}/`: This endpoint is used to update a receipt by ID

- `DELETE /receipts/{id}/`: This endpoint is used to delete a receipt by ID


## Installation

1. Clone the repository
2. Install the dependencies by running `pip install r-requirements.txt`
3. Create a PostgreSQL database and update the database URl in the database.py file
4. Run the database.py file to create the receipts table


## How to Run

Start the server by running `python 3 server.py`



## Note

This porject is setup to use the PostgreSQL database, and the database connection is established on the line:
e
engine= 
`create_engine("postgresql://maryam:mypassword@localhost:5000/testdb")`

If you would like to use a different database, you will need to update the connection string to match the approriate database type and credentials



## Usage

- To submit a receipt for processing, make a POST request to http://localhost:5000/receipts/process with the receipt data in the request body in JSON format. The response will be a JSON object containing the ID assigned to the receipt and the points awarded for the receipt.

- To retrieve all receipts, make a GET request to http://localhost:5000/receipts/.

- To retrieve a receipt by ID, make a GET request to http://localhost:5000/receipts/<receipt_id>/.

- To retrieve the points awarded for a receipt by ID, make a GET request to http://localhost:5000/receipts/<receipt_id>/points.

- It is also possible to update or delete a receipt by sending a PATCH or DELETE request to http://localhost:5000/receipts/<receipt_id>/ respectively.

## Summary

Flask application that connect to a PostgreSQL database, defines several routes for performing CRUD operation on receipt data, and calculates points based on the receipt data. 




