import datetime
from bson import ObjectId
from pymongo import MongoClient
from sqlalchemy import create_engine, Table, Column, MetaData, String
from sqlalchemy.orm import sessionmaker

# REPLACE WITH YOUR INFO.
config = {
    "mysql": {
        "host": "localhost",
        "user": "root",
        "password": "snoopy1230465",
        "database": "trial308"
    },
    "mongodb": {
        "host": "localhost",
        "port": 27017,
        "database": "Flight Database"
    }
}


def connectDB():
    connection_string = "mongodb+srv://asfafeeroze:1234@cluster0.zj78qtj.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
    client = MongoClient(connection_string)
    db = client.Cluster0
    print("Connection established to your db")
    return db


def connect_mysql():
    mysql_config = config['mysql']
    engine = create_engine(
        f'mysql+mysqlconnector://{mysql_config["user"]}:{mysql_config["password"]}@{mysql_config["host"]}/{mysql_config["database"]}')
    Session = sessionmaker(bind=engine)
    if Session:
        print("Connection established to MySQL")
    return engine, Session()
