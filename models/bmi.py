from models import db


class BMI(db.Model):

    __tablename__ = "bmi_logs"

    id = db.Column(db.Integer, primary_key=True)

    user_id = db.Column(
        db.Integer,
        db.ForeignKey("users.id"),
        nullable=False
    )

    height = db.Column(db.Float)

    weight = db.Column(db.Float)

    bmi = db.Column(db.Float)

    category = db.Column(db.String(50))

    log_date = db.Column(db.Date)

    created_at = db.Column(
        db.DateTime,
        server_default=db.func.now()
    )