#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  2 09:40:08 2024

@author: vitor
"""

import xml.etree.ElementTree as ET
from datetime import datetime as dt

#%%
tree = ET.parse('xml/EDMISLON.PJC')
root = tree.getroot()

#%% Satas
path_data_inicio = 'dataAdmissao'
path_data_termino = 'dataDemissao'

dataInicio = dt.fromtimestamp(int(root.find(path_data_inicio).text)/1000).strftime('%m/%Y')

dataTermino = dt.fromtimestamp(int(root.find(path_data_termino).text)/1000).strftime('%m/%Y')

print(dataInicio)
print(dataTermino)

#%% Segundo passo: Valores!!
# PODE SER VARIAÇÃO SALARIAL, REMUNERAÇÃO, SAL. PAG, 
# SALÁRIO, SALÁRIO PAGO E ETC, DEPENDE DE QUEM DIGITA:
#

matches = ['salario','sal. pag', 'salario pago', 'remuneração', 'remuneração', 'salario base']

for col in root.findall("./historicosSalariais/Set/HistoricoSalarial/nome"):
    for x in matches:
        if x in str.lower(col.text):
            # Achei o caminho dos Salarios
            # Agora preciso dos valores
#            print(col.text)
            path = "./historicosSalariais/Set/HistoricoSalarial[nome='"+col.text+"']/ocorrencias/List/OcorrenciaDoHistoricoSalarial/valor"
            for col in root.findall(path):
                print(col.text)
            

#%%  CONTRIBUIÇÃO SOCIAL SEGURADO (DESCONTAR DO PRINCIPAL)
# DEVIDO SEGURADO
# Tabela 1
for col in root.findall("./inss/Inss/inssSobreSalariosDevidos/InssSobreSalariosDevidos/ocorrencias/Set/OcorrenciaDeInssSobreSalariosDevidos/valorDevidoSeguradoVerbas"):
    if col.text != "null":
        print("{:.2f}".format(float(col.text)))
    
#%% Tabela 2

for col in root.findall("./inss/Inss/inssSobreSalariosDevidos/InssSobreSalariosDevidos/ocorrencias/Set/OcorrenciaDeInssSobreSalariosDevidos/valorDevidoEmpresaVerbas"):
    if col.text != "null":
        print("{:.2f}".format(float(col.text)))


#%% Tabela 3

for col in root.findall("./inss/Inss/inssSobreSalariosDevidos/InssSobreSalariosDevidos/ocorrencias/Set/OcorrenciaDeInssSobreSalariosDevidos/valorDevidoSAT"):
    if col.text != "null":
        print("{:.2f}".format(float(col.text)))


# CADA CÓDIGO DESSE REPRESENTA UM DADO:
"""
108251 = CONTRIBUIÇÃO SOCIAL SEGURADO (DESCONTAR DO PRINCIPAL
113851 = Nome: CONTRIBUIÇÃO SOCIAL EMPRESA
164651 = Nome: SEGURO DE ACIDENTE DO TRABALHO (SAT
OS VALORES TÊM QUE ESTÁ AO LADO DA REFERIDA COMPETÊNCIA.
"""


#%% IRPF

irpf = root.find("./dadosEstruturados/impostoRenda").text