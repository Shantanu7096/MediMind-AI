from models import db


class MedicineInfo(db.Model):

    __tablename__ = "medicine_info"

    id = db.Column(db.Integer, primary_key=True)

    medicine_name = db.Column(db.String(255), unique=True)

    generic_name = db.Column(db.String(255))

    manufacturer = db.Column(db.String(255))

    uses = db.Column(db.Text)

    side_effects = db.Column(db.Text)

    precautions = db.Column(db.Text)

    food_interactions = db.Column(db.Text)

    storage = db.Column(db.Text)

    dosage_information = db.Column(db.Text)

    ai_summary = db.Column(db.Text)

    last_updated = db.Column(
        db.DateTime,
        server_default=db.func.now()
    )