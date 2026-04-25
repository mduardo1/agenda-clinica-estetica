from datetime import date, datetime

from app.database.db import db


class Client(db.Model):
    __tablename__ = "clients"

    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(160), nullable=False)
    birth_date = db.Column(db.Date, nullable=True)
    whatsapp = db.Column(db.String(30), nullable=False)
    anamnesis_notes = db.Column(db.Text, nullable=True)
    restrictions = db.Column(db.Text, nullable=True)
    created_at = db.Column(db.Date, default=date.today, nullable=False)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    anamnesis_records = db.relationship(
        "Anamnesis",
        back_populates="client",
        cascade="all, delete-orphan",
    )
    appointments = db.relationship("Appointment", back_populates="client")
