from flask import Flask
from models import db
from controllers import bp as departamento_bp

app = Flask(__name__)
# Ajustar aqui os paraêmtros do banco de dados
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:5555@localhost:3305/clinica'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

with app.app_context():
    db.create_all()

app.register_blueprint(departamento_bp)

if __name__ == '__main__':
    app.run(debug=True)