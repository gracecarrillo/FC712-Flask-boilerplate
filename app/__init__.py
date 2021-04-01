import os
from flask import Flask
from flask.config import Config

#####################
# App creation file #
#####################

# creating flask object
app = Flask(__name__)
#app.config.from_object(Config)
SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY

# importing the routes
from app import routes