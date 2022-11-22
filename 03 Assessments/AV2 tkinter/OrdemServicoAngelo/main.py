# https://github.com/A21n13g0/Ordem-de-Servico
# Angelo - Python RAD - Professor Heleno Cardoso (22/11/2022)
# Import do tkinter e tkcalendar
# pip install tkcalendar 
# pip3 install tkcalendar
# python.exe -m pip install --upgrade pip
# virtualenv(para Python 2) ou venv, possivelmente via poetry, (para Python 3).

from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkcalendar import Calendar, DateEntry

# Import do process
from process import *

# Cores
co0 = "#f0f3f5"  # Preta
co1 = "#feffff"  # branca
co2 = "#4fa882"  # verde
co3 = "#38576b"  # valor
co4 = "#403d3d"   # letra
co5 = "#e06636"   # - profit
co6 = "#038cfc"   # azul
co7 = "#ef5350"   # vermelha
co8 = "#263238"   # + verde
co9 = "#e9edf5"   # sky blue

# Tela
aux = 0
window = Tk()
window.title("Ordem de Serviço")
window.geometry("1043x453")
window.configure(bg=co9)
window.resizable(width=False, height=False)

# Divisor da tela
frame_top = Frame(window, width=310, height=50, bg=co2, relief='flat')
frame_top.grid(row=0, column=0)

frame_base = Frame(window, width=310, height=400, bg=co1, relief='flat')
frame_base.grid(row=1, column=0, padx=0, pady=1, sticky=NSEW)

frame_right = Frame(window, width=580, height=400, bg=co1, relief='flat')
frame_right.grid(row=0, column=1, rowspan=2, padx=1, pady=0, sticky=NSEW)

# Label top
app_name = Label(frame_top, text='Formulario de Ordem de Serviço',
                 anchor=NW, font=('Ivy 13 bold'), bg=co2, fg=co1, relief='flat')
app_name.place(x=10, y=20)

# Label base
label_os = Label(frame_base, text='Numero da OS *', anchor=NW,
                 font=('Ivy 10 bold'), bg=co1, fg=co4, relief='flat')
label_os.place(x=10, y=10)
entry_os = Entry(frame_base, width=45, justify='left', relief='solid')
entry_os.place(x=15, y=30)

label_typeService = Label(frame_base, text='Tipo de Serviço *',
                          anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4, relief='flat')
label_typeService.place(x=10, y=50)
entry_typeService = Entry(frame_base, width=45, justify='left', relief='solid')
entry_typeService.place(x=15, y=70)

label_description = Label(frame_base, text='Descrição *', anchor=NW,
                          font=('Ivy 10 bold'), bg=co1, fg=co4, relief='flat')
label_description.place(x=10, y=90)
entry_description = Entry(frame_base, width=45, justify='left', relief='solid')
entry_description.place(x=15, y=110)

label_date = Label(frame_base, text='Data do Serviço *', anchor=NW,
                   font=('Ivy 10 bold'), bg=co1, fg=co4, relief='flat')
label_date.place(x=10, y=140)
entry_date = DateEntry(
    frame_base, width=12, background='darkblue', foreground='white', borderwidth=2)
entry_date.place(x=15, y=160)

label_provider = Label(frame_base, text='Prestador *', anchor=NW,
                       font=('Ivy 10 bold'), bg=co1, fg=co4, relief='flat')
label_provider.place(x=10, y=190)
entry_provider = Entry(frame_base, width=45, justify='left', relief='solid')
entry_provider.place(x=15, y=210)

label_client = Label(frame_base, text='Cliente *', anchor=NW,
                     font=('Ivy 10 bold'), bg=co1, fg=co4, relief='flat')
label_client.place(x=10, y=230)
entry_client = Entry(frame_base, width=45, justify='left', relief='solid')
entry_client.place(x=15, y=250)

label_value = Label(frame_base, text='Valor *', anchor=NW,
                    font=('Ivy 10 bold'), bg=co1, fg=co4, relief='flat')
label_value.place(x=10, y=270)
entry_value = Entry(frame_base, width=45, justify='left', relief='solid')
entry_value.place(x=15, y=290)

# frame right - Exibir registros


def show():
    global tree
    list = select()

    # Lista para cabecario
    table_head = ['ID', 'OS', 'Serviço', 'Descrição',
                  'Data', 'Provedor', 'Cliente', 'Valor']

    # Criando a tabela
    tree = ttk.Treeview(frame_right, selectmode="extended",
                        columns=table_head, show="headings")

    # Vertical scrollbar
    vsb = ttk.Scrollbar(frame_right, orient="vertical", command=tree.yview)

    # Horizontal scrollbar
    hsb = ttk.Scrollbar(frame_right, orient="horizontal", command=tree.xview)

    tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
    tree.grid(column=0, row=0, sticky='nsew')
    vsb.grid(column=1, row=0, sticky='ns')
    hsb.grid(column=0, row=1, sticky='ew')

    frame_right.grid_rowconfigure(0, weight=12)

    hd = ["nw", "nw", "nw", "nw", "nw", "nw", "nw", "nw"]
    h = [30, 70, 120, 120, 100, 100, 100, 70]
    n = 0

    for col in table_head:
        tree.heading(col, text=col.title(), anchor=CENTER)
        tree.column(col, width=h[n], anchor=hd[n])

        n += 1

    for item in list:
        tree.insert('', 'end', values=item)

# Cadastrar


def register():
    os = entry_os.get()
    typeService = entry_typeService.get()
    description = entry_description.get()
    date = entry_date.get()
    provider = entry_provider.get()
    client = entry_client.get()
    value = entry_value.get()

    if os == '' or typeService == '' or description == '' or provider == '' or client == '' or value == '':
        messagebox.showerror(
            "Erro", "Preencha todos os campos para cadastrar!")
    else:
        service = [os, typeService, description, date, provider, client, value]
        insert(service)
        messagebox.showinfo(
            "Sucesso", "Ordem de serviço cadastrada com sucesso!")

        entry_os.delete(0, 'end')
        entry_typeService.delete(0, 'end')
        entry_description.delete(0, 'end')
        entry_date.delete(0, 'end')
        entry_provider.delete(0, 'end')
        entry_client.delete(0, 'end')
        entry_value.delete(0, 'end')

    for widget in frame_right.winfo_children():
        widget.destroy()

    show()

# Atualizar


def change():
    global aux
    try:
        treep_data = tree.focus()
        treep_dictionary = tree.item(treep_data)
        tree_list = treep_dictionary['values']

        id = tree_list[0]

        if aux != 0 and aux == tree_list[0]:
            messagebox.showerror("Erro", "Registro já está selecionado!")
        else:
            aux = id
            entry_date.delete(0, 'end')
            entry_os.insert(0, tree_list[1])
            entry_typeService.insert(0, tree_list[2])
            entry_description.insert(0, tree_list[3])
            entry_date.insert(0, tree_list[4])
            entry_provider.insert(0, tree_list[5])
            entry_client.insert(0, tree_list[6])
            entry_value.insert(0, tree_list[7])

        def executeUpdate():
            global aux
            os = entry_os.get()
            typeService = entry_typeService.get()
            description = entry_description.get()
            date = entry_date.get()
            provider = entry_provider.get()
            client = entry_client.get()
            value = entry_value.get()

            if os == '' or typeService == '' or description == '' or provider == '' or client == '' or value == '':
                messagebox.showerror(
                    "Erro", "Preencha todos os campos para atualizar!")
            else:
                aux = 0
                service = [os, typeService, description,
                           date, provider, client, value, id]
                update(service)
                messagebox.showinfo(
                    "Sucesso", "Ordem de serviço atualizada com sucesso!")

                entry_os.delete(0, 'end')
                entry_typeService.delete(0, 'end')
                entry_description.delete(0, 'end')
                entry_date.delete(0, 'end')
                entry_provider.delete(0, 'end')
                entry_client.delete(0, 'end')
                entry_value.delete(0, 'end')

            for widget in frame_right.winfo_children():
                widget.destroy()

            show()

        btn_confirm = Button(frame_base, command=executeUpdate, text='Confirmar', width=7, font=(
            'Ivy 10 bold'), bg=co8, fg=co1, relief='raised', overrelief='ridge')
        btn_confirm.place(x=160, y=350)

    except IndexError:
        messagebox.showerror("Erro", "Selecione um registro da tabela!")

# Deletar


def remove():
    try:
        treep_data = tree.focus()
        treep_dictionary = tree.item(treep_data)
        tree_list = treep_dictionary['values']

        id = [tree_list[0]]

        delete(id)
        messagebox.showinfo(
            "Sucesso", "Ordem de serviço removida com sucesso!")

        for widget in frame_right.winfo_children():
            widget.destroy()

        show()
    except IndexError:
        messagebox.showerror("Erro", "Selecione um registro da tabela!")


# Botões
btn_insert = Button(frame_base, command=register, text='Inserir', width=7, font=(
    'Ivy 10 bold'), bg=co2, fg=co1, relief='raised', overrelief='ridge')
btn_insert.place(x=10, y=350)

btn_update = Button(frame_base, command=change, text='Atualizar', width=7, font=(
    'Ivy 10 bold'), bg=co8, fg=co1, relief='raised', overrelief='ridge')
btn_update.place(x=85, y=350)

btn_delete = Button(frame_base, command=remove, text='Deletar', width=7, font=(
    'Ivy 10 bold'), bg=co7, fg=co1, relief='raised', overrelief='ridge')
btn_delete.place(x=235, y=350)

# Exibindo os componentes visuais
show()
window.mainloop()
