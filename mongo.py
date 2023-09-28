from pymongo.mongo_client import MongoClient

#import os
#from dotenv import load_dotenv

#load_dotenv()


class MongoConnection:
    def __init__(self):
        #URL conexion de mongoDB local
        uri = "mongodb://localhost:27017"

        # Create a new client and connect to the server
        self.client = MongoClient(uri)

    def test_connection(self):
        # Send a ping to confirm a successful connection
        try:
            self.client.admin.command('ping')
            print("Pinged your deployment. You successfully connected to MongoDB!")
        except Exception as e:
            print(e)


if __name__ == "__main__":
    MongoConnection().test_connection()
