from flask import Blueprint, flash, redirect, render_template, request, url_for
from flask_login import login_required

from app.services.client_service import ClientService


clients_bp = Blueprint("clients", __name__, url_prefix="/clientes")


@clients_bp.route("/", methods=["GET", "POST"])
@login_required
def index():
    if request.method == "POST":
        ClientService.create(request.form)
        flash("Cliente cadastrada com sucesso.", "success")
        return redirect(url_for("clients.index"))

    return render_template("clients/index.html", clients=ClientService.list_all())
