from flask import Flask, request, jsonify
from zeep import Client
from variables import settings
from app import app

# SOAP Service WSDL URL (replace with your actual WSDL URL or endpoint)
SOAP_SERVICE_URL = settings.SOAP_SERVICE_URL

# Create a Zeep SOAP client
soap_client = Client(SOAP_SERVICE_URL)

@app.route("/run-code", methods=["POST"])
def run_code():
    """
    REST endpoint to call the SOAP service for running code.
    Expects JSON input from the frontend.
    """
    try:
        # Get JSON data from the frontend request
        data = request.json
        language = data.get("language")
        stdin = data.get("stdin")
        fname= data.get("fname")
        code = data.get("code")

        if not language or not code:
            return jsonify({"status": "error", "message": "Missing required fields: 'language' or 'code'"}), 400

        # Call the SOAP service using Zeep
        response = soap_client.service.run_code(language, stdin,fname, code)

        # Return the SOAP response to the frontend as JSON
        return jsonify({
            "status": response.status,
            "output": response.output,
            "error": response.error
        })

    except Exception as e:
        return jsonify({"status": "error", "message": f"Failed to call SOAP service: {str(e)}"}), 500


if __name__ == "__main__":
    app.run(debug=True, port=5001)
