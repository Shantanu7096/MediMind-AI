from models import db


class Medicine(db.Model):

    __tablename__ = "medicines"

    id = db.Column(db.Integer, primary_key=True)

    user_id = db.Column(
        db.Integer,
        db.ForeignKey("users.id"),
        nullable=False
    )

    medicine_name = db.Column(
        db.String(100),
        nullable=False
    )

    dosage = db.Column(
        db.String(50),
        nullable=False
    )

    medicine_type = db.Column(
        db.String(50)
    )

    frequency = db.Column(
        db.String(50)
    )

    food_instruction = db.Column(
        db.String(30)
    )

    reminder_time = db.Column(
        db.Time
    )

    start_date = db.Column(
        db.Date
    )

    end_date = db.Column(
        db.Date
    )

    notes = db.Column(
        db.Text
    )

    status = db.Column(
        db.String(20),
        default="Pending"
    )

    created_at = db.Column(
        db.DateTime,
        server_default=db.func.now()
    )