import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv 

# Cargar las variables de entorno
load_dotenv()

app = Flask(__name__)

# Ruta raíz
@app.route('/')
def index():
    return 'Hola Mundo'

if __name__ == '__main__':
    app.run(debug=True)
