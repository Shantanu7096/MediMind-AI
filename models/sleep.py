from models import db


class SleepLog(db.Model):

    __tablename__ = "sleep_logs"

    id = db.Column(db.Integer, primary_key=True)

    user_id = db.Column(
        db.Integer,
        db.ForeignKey("users.id"),
        nullable=False
    )

    sleep_time = db.Column(db.Time)

    wake_time = db.Column(db.Time)

    total_hours = db.Column(db.Float)

    sleep_quality = db.Column(db.String(20))

    log_date = db.Column(db.Date)

    created_at = db.Column(
        db.DateTime,
        server_default=db.func.now()
    )