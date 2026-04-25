from datetime import date

from flask import Blueprint, flash, redirect, render_template, request, url_for
from flask_login import login_required

from app.services.appointment_service import AppointmentService
from app.services.client_service import ClientService
from app.services.procedure_service import ProcedureService
from app.services.reminder_service import ReminderService


appointments_bp = Blueprint("appointments", __name__, url_prefix="/agenda")


@appointments_bp.route("/", methods=["GET"])
@login_required
def calendar():
    current_year = request.args.get("year", default=date.today().year, type=int)
    current_month = request.args.get("month", default=date.today().month, type=int)
    selected_date = request.args.get("date", default=date.today().isoformat())

    return render_template(
        "appointments/calendar.html",
        year=current_year,
        month=current_month,
        selected_date=selected_date,
        months=month_options(),
        appointments=AppointmentService.list_by_month(current_year, current_month),
        clients=ClientService.list_all(),
        procedures=ProcedureService.list_all(),
        reminders=ReminderService.pending_messages(current_year, current_month),
    )


@appointments_bp.route("/novo", methods=["POST"])
@login_required
def create():
    try:
        AppointmentService.create(request.form)
        flash("Agendamento criado com sucesso.", "success")
    except ValueError as error:
        flash(str(error), "error")

    return redirect(
        url_for(
            "appointments.calendar",
            year=request.form.get("year"),
            month=request.form.get("month"),
            date=request.form.get("appointment_date"),
        )
    )


@appointments_bp.route("/gerenciamento")
@login_required
def management():
    current_year = request.args.get("year", default=date.today().year, type=int)
    current_month = request.args.get("month", default=date.today().month, type=int)
    appointments = AppointmentService.list_by_month(current_year, current_month)
    total_cost = sum(item.procedure.cost for item in appointments)
    total_price = sum(item.procedure.price for item in appointments)

    return render_template(
        "appointments/management.html",
        year=current_year,
        month=current_month,
        months=month_options(),
        appointments=appointments,
        total_cost=total_cost,
        total_price=total_price,
        total_profit=total_price - total_cost,
    )


def month_options():
    return [
        (1, "Janeiro"),
        (2, "Fevereiro"),
        (3, "Marco"),
        (4, "Abril"),
        (5, "Maio"),
        (6, "Junho"),
        (7, "Julho"),
        (8, "Agosto"),
        (9, "Setembro"),
        (10, "Outubro"),
        (11, "Novembro"),
        (12, "Dezembro"),
    ]
