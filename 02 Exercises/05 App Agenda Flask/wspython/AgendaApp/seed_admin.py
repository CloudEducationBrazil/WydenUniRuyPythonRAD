from app import create_app, db
from app.models.user_model import User

app = create_app()

with app.app_context():
    user = User.query.filter_by(username="admin").first()
    if not user:
        user = User(username="admin")
        user.set_password("123")
        db.session.add(user)
        db.session.commit()
        print("Usuário admin criado: admin / 123")
    else:
        print("Usuário admin já existe.")
