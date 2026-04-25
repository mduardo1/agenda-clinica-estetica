from flask import Blueprint, redirect, render_template, url_for
from flask_login import login_required


main_bp = Blueprint("main", __name__)


@main_bp.route("/")
def index():
    return redirect(url_for("main.menu"))


@main_bp.route("/menu")
@login_required
def menu():
    return render_template("main/menu.html")
