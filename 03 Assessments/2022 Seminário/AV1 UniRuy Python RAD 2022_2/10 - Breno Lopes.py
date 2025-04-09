# https://github.com/tosename/AV1_python/blob/main/AV1_python.py
# Cad Trajetos

from json.decoder import JSONDecodeError
import os
import os.path
import random
import json

cadastros_trajetos = {}

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

try:
    read_fake_db = open(os.path.join(__location__, 'fakebd.txt'), 'r')
    load_cadastros = read_fake_db.read()
    parsed_cadastros = json.loads(load_cadastros)

    for cadastro in parsed_cadastros:
        cadastros_trajetos.update({int(cadastro): parsed_cadastros[cadastro]})
    read_fake_db.close()

except FileNotFoundError:
    write_fake_db = open(os.path.join(__location__, 'fakebd.txt'), 'w')
    write_fake_db.write(r'{}')
    write_fake_db.close()

except JSONDecodeError:
    write_fake_db = open(os.path.join(__location__, 'fakebd.txt'), 'w')
    write_fake_db.write(r'{}')
    write_fake_db.close()


def clear_screen(): return os.system('cls')


def primary_key(id_trajeto):
    while id_trajeto in cadastros_trajetos:
        id_trajeto = random.randint(1, 1000)
    return id_trajeto


while True:
    resp_menu = input('''
    Menu Cadastro de Trajetos
    1 - Cadastrar novo trajeto
    2 - Consultar trajeto(s) cadastrado(s)
    3 - Atualizar um trajeto cadastrado
    4 - Excluir o cadastro de um trajeto
    5 - Sair
    Digite o número correspondente a opção desejada: '''
                      )

    if resp_menu == '1':
        clear_screen()
        origem_trajeto = input('Digite a cidade de origem do trajeto: ')
        destino_trajeto = input('Digite a cidade de destino do trajeto: ')
        try:
            valor_trajeto = int(input('Digite o valor do trajeto: '))
        except ValueError:
            print('\nValor inválido, assumindo valor 0...')
            valor_trajeto = 0

        id_trajeto = random.randint(1, 1000)
        id_trajeto_pk = primary_key(id_trajeto)

        cadastros_trajetos.update({id_trajeto_pk: dict(id=id_trajeto_pk, origem=origem_trajeto,
                                                       destino=destino_trajeto, valor=valor_trajeto)})

        print(f'\nNovo trajeto de id {id_trajeto_pk} cadastrado!')

    elif resp_menu == '2':
        clear_screen()
        resp_consulta = input(
            '1 - Buscar por id\n2 - Buscar por destino\n3 - Ver a lista completa de cadastros\n\nDigite o numero correspondente: ')

        clear_screen()
        if resp_consulta == '1':
            try:
                busca_id = int(
                    input('\nDigite o id do cadastro que deseja consultar: '))
            except ValueError:
                print('\nid inválido')
            else:
                if cadastros_trajetos.get(busca_id) == None:
                    print('\nNão há cadastro associado a esse id')
                else:
                    print('\n', cadastros_trajetos.get(busca_id))

        elif resp_consulta == '2':
            busca_destino = input(
                '\nDigite o destino do(s) cadastro(s) que deseja consultar: ')
            for cadastro in cadastros_trajetos:
                if cadastros_trajetos[cadastro]['destino'] == busca_destino:
                    print('\n', cadastros_trajetos[cadastro])

        elif resp_consulta == '3':
            clear_screen()
            for cadastro in cadastros_trajetos:
                print(cadastros_trajetos[cadastro], '\n')

        else:
            print('\nOpção inválida!')

    elif resp_menu == '3':
        clear_screen()
        try:
            busca_id = int(
                input('\nDigite o id do cadastro que deseja atualizar: '))

        except ValueError:
            print('\nid inválido')

        else:
            if cadastros_trajetos.get(busca_id) == None:
                print('\nNão foi encontrado cadastro associado a esse id')
            else:
                print(f'\nCadastro: {cadastros_trajetos.get(busca_id)}')

                resp_update = input('''
                1 - Atualizar origem
                2 - Atualizar destino
                3 - Atualizar valor
                Digite o número correspondente à informação que deseja alterar: '''
                                    )
                if resp_update == '1':
                    clear_screen()
                    origem_update = input('Digite a nova origem do trajeto: ')
                    cadastros_trajetos[busca_id].update(
                        {'origem': origem_update})
                    print('\nCadastro atualizado!',
                          f'\n{cadastros_trajetos[busca_id]}')

                elif resp_update == '2':
                    clear_screen()
                    destino_update = input(
                        'Digite a novo destino do trajeto: ')
                    cadastros_trajetos[busca_id].update(
                        {'destino': destino_update})
                    print('\nCadastro atualizado!',
                          f'\n{cadastros_trajetos[busca_id]}')

                elif resp_update == '3':
                    clear_screen()
                    try:
                        valor_update = int(
                            input('Digite a novo valor do trajeto: '))
                    except ValueError:
                        print('\nValor inválido')
                    else:
                        cadastros_trajetos[busca_id].update(
                            {'valor': valor_update})
                        print('\nCadastro atualizado!',
                              f'\n{cadastros_trajetos[busca_id]}')

                else:
                    print('\nOpção inválida!')

    elif resp_menu == '4':
        clear_screen()
        try:
            busca_id = int(
                input('\nDigite o id do cadastro que deseja excluir: '))

        except ValueError:
            print('\nid inválido')

        else:
            try:
                cadastros_trajetos.pop(busca_id)

            except KeyError:
                print('\nid não existente')

            else:
                print('\nCadastro excluído!')

    elif resp_menu == '5':
        break

    else:
        clear_screen()
        print('Opção inválida!')

    voltar_menu_true = 'sim'
    voltar_menu = input(
        '\nSe deseja voltar ao menu inicial digite "sim", caso contrário o programa encerrará.\n').lower()

    if voltar_menu == voltar_menu_true:
        clear_screen()
        continue
    else:
        break

write_fake_db = open(os.path.join(__location__, 'fakebd.txt'), 'w')
save_cadastros = json.dumps(cadastros_trajetos)
write_fake_db.write(save_cadastros)
write_fake_db.close()
