from flask import Blueprint, flash, redirect, render_template, request, url_for
from flask_login import login_required

from app.services.anamnesis_service import AnamnesisService
from app.services.client_service import ClientService


anamnesis_bp = Blueprint("anamnesis", __name__, url_prefix="/anamnese")


@anamnesis_bp.route("/", methods=["GET", "POST"])
@login_required
def index():
    selected_client_id = request.args.get("client_id", type=int)

    if request.method == "POST":
        AnamnesisService.create(request.form)
        flash("Ficha de anamnese salva com sucesso.", "success")
        return redirect(url_for("anamnesis.index", client_id=request.form["client_id"]))

    records = []
    if selected_client_id:
        records = AnamnesisService.list_by_client(selected_client_id)

    return render_template(
        "anamnesis/index.html",
        clients=ClientService.list_all(),
        selected_client_id=selected_client_id,
        records=records,
    )
