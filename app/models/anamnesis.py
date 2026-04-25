from datetime import datetime

from app.database.db import db


class Anamnesis(db.Model):
    __tablename__ = "anamnesis_records"

    id = db.Column(db.Integer, primary_key=True)
    client_id = db.Column(db.Integer, db.ForeignKey("clients.id"), nullable=False)
    notes = db.Column(db.Text, nullable=True)
    restrictions = db.Column(db.Text, nullable=True)
    care_instructions = db.Column(db.Text, nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)

    client = db.relationship("Client", back_populates="anamnesis_records")
