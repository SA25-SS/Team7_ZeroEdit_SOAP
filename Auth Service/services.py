from importers import *
from db_connector import *
from utils import json_to_xml, sha256_hash
from models import *

# class HelloWorldService(ServiceBase):
#     @rpc(Unicode, Integer, _returns=Iterable(Unicode))
#     def say_hello(ctx, name, times):
#         for i in range(times):
#             yield 'Hello, %s' % name



class RegisterUserService(ServiceBase):
    @rpc(Unicode, Unicode,Unicode,Integer,Unicode,_returns=GeneralResponseModel)
    def register_user(ctx,name,username,password,age,email):
        if user.find_one({"$or": [{"username": username}, {"email": email}]}):
            status = "error"
            message = "Username or email already exists."
        else:
            user_data = {
                "name": name,
                "username": username,
                "password": sha256_hash(password),
                "age": age,
                "email": email
            }
            try:
                user.insert_one(user_data)
                status = "success"
                message = "User registered successfully."
            except Exception as e:
                status = "error"
                message = f"Registration failed: {str(e)}"


        return GeneralResponseModel(status=status, message=message)

class LoginUserService(ServiceBase):

    @rpc(Unicode, Unicode, _returns=LoginResponse)
    def login_user(ctx, username, password):
        users = user.find_one({"username": username, "password": password})

        if users:
            payload = {
                "sub": username,
                "exp": datetime.utcnow() + timedelta(hours=1)
            }
            token = jwt.encode(payload, settings.secret_key, algorithm="HS256")
            return LoginResponse(status="success", message="Login successful", token=token)
        else:
            return LoginResponse(status="error", message="Invalid username or password", token=None)

class VerifyTokenService(ServiceBase):
    @rpc(Unicode, _returns=GeneralResponseModel)
    def verify_token(ctx, token):
        try:
            decoded_token = jwt.decode(token, settings.secret_key, algorithms=["HS256"])
        except Exception as e:
            return GeneralResponseModel(status="error", message=f"Invalid token")

        users = user.find_one({"username": decoded_token["sub"]})
        if not users:
            return GeneralResponseModel(status="error", message="Invalid token")
        else:
            return GeneralResponseModel(status="success", message="Token verified")

