# URL Shortener
A web application built using Flask framework in Python that shortens a long URL into a short URL.

# Application Features
- A REST api
- It takes a long URL as an input and shortens it into a short URL.
- It stores the mapping of short and long URLs in a database (MongoDB).
- It redirects the user from the short URL to the original long URL.

# Technical Info
- Python 3, HTML, CSS
- Flask
- Pymongo
- Mongodb


curl -X POST -H 'Content-Type: application/json' \
     -d '{"url":"https://www.reddit.com/"}' \
     http://localhost:3000/shorten

curl -X GET -H 'Content-Type: application/json' http://localhost:3000/14830d      
# Setup
## Database
This application requires a mongodb database setup on an accessible port. 

To install a mongodb in a docker container:

1. 

# Flask Application
1. Clone the repository `$ git clone https://github.com/<repo-name>.git`

2. Change the working directory to the cloned repository `$ cd url-shortner`

3. Install the dependencies `$ pip install -r requirements.txt`

5. Make sure you have a MongoDB database running on 0.0.0.0:27017. 
   If you do not have one, you can follow the steps at ##database

4. Start the Flask development server `$ python app.py`

5. Open a web browser and go to `http://127.0.0.1:3000`



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