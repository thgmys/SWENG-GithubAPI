import pymongo
import certifi

# clears mongodb database
print("Empty MongoDB Database")
password=input("Enter password for database access:")
client = pymongo.MongoClient(f"mongodb+srv://mark:{password}@sweng.hrxdo.mongodb.net/myFirstDatabase?retryWrites=true&w=majority", tlsCAFile=certifi.where())
db = client.test
db.githubdata.delete_many({})
print("Database Emptied")