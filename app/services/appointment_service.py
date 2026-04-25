from datetime import datetime, timedelta

from app.models.appointment import Appointment
from app.repositories.appointment_repository import AppointmentRepository


class AppointmentService:
    @staticmethod
    def list_by_month(year, month):
        return AppointmentRepository.by_month(year, month)

    @staticmethod
    def list_by_date(appointment_date):
        return AppointmentRepository.by_date(appointment_date)

    @staticmethod
    def create(data):
        appointment_date = datetime.strptime(data["appointment_date"], "%Y-%m-%d").date()
        start_time = AppointmentService.to_24h_time(
            data["hour"],
            data["minute"],
            data["period"],
        )
        duration = int(data["duration_minutes"])

        if AppointmentService.has_conflict(appointment_date, start_time, duration):
            raise ValueError("Ja existe um agendamento conflitante neste horario.")

        appointment = Appointment(
            client_id=int(data["client_id"]),
            procedure_id=int(data["procedure_id"]),
            appointment_date=appointment_date,
            start_time=start_time,
            duration_minutes=duration,
        )
        return AppointmentRepository.add(appointment)

    @staticmethod
    def has_conflict(appointment_date, start_time, duration_minutes):
        requested_start = AppointmentService.combine(appointment_date, start_time)
        requested_end = requested_start + timedelta(minutes=duration_minutes)

        for item in AppointmentRepository.by_date(appointment_date):
            existing_start = AppointmentService.combine(item.appointment_date, item.start_time)
            existing_end = existing_start + timedelta(minutes=item.duration_minutes)
            if requested_start < existing_end and requested_end > existing_start:
                return True
        return False

    @staticmethod
    def to_24h_time(hour, minute, period):
        hour_number = int(hour)
        if period == "PM" and hour_number != 12:
            hour_number += 12
        if period == "AM" and hour_number == 12:
            hour_number = 0
        return f"{hour_number:02d}:{int(minute):02d}"

    @staticmethod
    def to_12h_time(time_value):
        parsed = datetime.strptime(time_value, "%H:%M")
        return parsed.strftime("%I:%M %p")

    @staticmethod
    def combine(appointment_date, start_time):
        return datetime.combine(
            appointment_date,
            datetime.strptime(start_time, "%H:%M").time(),
        )
