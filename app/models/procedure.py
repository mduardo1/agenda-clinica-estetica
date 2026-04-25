from datetime import datetime

from app.database.db import db


class Procedure(db.Model):
    __tablename__ = "procedures"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    description = db.Column(db.Text, nullable=True)
    cost = db.Column(db.Numeric(10, 2), nullable=False, default=0)
    price = db.Column(db.Numeric(10, 2), nullable=False, default=0)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)

    appointments = db.relationship("Appointment", back_populates="procedure")

    @property
    def profit(self):
        return self.price - self.cost
