from util import limpar_tela
from participante import cadastrar_participante, listar_participantes
from evento import cadastrar_evento, listar_eventos

def ler_opcao(lim_sup):
    try:
        op = int(input('Escolha uma opção:   '))
        if 0 <= op <= lim_sup:
            return op
    except ValueError:
        pass
    print('Voce não digitou uma opção válida!')
    return -1

def menu_principal():
    while True:
        limpar_tela()
        print('+++++++++++++++++++++ MENU +++++++++++++++++++++++')
        print('1- Cadastrar')
        print('2- Listar')
        print('0- Sair')
        op = ler_opcao(2)

        if op ==1:
            menu_cadastro()
        elif op ==1:
            menu_listagem()
        elif op == 0:
            print("Saindo do sistema...")
            break

def menu_cadastro():
    limpar_tela()
    print('+++++++ Menu Cadastrar ++++++++')
    print('1- Participante')
    print('2- Evento')
    print('0- Voltar')
    op = ler_opcao(2)
    
    if op == 1:
        cadastrar_participante()
    elif op == 2:
        cadastrar_evento()

def menu_listagem():
    limpar_tela()
    print('+++++++ Menu Listar ++++++++')
    print('1- Participantes')
    print('2- Eventos')
    print('0- Voltar')
    op = ler_opcao(2)

    if op == 1:
        listar_participantes()
    elif op == 2:
        listar_eventos()
