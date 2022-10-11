from AV01.lib.interface import *
from time import sleep

lista_compras_e_vendas = [{}]


def cadastrar():
    id = leiaint('Digite o codigo do produto:')
    nome_cliente = str(input("Nome do cliente/Fornecedor: "))
    nome_produto = str(input("Produto: "))
    preço = leiafloat('Digite o preço do produto: ')
    if id in lista_compras_e_vendas:
        print('produto já existente!')
    else:
        lista_compras_e_vendas.append(
            {"ID": id, "Nome do Cliente/Fornecedor": nome_cliente, 'Produto': nome_produto, 'Preço': preço})

    return cadastrar


def excluir():
    prod = input('Digite o id do produto:')
    del (lista_compras_e_vendas[int(prod)])
    return excluir


def gravarArquivo():
    a = open('bd.txt', 'at', encoding='utf-8')
    data = str(lista_compras_e_vendas)
    a.write(data)
    a.close()
    return gravarArquivo


def importarArquivo():
    arquivo = open('bd.txt', 'r', encoding='utf-8')
    lista = arquivo.readlines()  # readlinesssssss
    arquivo.close()
    lista_compras_e_vendas.append(lista)
    return importarArquivo
