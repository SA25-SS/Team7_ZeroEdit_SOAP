from spyne import Application, rpc, ServiceBase, Unicode, Integer, ComplexModel
from spyne.model.primitive import String
from spyne.server.wsgi import WsgiApplication
from spyne.protocol.soap import Soap11
import requests
from secrets import settings

from werkzeug.middleware.dispatcher import DispatcherMiddleware

# Define response model for the SOAP service
class CompilerResponseModel(ComplexModel):
    status = Unicode
    output = Unicode
    error = Unicode

# Define the SOAP service class
class CompilerService(ServiceBase):
    @rpc(Unicode, Unicode, Unicode, Unicode, _returns=CompilerResponseModel)
    def run_code(ctx, language, stdin, fname, code):
        """
        SOAP operation to execute code using OneCompiler API.
        :param language: Programming language (e.g., 'python').
        :param stdin: Input to be provided to the program.
        :param code: Source code to execute.
        :return: CompilerResponseModel containing status, output, and error.
        """
        # OneCompiler API details
        ONECOMPILER_API_URL = settings.oc_api_url
        ONECOMPILER_API_HOST = settings.oc_api_host
        ONECOMPILER_API_KEY = settings.oc_api_key

        # Prepare payload for OneCompiler API
        payload = {
            "language": language,
            "stdin": stdin,
            "files": [{"name": fname, "content": code}],
        }

        # Headers for OneCompiler API
        headers = {
            "Content-Type": "application/json",
            "x-rapidapi-host": ONECOMPILER_API_HOST,
            "x-rapidapi-key": ONECOMPILER_API_KEY,
        }

        try:
            # Call OneCompiler API
            response = requests.post(ONECOMPILER_API_URL, json=payload, headers=headers)
            response_data = response.json()

            # Prepare response model
            status = response_data.get("status", "error")
            output = response_data.get("stdout", "")
            error = response_data.get("stderr", "")

        except Exception as e:
            status = "error"
            output = ""
            error = f"Failed to call OneCompiler API: {str(e)}"

        return CompilerResponseModel(status=status, output=output, error=error)


# Create SOAP application
application = Application(
    [CompilerService],
    tns="spyne.examples.compiler",
    in_protocol=Soap11(),
    out_protocol=Soap11(),
)

# Wrap application in WSGI container
wsgi_application = WsgiApplication(application)

application = DispatcherMiddleware(None, {
    '/soap/compiler': wsgi_application
})
if __name__ == "__main__":
    from wsgiref.simple_server import make_server

    print("Starting SOAP server on http://localhost:7000...")
    server = make_server("0.0.0.0", 7000, wsgi_application)
    server.serve_forever()
