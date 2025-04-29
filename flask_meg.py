#try_flask

from flask import Flask
import json
from datetime import datetime
from flask_cors import CORS

app = Flask(__name__)
app.config["JSON_AS_ASCII"]=False
CORS(app)

@app.route('/')
def index():
    return "Hello World!"

@app.route('/sutit/<zina>')
def sutit(zina):
    

    print(zina)

    #Mainīgais, kas satur ziņas informāciju
    rinda = {
        "zina":zina
    }

    #Datu nolasīšana no chat.json faila
    with open ("chat.json","r",encoding='utf-8') as f:
        vecasZinas = f.read()
        vecieJson = json.loads(vecasZinas)

    #Jauno datu pievienošana iegūtajiem datiem no json faila    
    vecieJson.append(rinda)

    #Datu pievienošana chat.json failā
    with open ("chat.json","w",encoding='utf-8') as f:
        f.write(json.dumps(vecieJson,indent=2,ensure_ascii=False))

    return 'Ok'
app.run()
# app.run(host='0.0.0.0', port=81)