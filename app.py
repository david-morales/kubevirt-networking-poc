from flask import Flask, jsonify
from pymongo import MongoClient
import os

app = Flask(__name__)

@app.route('/')
def welcome():

    # Read environment variables
    app_database = os.environ.get('APP_DATABASE')
    replicaset = os.environ.get('REPLICASET')
    mongodb_user = os.environ.get('APP_USER')
    mongodb_password = os.environ.get('APP_USER_PASSWORD')
    tls_enabled = os.environ.get('TLS_ENABLED')


    client= None

    if tls_enabled:

        # Concatenate the certificate and key into a single PEM file at runtime
        pem_file_path = "/tmp/tls.pem"
        with open(pem_file_path, 'w') as pem_file:
            with open('/certificates/tls.crt', 'r') as crt_file:
                pem_file.write(crt_file.read())
            with open('/certificates/tls.key', 'r') as key_file:
                pem_file.write(key_file.read())

        # Use the concatenated certificate and key file in the MongoClient connection
        client = MongoClient(host=['mongodb-0:27017', 'mongodb-1:27017', 'mongodb-2:27017'],
                                replicaset=replicaset,
                                tls=tls_enabled, 
                                tlsCertificateKeyFile=pem_file_path, 
                                tlsCAFile='/certificates/ca.crt',
                                username=mongodb_user,
                                password=mongodb_password,
                                authSource=app_database
                                )
    else:
        # Use the concatenated certificate and key file in the MongoClient connection
        client = MongoClient(host=['mongodb-0:27017', 'mongodb-1:27017', 'mongodb-2:27017'],
                                replicaset=replicaset,
                                username=mongodb_user,
                                password=mongodb_password,
                                authSource=app_database
                                )

    db = client[app_database]
    collection = db['names']
    name = collection.find_one()['name']
    client.close()
    rc = '\n'
    return f"Welcome to a cloud native hybrid application, {name}! {rc}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)