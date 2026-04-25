from flask import Blueprint, flash, redirect, render_template, request, url_for
from flask_login import login_required

from app.services.procedure_service import ProcedureService


procedures_bp = Blueprint("procedures", __name__, url_prefix="/procedimentos")


@procedures_bp.route("/", methods=["GET", "POST"])
@login_required
def index():
    if request.method == "POST":
        ProcedureService.create(request.form)
        flash("Procedimento cadastrado com sucesso.", "success")
        return redirect(url_for("procedures.index"))

    return render_template(
        "procedures/index.html",
        procedures=ProcedureService.list_all(),
    )
