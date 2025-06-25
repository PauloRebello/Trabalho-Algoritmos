from util import limpar_tela
from aluno import cadastrar_aluno
from professor import cadastrar_professor

def ler_opcao(lim_sup):
    #ler a opção até q seja válido
    op = input('Escolha uma opção:   ')
    if op > 0 and op < lim_sup:
        return op
    print('Voce não digitou uma op válida!')
    return -1

def menu_principal():
    limpar_tela()
    print('+++++++++++++++++++++ MENU +++++++++++++++++++++++')
    print('1- Cadastrar')
    print('2- Matricular')
    print('3- Consultar')
    print('4- Relatório')
    print('0- Sair')
    op = ler_opcao(4)

#melhorar
    if op ==1:
        menu_cadastro()


def menu_cadastro():
    limpar_tela()
    print('+++++++ Menu Cadastrar ++++++++')
    print('1- Aluno')
    print('2- Professor')
    print('3- Turma')
    print('0- Voltar')
    op = ler_opcao(3)
    
    if op ==1:
        cadastrar_aluno()
    elif op == 2:
        cadastrar_professor()

def matricular():
    limpar_tela()
    print('+++++++ Menu Cadastrar ++++++++')
    print('1- Aluno')
    print('0- Voltar')
    op = ler_opcao(1)

