#IMPORTS
import datetime
import locale

#VALIDA SE O ID É UM INTEIRO
def isInt(id):
    try:
        int(id)
        return True
    except ValueError:
        return False

#VALIDA SE A DATA É VALIDA
def isData(data):
    try:
        datetime.datetime.strptime(str(data), '%d/%m/%Y').strftime('%d/%m/%Y')
        return True
    except:
        return False

#VALIDA SE O VALOR É VALIDO
def isNumeric(value):
    try:
        if str.isnumeric(value):
            return True
        else:
            return False
    except ValueError:
        return False

#FORMATA VALOR DO SERVIÇO
def coin(value):
    val = int(value)
    locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
    val = locale.currency(val, grouping=True, symbol=None)
    return str(val)