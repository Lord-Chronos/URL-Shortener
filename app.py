from flask import Flask, redirect, request, render_template, jsonify
import hashlib
import pymongo
import sys

app = Flask(__name__)

# Replace with your mongodb address
db_address = "0.0.0.0:27017"

# Connect to the MongoDB database
client = pymongo.MongoClient("mongodb://" + db_address + "/")
db = client["url-shortener"]
urls = db["urls"]

# Checks Database is Connected
try:
    client.server_info()

except pymongo.errors.ServerSelectionTimeoutError as e:
    print("Databse connection failed with error: ", str(e))
    print("Ensure you have mongodb databse running on" + db_address)
    print("Quitting the application")
    sys.exit(1)


# POST route for shortening the URL
@app.route('/shorten', methods=['POST'])
def shorten():
    content_type = request.headers.get('Content-Type')
    
    # original_url = request.form['url']
    if content_type == 'application/json':
        data = request.get_json()
        original_url = data['url']
    else:
        original_url = request.form['url']

    # Generate a hash of the original URL using SHA-256, truncated to 6 characters
    hash = hashlib.sha256(original_url.encode('utf-8')).hexdigest()[:6]
    url_data = {
        "short_url": hash,
        "original_url": original_url
    }

    urls.insert_one(url_data)
    short_url_return = 'http://localhost:3000/' + hash

    # Returns json or html depending on request type
    if content_type == 'application/json':
        return jsonify({'short_url_return': short_url}), 200
    else:
        return render_template('base.html', short_url=short_url_return)

# GET route for retrieving original URL
@app.route('/<short_url>')
def redirect_url(short_url):
    content_type = request.headers.get('Content-Type')

    url = urls.find_one({"short_url": short_url})

    # Returns error json or html if url not in database
    if not url:
        if content_type == 'application/json':
            return jsonify({"error": "URL not found"}), 404
        else:
            return render_template('error.html')

    # Returns succeess json or html with original url from database
    original_url = url["original_url"]

    if content_type == 'application/json':
        return jsonify({'original_url': original_url}), 200
    else:
        return redirect(original_url)

# Route for main site page
@app.route('/')
def index():
    return render_template('base.html')

# Route to serve css
@app.route('/style2.css')
def css():
    return app.send_from_directory('static', 'style2.css')


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=3000)
