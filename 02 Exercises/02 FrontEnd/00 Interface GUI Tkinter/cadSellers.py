# https: // docs.python.org/pt-br/dev/library/tkinter.html

# Interface Gráfica:
# Passos: 1. Importar a bib tkinter; 2. Criar uma função; 3. Criar a janela utilizando o tkinter
# 4. Invocar uma função

from pip._vendor import requests
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

import os
import time
import dmlBDGenerica

def listar():
    os.system('cls')
    vquery = "select * from tb_sellers"
    recordset = dmlBDGenerica.dql(vquery)

    quadroGrid = LabelFrame(app, text="Vendedores")
    quadroGrid.pack(fill="both", expand="no", padx=10, pady=10)

    treeView = ttk.Treeview(quadroGrid, columns=('id', 'name'), show='headings')
    treeView.column('id', minwidth=0, width=50)
    treeView.column('name', minwidth=0, width=150)
    treeView.heading('id', text='ID')
    treeView.heading('name', text='Nome')
    treeView.pack()

    for linha in recordset:
      print('Nome:', linha)
      treeView.insert("", "end", values = linha)
    
    messagebox.showinfo(title="Vendedores", message="Listagem Ok!!!")
    quadroGrid.destroy()
   
def gerarTXT():
    if vNome.get() == "":
        messagebox.showinfo(title="ERRO - Vendedores", message="Name não informado!!!")
    else:
        pastaApp = os.path.dirname(__file__)
        # print(pastaApp)
        arqSellers = pastaApp+"\\sellers.txt"
        arqSellers = open(arqSellers, 'w')
        #arqSellers.write('Id:%s' % vId.get())
        arqSellers.write('\nNome:%s' % vNome.get())
        arqSellers.write('\n')
        arqSellers.close()

        messagebox.showinfo(title="Lista de Vendedores", message="Gerada com sucesso...")

def inserirSeller():
    if vNome.get() == "":
      messagebox.showinfo(title="ERRO - Vendedores", message="Name não informado!!!")

    if vNome.get() != "":
        vnome = vNome.get()
        vquery = "INSERT INTO tb_sellers (NAME) VALUES ('" + \
            vnome+"' )"
        dmlBDGenerica.dml(vquery)

        # Limpando os campos
        vNome.delete(0, END)

        messagebox.showinfo(title="Vendedores", message="Cadastrado com sucesso...")

        print('Dados gravados com sucesso ...')
    else:
        print('Erro na inclusão dos dados!!!')

app = Tk()
app.title('Cadastro de Vendedor')
app.geometry("500x330")  # largura x altura
app.configure(bg='#dde')

# primeiro criar o texto, depois associar ao grid para posicionar
# anchor =N ; S; E = Leste W= Oeste; NE;SE;SO;NO
Label(
    app, text='Nome',
    bg='#dde', fg='#009', anchor=W).place(x=10, y=10, width=100, height=20)

# Input
vNome = Entry(app)
vNome.place(x=10, y=30, width=200, height=20)

Button(app, text="Cadastrar Vendedor",
       command=inserirSeller).place(x=10, y=290, width=150, height=20)

Button(app, text="Listar",
       command=listar).place(x=170, y=290, width=100, height=20)

Button(app, text="Gerar TXT",
       command=gerarTXT).place(x=280, y=290, width=100, height=20)

app.mainloop()
