from flask import Flask
from flask_restx import Api
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///movies.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JSON_AS_ASCII'] = False
app.config['RESTX_JSON'] = {'ensure_ascii': False, 'indent': 2, 'sort_keys': False}

db = SQLAlchemy(app)

api = Api(app)


movies_ns = api.namespace('movies')
# directors_ns = api.namespace('directors')
# genres_ns = api.namespace('genres')


