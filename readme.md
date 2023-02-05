# URL Shortener
A web application built using Flask framework in Python that shortens a long URL into a short URL.

## Prerequisites
- Flask
- pymongo

## Running the application
1. Clone the repository `$ git clone https://github.com/<repo-name>.git`

2. Change the working directory to the cloned repository `$ cd <repo-name>`

3. Install the dependencies `$ pip install -r requirements.txt`

5. Make sure you have a MongoDB database running on 0.0.0.0:27017. 
   If you do not have one, you can follow these steps to set it up:
   
    - Download and install MongoDB Community Server from the official website
    - Start the MongoDB server using the command $ mongod

4. Start the Flask development server `$ python app.py`

5. Open a web browser and go to `http://127.0.0.1:3000`

## Application Features
- It takes a long URL as an input and shortens it into a short URL.
- It stores the mapping of short and long URLs in a database (MongoDB).
- It redirects the user from the short URL to the original long URL.

## Database Connection
The application connects to a MongoDB database running on `0.0.0.0:27017`. If the connection fails, the application terminates with an error message.

## URL Shortening Algorithm
The URL shortening algorithm used in the application is SHA-256 hash. It takes the original URL as input and generates a 6-character long hash string which serves as the short URL.

## Templates
The application uses Flask's templating engine to render the HTML pages. There are two templates in the application:
- base.html: The home page of the application
- error.html: The error page displayed when the short URL is not found in the database.

## Directory Structure
```
.
├── app.py
├── templates
│   ├── base.html
│   └── error.html
└── static
    └── style2.css
```