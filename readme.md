# URL Shortener
This is a Flask-based web application that shortens URL's. The application uses a MongoDB database to store the URLs and their corresponding short URLs. It has several endpoints for shortening and redirecting URLs that work with either a JSON or HTML request. 

# Application Features
- URL Shortening
- URL Redirection
- Support for Both JSON and HTML Requests
- Error Handling
- Database Connectivity

# Technical Info
- Python 3, HTML, CSS
- Flask
- Pymongo
- Mongodb

# Setup
## Database
The application connects to a MongoDB database running. If the connection fails, the application terminates with an error message.

To setup the MongoDB batabse in docker run:

`docker run --name mongo-url -d -p 27017:27017 mongo:latest    `


## Flask Application
1. Clone the repository `$ git clone https://github.com/<repo-name>.git`

2. Change the working directory to the cloned repository `$ cd url-shortner`

3. Install the dependencies `$ pip install -r requirements.txt`

5. Replace `db_address = "<host>:<port>"` with the address of your MongoDB database you set up earlier

4. Start the Flask server with `python app.py`

5. (optional) To use the web interface go to `http://127.0.0.1:3000`

# Use
## Endpoints

- `/` - GET endpoint that returns the main site page in HTML format.

- `/shorten` - POST endpoint that accepts a url parameter in the request body and returns a shortened URL in either JSON or HTML format depending on the type of request.
    - JSON Example `curl -X POST -H 'Content-Type: application/json' -d '{"url":"https://www.reddit.com/"}' http://localhost:3000/shorten`

- `/<short_url>` - GET endpoint that accepts a short URL as a path parameter and redirects the user to the original URL or returns an error message in JSON or HTML format if the short URL is not found in the database.
    - JSON Example `curl -X GET -H 'Content-Type: application/json' http://localhost:3000/14830d`

# Directory Structure
```
.
├── app.py
├── templates
│   ├── base.html
│   └── error.html
└── static
    └── style.css
```