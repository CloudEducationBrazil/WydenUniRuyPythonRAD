from flask import Flask, Response, request, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
import mysql.connector
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost:3306'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key= True)
    nome = db.Column(db.String(50))
    email = db.Column(db.String(100))
    senha = db.Column(db.String(60))

    def to_json(self):
        return {"id": self.id, "nome": self.nome, "email": self.email}
    
    def set_senha(self, senha):
        self.senha = bcrypt.generate_password_hash(senha).decode('utf-8')

    def check_senha(self, senha):
        return bcrypt.check_password_hash(self.senha, senha)

# Selecionar Tudo
@app.route("/usuarios", methods=["GET"])
def seleciona_usuarios():
    usuarios_objetos = Usuario.query.all()
    usuarios_json = [usuario.to_json() for usuario in usuarios_objetos]

    return gera_response(200, "usuarios", usuarios_json)

# Selecionar Individual
@app.route("/usuario/<id>", methods=["GET"])
def seleciona_usuario(id):
    usuario_objeto = Usuario.query.filter_by(id=id).first()
    usuario_json = usuario_objeto.to_json()

    return gera_response(200, "usuario", usuario_json)

# Cadastrar
@app.route("/usuario", methods=["POST"])
def cria_usuario():
    body = request.get_json()

    try:
        usuario = Usuario(nome=body["nome"], email= body["email"])
        usuario.set_senha(body["senha"])
        db.session.add(usuario)
        db.session.commit()
        return gera_response(201, "usuario", usuario.to_json(), "Criado com sucesso")
    except Exception as e:
        print('Erro', e)
        return gera_response(400, "usuario", {}, "Erro ao cadastrar")


# Atualizar
@app.route("/usuario/<id>", methods=["PUT"])
def atualiza_usuario(id):
    usuario_objeto = Usuario.query.filter_by(id=id).first()
    body = request.get_json()

    try:
        if('nome' in body):
            usuario_objeto.nome = body['nome']
        if('email' in body):
            usuario_objeto.email = body['email']
        if 'senha' in body:
            usuario_objeto.set_senha(body['senha'])
        
        db.session.add(usuario_objeto)
        db.session.commit()
        return gera_response(200, "usuario", usuario_objeto.to_json(), "Atualizado com sucesso")
    except Exception as e:
        print('Erro', e)
        return gera_response(400, "usuario", {}, "Erro ao atualizar")

# Deletar
@app.route("/usuario/<id>", methods=["DELETE"])
def deleta_usuario(id):
    usuario_objeto = Usuario.query.filter_by(id=id).first()

    try:
        db.session.delete(usuario_objeto)
        db.session.commit()
        return gera_response(200, "usuario", usuario_objeto.to_json(), "Deletado com sucesso")
    except Exception as e:
        print('Erro', e)
        return gera_response(400, "usuario", {}, "Erro ao deletar")


def gera_response(status, nome_do_conteudo, conteudo, mensagem=False):
    body = {}
    body[nome_do_conteudo] = conteudo

    if(mensagem):
        body["mensagem"] = mensagem

    return Response(json.dumps(body), status=status, mimetype="application/json")


if __name__ == '__main__':
    try:
        app.run(debug=True)
    except Exception as e:
        print(f"Erro: {str(e)}")