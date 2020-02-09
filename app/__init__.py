from app.config import Config
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

app = Flask(__name__)
app.secret_key = '4sU'
app.config.from_object(Config)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

login = LoginManager(app)
login.login_view = '/admin/auth/login'

from .views.admin.auth import auth
from .views.admin.debtor import debtor

app.register_blueprint(auth)
app.register_blueprint(debtor)

from app import routes, models
