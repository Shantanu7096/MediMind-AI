from models import db


class WaterLog(db.Model):

    __tablename__ = "water_logs"

    id = db.Column(db.Integer, primary_key=True)

    user_id = db.Column(
        db.Integer,
        db.ForeignKey("users.id"),
        nullable=False
    )

    glasses = db.Column(
        db.Integer,
        default=0
    )

    goal = db.Column(
        db.Integer,
        default=8
    )

    log_date = db.Column(db.Date)

    created_at = db.Column(
        db.DateTime,
        server_default=db.func.now()
    )