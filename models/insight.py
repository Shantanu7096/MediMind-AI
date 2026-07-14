from models import db


class Insight(db.Model):

    __tablename__ = "insights"

    id = db.Column(db.Integer, primary_key=True)

    user_id = db.Column(
        db.Integer,
        db.ForeignKey("users.id"),
        nullable=False
    )

    title = db.Column(
        db.String(150),
        nullable=False
    )

    message = db.Column(
        db.Text,
        nullable=False
    )

    health_score = db.Column(
        db.Integer,
        default=0
    )

    insight_type = db.Column(
        db.String(50),
        default="Daily"
    )

    created_at = db.Column(
        db.DateTime,
        server_default=db.func.now()
    )

    def __repr__(self):
        return f"<Insight {self.id}>"