from flask import Flask, redirect, request, render_template
import hashlib
import pymongo
import sys

# Initialize the Flask application
app = Flask(__name__)

db_address = "0.0.0.0:27017"

# Connect to the MongoDB database
client = pymongo.MongoClient("mongodb://" + db_address + "/")
db = client["url-shortener"]
urls = db["urls"]
print(urls)


def database_check():
    try:
        client.server_info()

    except pymongo.errors.ServerSelectionTimeoutError as e: 
        print("Databse connection failed with error: ", str(e))
        print("Ensure you have mongodb databse running on 0.0.0.0:27017")
        print("Quitting the application")
        sys.exit(1)
    return (urls)

database_check()

@app.route('/shorten', methods=['POST'])
def shorten():
    original_url = request.form['url']
    
    # Generate a hash of the original URL using SHA-256, truncated to 6 characters
    hash = hashlib.sha256(original_url.encode('utf-8')).hexdigest()[:6]
    url_data = {
        "short_url": hash,
        "original_url": original_url
    }

    urls.insert_one(url_data)
    short_url =  'http://localhost:3000/' + hash
    return render_template('base.html', short_url=short_url)

@app.route('/<short_url>')
def redirect_url(short_url):
    url = urls.find_one({"short_url": short_url})
    if not url:
        return render_template('error.html')
    original_url = url["original_url"]
    return redirect(original_url)

@app.route('/')
def index():
    return render_template('base.html')
    
@app.route('/style2.css')
def css():
    return app.send_from_directory('static', 'style2.css')

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=3000)
