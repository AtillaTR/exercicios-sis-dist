import requests
from datetime import datetime
import sqlite3
import matplotlib.pyplot as plt
import numpy as np

con = sqlite3.connect('./database/bdcotacoes.db')
cur = con.cursor()

url='https://api.hgbrasil.com/finance?format=json-cors&key=2ff3b0bd'

response = requests.get(url)
now = datetime.now()
dt_string= now.strftime("%Y-%m-%d_%H:%M:%S")

try:
    cur.execute("create table moedas (Dolar float, Euro float, Data text)")
except :
    if(response.status_code==200):
        json=response.json()
        dolar_value=json['results']['currencies']['USD']['buy']
        btc_value=json['results']['currencies']['BTC']['buy']
        euro_value=json['results']['currencies']['EUR']['buy']
        
        cur.execute("insert into moedas (Dolar, Euro, Data) values (?,?,?)", (dolar_value, euro_value, dt_string))
        con.commit()
        con.close()
        print("Data loaded")

    else:
        print("Bad request")