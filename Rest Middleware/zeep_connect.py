from flask import Flask, request, jsonify
from zeep import Client
from zeep.transports import Transport
from requests import Session
from variables import settings
from app import app


# SOAP WSDL URL
SOAP_WSDL_URL = settings.SOAP_AUTH_URL

# Initialize the zeep client
session = Session()          
session.headers.update({'Content-Type': 'text/xml;charset=UTF-8'})
transport = Transport(session=session)
client = Client(wsdl=SOAP_WSDL_URL, transport=transport)


@app.route('/register', methods=['POST'])
def register_user():
    """REST endpoint to register a user."""
    try:

        session.headers.update({
            'Content-Type': 'text/xml;charset-UTF-8'
        })
        # Parse JSON input from the client
        data = request.json
        name = data.get('name')
        username = data.get('username')
        password = data.get('password')
        age = data.get('age')
        email = data.get('email')

        # Validate input
        if not all([name, username, password, age, email]):
            return jsonify({"status": "error", "message": "All fields are required"}), 400

        # Call the SOAP API using zeep with custom headers
        response = client.service.register_user(
            name=name,
            username=username,
            password=password,
            age=age,
            email=email,
        )

        # Handle SOAP response
        return jsonify({"status": response.status, "message": response.message}), 200

    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500


@app.route('/login', methods=['POST'])
def login():
    """REST endpoint for user login."""
    try:

        session.headers.update({
            'Content-Type': 'text/xml;charset-UTF-8',
            'SOAPAction': 'login_user'
        })
        # Parse JSON input from the client
        data = request.json
        username = data.get('username')
        password = data.get('password')

        if not username or not password:
            return jsonify({"status": "error", "message": "Username and password are required"}), 400

        # Call the SOAP API using zeep with custom headers
        response = client.service.login_user(
            username=username,
            password=password,
        )

        # Handle SOAP response
        return jsonify({
            "status": response.status,
            "message": response.message,
            "token": response.token
        }), 200

    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500


@app.route('/verify-token', methods=['POST'])
def verify_token():
    """REST endpoint to verify a token."""
    try:

        session.headers.update({
            'Content-Type': 'text/xml;charset-UTF-8',
            'SOAPAction': 'verify_token'
        })
        # Parse JSON input from the client
        data = request.json
        token = data.get('token')

        # Validate input
        if not token:
            return jsonify({"status": "error", "message": "Token is required"}), 400


        # Call the SOAP API using zeep with custom headers
        response = client.service.verify_token(
            token=token,
        )

        # Handle SOAP response
        return jsonify({
            "status": response.status,
            "message": response.message
        }), 200

    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
