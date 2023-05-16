from flask import Flask, jsonify
from pymongo import MongoClient

app = Flask(__name__)

@app.route('/')
def welcome():
    # Use the concatenated certificate and key file in the MongoClient connection
    client = MongoClient('mongodb', 27017, 
                            tls=True, 
                            tlsCertificateKeyFile='tls.pem', 
                            tlsCAFile='ca.pem')
    db = client['demo']
    collection = db['names']
    name = collection.find_one()['name']
    client.close()
    rc = '\n'
    return f"Welcome to a cloud native hybrid application, {name}! {rc}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
