from flask import Flask, render_template, request, redirect, url_for, session, flash

app = Flask(__name__)
app.secret_key = "chave_secreta_qualquer"

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        usuario = request.form["usuario"]
        senha = request.form["senha"]

        if usuario == "admin" and senha == "123":
            session["usuario"] = usuario
            return redirect(url_for("home"))
        else:
            flash("Usuário ou senha inválidos!")

    return render_template("login.html")


@app.route("/home")
def home():
    if "usuario" not in session:
        return redirect(url_for("login"))

    return render_template("home.html", usuario=session["usuario"])


@app.route("/logout")
def logout():
    session.pop("usuario", None)
    return redirect(url_for("login"))


if __name__ == "__main__":
    app.run(debug=True)