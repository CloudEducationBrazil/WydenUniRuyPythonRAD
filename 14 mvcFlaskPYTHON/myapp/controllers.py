from flask import Blueprint, request, redirect, url_for, render_template
from models import Departamento, db

bp = Blueprint('departamento', __name__)

@bp.route('/')
def index():
    departamentos = Departamento.query.all()
    return render_template('index.html', departamentos=departamentos)

@bp.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        nome = request.form['nome']
        novo_departamento = Departamento(nome=nome)
        db.session.add(novo_departamento)
        db.session.commit()
        return redirect(url_for('departamento.index'))
    return render_template('create.html')

@bp.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    departamento = Departamento.query.get(id)
    if request.method == 'POST':
        departamento.nome = request.form['nome']
        db.session.commit()
        return redirect(url_for('departamento.index'))
    return render_template('edit.html', departamento=departamento)

@bp.route('/delete/<int:id>', methods=['POST'])
def delete(id):
    departamento = Departamento.query.get(id)
    db.session.delete(departamento)
    db.session.commit()
    return redirect(url_for('departamento.index'))