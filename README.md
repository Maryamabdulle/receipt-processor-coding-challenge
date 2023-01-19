# Receipt Processor Coding Challenge

This is a receipt processing web service build using Python 3 and Javascript. The service has two endpoints.

- `POST / receipt/process`: This endpoint is use to submit a receipt for processing. The receipt should be sent in the request body in JSON format and should confom to the "Receipt" shema specified in the API documentation. The response will be a JSON object containing the ID assigned to the receipt. 

- `GET /receipts/{id}/points`: This endpoint is used to retrieve the points awarded for a receipt. The ID of the receipt should be passed as a path parameter. The response will be a JSON object containing the number of points awarded for the receipt. 

## Installation

1. Clone the repository
2. Install the dependencies by running `npm install`
3. Start the server by running `npm start`


## Usage

Make a POST request to `http://localhost:5000/receipt/process` with the receipt data in the request body in JSON format. The response will be a JSON object containing the ID assigned to the receipt. 


Make a GET request to 
