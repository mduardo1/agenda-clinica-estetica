from datetime import datetime

from app.database.db import db


class Appointment(db.Model):
    __tablename__ = "appointments"

    id = db.Column(db.Integer, primary_key=True)
    client_id = db.Column(db.Integer, db.ForeignKey("clients.id"), nullable=False)
    procedure_id = db.Column(db.Integer, db.ForeignKey("procedures.id"), nullable=False)
    appointment_date = db.Column(db.Date, nullable=False)
    start_time = db.Column(db.String(5), nullable=False)
    duration_minutes = db.Column(db.Integer, nullable=False)
    reminder_sent = db.Column(db.Boolean, default=False, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)

    client = db.relationship("Client", back_populates="appointments")
    procedure = db.relationship("Procedure", back_populates="appointments")
