from calendar import monthrange
from datetime import date

from app.models.appointment import Appointment
from app.repositories.base_repository import BaseRepository


class AppointmentRepository(BaseRepository):
    model = Appointment

    @classmethod
    def by_month(cls, year, month):
        first_day = date(year, month, 1)
        last_day = date(year, month, monthrange(year, month)[1])
        return (
            cls.model.query.filter(
                cls.model.appointment_date >= first_day,
                cls.model.appointment_date <= last_day,
            )
            .order_by(cls.model.appointment_date.asc(), cls.model.start_time.asc())
            .all()
        )

    @classmethod
    def by_date(cls, appointment_date):
        return (
            cls.model.query.filter_by(appointment_date=appointment_date)
            .order_by(cls.model.start_time.asc())
            .all()
        )
