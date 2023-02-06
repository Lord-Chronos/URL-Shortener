# URL Shortener
A Flask-based web application that shortens URL's. The application uses a MongoDB database to store the original URLs and their corresponding short URLs, and has multiple endpoints for shortening and redirecting URLs. It supports both JSON and HTML requests and has error handling in place.

# Application Features
- URL Shortening
- URL Redirection
- JSON and HTML Request WSupport
- Error Handling

# Technical Info
- Flask
- Python 3 
- Pymongo
- HTML, CSS

# Setup
## Database
The application requires a MongoDB database to store the original and short URLs. 
One way to set this up is by using Docker with the following command:

`$ docker run --name mongo-url -d -p 27017:27017 mongo:latest    `

**Note:** MongoDB 5.0+ requires a CPU with AVX support, if your cpu does not have support use `mongo:4`

## Flask Application
1. Clone the repository: `$ git clone https://github.com/<repo-name>.git`

2. Change the working directory to the cloned repository: `$ cd url-shortner`

3. Install the dependencies: `$ pip install -r requirements.txt`

5. Replace `db_address = "<host>:<port>"` in app.py with the address of your MongoDB database setup.

4. Start the Flask server with `$ python app.py`

5. (Optional) Access the web interface at `http://localhost:3000`


# Use
## Endpoints

- `/` - A GET endpoint that returns the main site page in HTML format.

- `/shorten` - A POST endpoint that accepts a url parameter in the request body and returns a shortened URL in either JSON or HTML format depending on the request type.
    - JSON Example: `$ curl -X POST -H 'Content-Type: application/json' -d '{"url":"https://www.github.com/"}' http://localhost:3000/shorten`

- `/<short_url>` - A GET endpoint that accepts a short URL as a path parameter and redirects the user to the original URL. If the short URL is not found in the database, it returns an error message in either JSON or HTML format.
    - JSON Example: `$ curl -X GET -H 'Content-Type: application/json' http://localhost:3000/23c73f`

**Note:** Currently, the return URL is for localhost even if the server is remote.

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