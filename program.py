from flask import *
from BlockChain import Block , DataBase
import RSA


app = Flask("__app__")

@app.route("/")
def MainPage():

    return """hello"""

@app.route("/transaction")
def transaction():

    
    
    return f""" {request.args.get("get")}"""

@app.route("/login")
def login():

    pass

@app.route("/create")
def createAccount():

    (privat,public) = RSA.Generate_key()

    
    DataBase.AddAccunt(privat , publicKey=public)

    return str(public) + "#" + str(privat)

app.run()