from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required
from datetime import datetime
from app import db
from app.models.agenda_model import Agenda

agenda_bp = Blueprint("agenda", __name__, url_prefix="/agenda")

@agenda_bp.route("/listar")
@login_required
def listar_agenda():
    registros = Agenda.query.order_by(Agenda.data.desc()).all()
    return render_template("agenda_list.html", registros=registros)

@agenda_bp.route("/novo", methods=["GET", "POST"])
@login_required
def nova_agenda():
    if request.method == "POST":
        data = request.form["data"]
        descricao = request.form["descricao"]
        realizada = True if request.form.get("realizada") == "on" else False

        agenda = Agenda(
            data=datetime.strptime(data, "%Y-%m-%d").date(),
            descricao=descricao,
            realizada=realizada
        )

        db.session.add(agenda)
        db.session.commit()

        return redirect(url_for("agenda.listar_agenda"))

    return render_template("agenda_form.html")

@agenda_bp.route("/editar/<int:id>", methods=["GET", "POST"])
@login_required
def editar_agenda(id):
    agenda = Agenda.query.get_or_404(id)

    if request.method == "POST":
        agenda.data = datetime.strptime(request.form["data"], "%Y-%m-%d").date()
        agenda.descricao = request.form["descricao"]
        agenda.realizada = True if request.form.get("realizada") == "on" else False

        db.session.commit()
        return redirect(url_for("agenda.listar_agenda"))

    return render_template("agenda_form.html", agenda=agenda)

@agenda_bp.route("/excluir/<int:id>")
@login_required
def excluir_agenda(id):
    agenda = Agenda.query.get_or_404(id)
    db.session.delete(agenda)
    db.session.commit()

    return redirect(url_for("agenda.listar_agenda"))
