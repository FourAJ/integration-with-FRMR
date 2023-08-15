from flask import Flask
from flask_socketio import SocketIO
import os
from os import environ as env
from dotenv import load_dotenv

dotenv_path = os.path.join(os.path.dirname(__file__), '../../.env')
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)

app = Flask(__name__, template_folder='../templates', static_folder='../static')
app.config['SECRET_KEY'] = env['SECRETKEY']

socketio = SocketIO()
socketio.init_app(app)

JWT_FRMR_API_TOKEN = env['JWT_FRMR_API_TOKEN']
JWT_MODULE_API_TOKEN = env['JWT_MODULE_API_TOKEN']

BaseURLfrmr = env['BASE_URL_FRMR']
MODULE_API_URL = env['MODULE_API_URL']

DATABASE_MODULE_URL = env['DATABASE_MODULE_URL']
