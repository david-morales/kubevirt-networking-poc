from flask import Flask, jsonify
from pymongo import MongoClient
import os

app = Flask(__name__)

@app.route('/')
def welcome():
    # Concatenate the certificate and key into a single PEM file at runtime
    pem_file_path = "/tmp/tls.pem"
    with open(pem_file_path, 'w') as pem_file:
        with open('/certificates/tls.crt', 'r') as crt_file:
            pem_file.write(crt_file.read())
        with open('/certificates/tls.key', 'r') as key_file:
            pem_file.write(key_file.read())

    # Use the concatenated certificate and key file in the MongoClient connection
    client = MongoClient('mongodb', 27017, 
                            tls=True, 
                            tlsCertificateKeyFile=pem_file_path, 
                            tlsCAFile='/certificates/ca.crt')
    db = client['demo']
    collection = db['names']
    name = collection.find_one()['name']
    client.close()
    rc = '\n'
    return f"Welcome to a cloud native hybrid application, {name}! {rc}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
