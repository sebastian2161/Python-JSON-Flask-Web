import json
from flask import *
from functools import wraps
import requests


app = Flask(__name__)
app.secret_key = 'mysecretkey'
app.config.from_object(__name__)


@app.route('/')
def index():
     with open('paises_capitales.json') as f:

             paises = json.load(f)

             valores = []
             for x in paises :
                 valores.append(list(x.values()))

             return render_template('consultar.html', valores=valores)


if __name__ == '__main__':
    app.run(port = 3000, debug=True)


    