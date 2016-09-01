from flask import Flask
from amir import amirblue
from amir2 import amirblue2

app = Flask(__name__)
app.config['SECRET_KEY']='test'
app.register_blueprint(amirblue)
app.register_blueprint(amirblue2)
from app import views