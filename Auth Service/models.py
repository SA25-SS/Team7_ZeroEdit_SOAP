
from spyne import ComplexModel, Unicode

class GeneralResponseModel(ComplexModel):
    __namespace__ = "codeshare.app.auth"
    status = Unicode
    message = Unicode


class LoginResponse(ComplexModel):
    __namespace__ = 'codeshare.app.auth'
    status = Unicode
    message = Unicode
    token = Unicode