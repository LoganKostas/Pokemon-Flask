from flask import Flask
from config import Config
from flask_login import LoginManager


from .auth.routes import auth
from .team.routes import team
from .models import User

app = Flask(__name__)
login = LoginManager()

@login.user_loader
def load_user(user_id):
    return User.query.get(user_id)

app.register_blueprint(auth)
app.register_blueprint(team)

app.config.from_object(Config)

from .models import db
from flask_migrate import Migrate

db.init_app(app)
migrate = Migrate(app, db)
login.init_app(app)


login.login_view = 'auth.login'
from . import routes
from . import models