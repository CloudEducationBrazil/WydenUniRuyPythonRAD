# https://github.com/users/carlos1258ss/projects/1?classId=27bd03ab-65b6-4263-90af-50d093a0956a&assignmentId=13d15b99-4d64-423e-8899-741ed1d1f38b&submissionId=effabd34-421b-3e08-c3a6-f47aa7ed31ab
# Cadastro Vinho

import tkinter as tk
from tkinter import ttk
import datetime as dt

lista_tipos = ["tinto", "rose", "branco"]
lista_codigos = []

janela = tk.Tk()


def inserir_codigo():


descricao = entry_descricao.get()
tipo = combobox_selecionar_tipo.get()
quant = entry_quant.get()
data_criacao = dt.datetime.now()
data_criacao = data_criacao.strftime("%d/%m/%Y %H:%M")
codigo = len(lista_codigos)+1
codigo_str = "COD-{}".format(codigo)
lista_codigos.append((codigo_str, descricao, tipo, quant, data_criacao))

janela.title('Ferramenta de cadastro de vinhos')

label_descricao = tk.Label(text="nome do vinho")
label_descricao.grid(row=1, column=0, padx=10, pady=10,
                     sticky='nswe', columnspan=4)

entry_descricao = tk.Entry()
entry_descricao.grid(row=2, column=0, padx=10, pady=10,
                     sticky='nswe', columnspan=4)

label_tipo_unidade = tk.Label(text="Tipo do vinho")
label_tipo_unidade.grid(row=3, column=0, padx=10,
                        pady=10, sticky='nswe', columnspan=2)

combobox_selecionar_tipo = ttk.Combobox(values=lista_tipos)
combobox_selecionar_tipo.grid(
    row=3, column=2, padx=10, pady=10, sticky='nswe', columnspan=2)

label_quant = tk.Label(text="preço")
label_quant.grid(row=4, column=0, padx=10, pady=10,
                 sticky='nswe', columnspan=2)

entry_quant = tk.Entry()
entry_quant.grid(row=4, column=2, padx=10, pady=10,
                 sticky='nswe', columnspan=2)

botao_criar_codigo = tk.Button(text="cadastrar", command=inserir_codigo)
botao_criar_codigo.grid(row=5, column=0, padx=10,
                        pady=10, sticky='nswe', columnspan=4)

janela.mainloop()

print(lista_codigos)
