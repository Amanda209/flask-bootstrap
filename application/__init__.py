from flask import Flask

app = Flask(__name__)

# Routes definition
import application.routes.index
