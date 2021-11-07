from json import dumps
from flask import Flask
from requests import codes

app = Flask(__name__)
flask_response_headers = {'Content-Type': 'application/json'}


@app.route('/')
@app.route('/health_check', methods=['GET'])
def default_page():
    message = {
        'status': 'Flask up!'
    }
    return app.make_response((dumps(message), codes.ok, flask_response_headers))
