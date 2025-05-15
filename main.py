import os

from flask import Flask, send_file, make_response

app = Flask(__name__)

@app.route("/", methods=['GET'])
def index():
    with open('index.html', 'r') as f:
        return make_response(f.read(), 200, {'Content-type': 'text/html'})

@app.route("/contact.html", methods=['GET'])
def contact():
    with open('contact.html', 'r') as f:
        return make_response(f.read(), 200, {'Content-type': 'text/html'})

@app.route("/products.html", methods=['GET'])
def products():
    with open('products.html', 'r') as f:
        return make_response(f.read(), 200, {'Content-type': 'text/html'})

@app.route("/category.html", methods=['GET'])
def category():
    with open('category.html', 'r') as f:
        return make_response(f.read(), 200, {'Content-type': 'text/html'})

@app.route("/orders", methods=['GET'])
def orders():
    with open('category.html', 'r') as f:
        return make_response(f.read(), 200, {'Content-type': 'text/html'})

def main():
    app.run(port=int(os.environ.get('PORT', 80)))

if __name__ == "__main__":
    main()
