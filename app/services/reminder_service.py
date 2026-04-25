from datetime import datetime, timedelta

from app.repositories.appointment_repository import AppointmentRepository
from app.services.appointment_service import AppointmentService


class ReminderService:
    @staticmethod
    def pending_messages(year, month):
        now = datetime.now()
        limit = now + timedelta(hours=1)
        messages = []

        for appointment in AppointmentRepository.by_month(year, month):
            start_at = AppointmentService.combine(
                appointment.appointment_date,
                appointment.start_time,
            )
            if now <= start_at <= limit and not appointment.reminder_sent:
                messages.append(
                    {
                        "whatsapp": appointment.client.whatsapp,
                        "message": (
                            f"Ola {appointment.client.full_name}, lembramos do seu "
                            f"procedimento {appointment.procedure.name} as "
                            f"{AppointmentService.to_12h_time(appointment.start_time)}. "
                            f"Duracao: {appointment.duration_minutes} minutos."
                        ),
                    }
                )
        return messages
