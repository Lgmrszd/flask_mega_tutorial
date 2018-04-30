from flask import Flask
__version__ = "0.1"


app = Flask(__name__)
app.config.from_object('app.config')

from app import routes
