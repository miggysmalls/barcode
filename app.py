import time
import json
import random
import requests
from faker import Faker
from flask import Flask, jsonify

app = Flask(__name__)
flask_response_headers = {'Content-Type': 'application/json'}
fake = Faker()


@app.route('/')
@app.route('/health_check', methods=['GET'])
def default_page():
    message = {
        'status': 'Flask up!'
    }
    # return app.make_response((dumps(message), codes.ok, flask_response_headers))
    return jsonify(message)

@app.route('/about', methods=['GET'])
def default_page():
    message = {
        'status': 'Flask up!'
    }
    return app.make_response((dumps(message), codes.ok, flask_response_headers))
    # return app.make_response((json.dumps(message), requests.codes.ok, flask_response_headers))
    return jsonify(message)


@app.route('/mock/scan_response', methods=['GET'])
def mock_scan():
    response = mock_product()
    # return app.make_response((json.dumps(response), requests.codes.ok, flask_response_headers))
    return jsonify(response)


@app.route('/retailers', methods=['GET'])
def get_retailers():
    return jsonify(retailers)


def mock_product():
    return {
        'product_id': time.time_ns(),
        'product_name': fake.company(),
        'product_price': random.randrange(1, 1000),
        'product_description': 'Product description.',
        'on_sale': False,
        'retailer_id': random.randint(1, 5),
    }


retailers = [
    {
        'retailer_id': 1,
        'retailer_name': 'adidas',
        'retailer_description': ''
    },
    {
        'retailer_id': 2,
        'retailer_name': 'nike',
        'retailer_description': ''
    },
    {
        'retailer_id': 3,
        'retailer_name': 'sketchers',
        'retailer_description': ''
    },
    {
        'retailer_id': 4,
        'retailer_name': 'merrell',
        'retailer_description': ''
    },
    {
        'retailer_id': 5,
        'retailer_name': 'puma',
        'retailer_description': ''
    }
]


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
