from flask_login import UserMixin
from models import db


class User(UserMixin, db.Model):

    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)

    fullname = db.Column(db.String(100), nullable=False)

    email = db.Column(db.String(120), unique=True, nullable=False)

    password = db.Column(db.String(255), nullable=False)

    phone = db.Column(db.String(15))

    age = db.Column(db.Integer)

    gender = db.Column(db.String(20))

    blood_group = db.Column(db.String(5))

    height = db.Column(db.Float)

    weight = db.Column(db.Float)

    allergies = db.Column(db.Text)

    chronic_diseases = db.Column(db.Text)

    emergency_contact = db.Column(db.String(15))

    profile_image = db.Column(
        db.String(255),
        default="default.png"
    )

    is_admin = db.Column(
        db.Boolean,
        default=False
    )

    created_at = db.Column(
        db.DateTime,
        server_default=db.func.now()
    )

    updated_at = db.Column(
        db.DateTime,
        server_default=db.func.now(),
        onupdate=db.func.now()
    )

    def get_id(self):
        return str(self.id)