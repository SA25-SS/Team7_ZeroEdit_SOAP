# from flask import Flask, request, jsonify
# import requests

# from app import app

# SOAP_URL = "http://15.207.110.230/soap/auth"  # Your SOAP API endpoint
# SOAP_HEADERS = {'Content-Type': 'text/xml;charset=UTF-8'}

# def create_soap_request(name, username, password, age, email, city, state, country):
#     """Generate a SOAP XML request."""
#     return f"""
#     <soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/"
#                       xmlns:spy="codeshare.app.auth">
#        <soapenv:Header/>
#        <soapenv:Body>
#           <spy:register_user>
#              <spy:name>{name}</spy:name>
#              <spy:username>{username}</spy:username>
#              <spy:password>{password}</spy:password>
#              <spy:age>{age}</spy:age>
#              <spy:email>{email}</spy:email>
#              <spy:city>{city}</spy:city>
#              <spy:state>{state}</spy:state>
#              <spy:country>{country}</spy:country>
#           </spy:register_user>
#        </soapenv:Body>
#     </soapenv:Envelope>
#     """

# def create_login_soap_request(username, password):
#     """Generate a SOAP XML request for login."""
#     return f"""<?xml version="1.0" encoding="UTF-8"?>
#     <soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:tns="codeshare.app.auth">
#        <soapenv:Header/>
#        <soapenv:Body>
#           <tns:login_user>
#              <tns:username>{username}</tns:username>
#              <tns:password>{password}</tns:password>
#           </tns:login_user>
#        </soapenv:Body>
#     </soapenv:Envelope>
#     """

# def create_verify_token_soap_request(token):
#     """Generate a SOAP XML request for token verification."""
#     return f"""<?xml version="1.0" encoding="UTF-8"?>
#     <soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/"
#                       xmlns:auth="codeshare.app.auth">
#        <soapenv:Header/>
#        <soapenv:Body>
#           <auth:verify_token>
#              <auth:token>{token}</auth:token>
#           </auth:verify_token>
#        </soapenv:Body>
#     </soapenv:Envelope>
#     """

# @app.route('/register', methods=['POST'])
# def register_user():
#     """REST endpoint to register a user."""
#     try:
#         # Parse JSON input from the client
#         data = request.json
#         name = data.get('name')
#         username = data.get('username')
#         password = data.get('password')
#         age = data.get('age')
#         email = data.get('email')
#         city = data.get('city')
#         state = data.get('state')
#         country = data.get('country')

#         # Validate input
#         if not all([name, username, password, age, email, city, state, country]):
#             return jsonify({"status": "error", "message": "All fields are required"}), 400

#         # Create SOAP request body
#         soap_body = create_soap_request(name, username, password, age, email, city, state, country)

#         # Call the SOAP API
#         response = requests.post(SOAP_URL, headers=SOAP_HEADERS, data=soap_body)

#         # Handle SOAP response
#         if response.status_code == 200:
#             # Parse response (assuming it's in XML format)
#             # For simplicity here we just return the raw response text
#             return jsonify({"status": "success", "message": "User registered successfully"}), 200
#         else:
#             return jsonify({"status": "error", "message": "SOAP API call failed"}), 500

#     except Exception as e:
#         return jsonify({"status": "error", "message": str(e)}), 500
    


    
# @app.route('/login', methods=['POST'])
# def login():
#     """REST endpoint for user login."""
#     try:
#         # Parse JSON input from the client
#         data = request.json
#         username = data.get('username')
#         password = data.get('password')

#         if not username or not password:
#             return jsonify({"status": "error", "message": "Username and password are required"}), 400

#         # Create SOAP request body
#         soap_body = create_login_soap_request(username, password)

#         # Call the SOAP API
#         response = requests.post(SOAP_URL, headers={'Content-Type': 'text/xml;charset=UTF-8', 'SOAPAction': 'login_user'}, data=soap_body)

#         # Handle SOAP response
#         if response.status_code == 200:
            
#             return jsonify({"status": "success", "message": "Login successful", "token": "token"}), 200
#         else:
#             return jsonify({"status": "error", "message": "SOAP API call failed"}), 500

#     except Exception as e:
#         return jsonify({"status": "error", "message": str(e)}), 500

# @app.route('/verify-token', methods=['POST'])
# def verify_token():
#     """REST endpoint to verify a token."""
#     try:
#         # Parse JSON input from the client
#         data = request.json
#         token = data.get('token')

#         # Validate input
#         if not token:
#             return jsonify({"status": "error", "message": "Token is required"}), 400

#         # Create SOAP request body
#         soap_body = create_verify_token_soap_request(token)

#         # Call the SOAP API
#         response = requests.post(SOAP_URL, headers={**SOAP_HEADERS, 'SOAPAction': 'verify_token'}, data=soap_body)

#         # Handle SOAP response
#         if response.status_code == 200:
#             # Parse response (assuming it's in XML format)
#             # For simplicity, just returning raw response here
#             return jsonify({"status": "success", "message": "Token verified"}), 200
#         else:
#             return jsonify({"status": "error", "message": "SOAP API call failed"}), 500

#     except Exception as e:
#         return jsonify({"status": "error", "message": str(e)}), 500


# if __name__ == '__main__':
#     app.run(debug=True)
