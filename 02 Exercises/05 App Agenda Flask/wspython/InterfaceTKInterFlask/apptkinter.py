import tkinter as tk
from tkinter import messagebox

def entrar():
    user = usuario.get()
    pwd = senha.get()

    if user == "admin" and pwd == "123":
        messagebox.showinfo("Login", "Login realizado com sucesso!")
    else:
        messagebox.showerror("Login", "Usuário ou senha inválidos!")

janela = tk.Tk()
janela.title("Login")
janela.geometry("250x150")

tk.Label(janela, text="Usuário:").pack()
usuario = tk.Entry(janela)
usuario.pack()

tk.Label(janela, text="Senha:").pack()
senha = tk.Entry(janela, show="*")
senha.pack()

botao = tk.Button(janela, text="Entrar", command=entrar)
botao.pack(pady=10)

janela.mainloop()