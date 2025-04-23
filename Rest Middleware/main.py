from app import app
from compiler_connect import *
from zeep_connect import *

if __name__ == "__main__":
    app.run(debug=True, port=5001)