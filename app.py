from flask import Flask

from config import Config

from flask_login import LoginManager

from models import db

from models.user import User

from routes.main import main
from routes.auth import auth
from routes.dashboard import dashboard_bp
from routes.medicine import medicine_bp
from routes.reminder import reminder_bp
from routes.water import water_bp
from routes.sleep import sleep_bp

app = Flask(__name__)

app.config.from_object(Config)

db.init_app(app)

login_manager = LoginManager()

login_manager.login_view = "auth.login"

login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):

    return User.query.get(int(user_id))


app.register_blueprint(main)

app.register_blueprint(auth)

app.register_blueprint(dashboard_bp)

app.register_blueprint(medicine_bp)

app.register_blueprint(reminder_bp)

app.register_blueprint(water_bp)

app.register_blueprint(sleep_bp)

with app.app_context():

    db.create_all()


if __name__ == "__main__":

    app.run(debug=True)