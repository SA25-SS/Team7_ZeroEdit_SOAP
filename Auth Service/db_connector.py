import pymongo
from secrets import settings
client = pymongo.MongoClient(settings.mongodb_connection_string)

mongod = client[settings.mongodb_database]

user = mongod["User"]
