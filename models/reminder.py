from models import db


class Reminder(db.Model):

    __tablename__ = "reminders"

    id = db.Column(db.Integer, primary_key=True)

    medicine_id = db.Column(
        db.Integer,
        db.ForeignKey("medicines.id"),
        nullable=False
    )

    reminder_time = db.Column(db.Time)

    reminder_date = db.Column(db.Date)

    status = db.Column(
        db.String(20),
        default="Pending"
    )

    created_at = db.Column(
        db.DateTime,
        server_default=db.func.now()
    )

    medicine = db.relationship(
        "Medicine",
        backref="reminders"
    )