from banco import gerar_lista_participantes 
participantes = [
    {
        'cpf': '11111111111',
        'nome': 'Ana Clara',
        'email': 'ana.clara@email.com',
        'preferencias': ['IA', 'Web'],
        'eventos': []
    },
    {
        'cpf': '11111111112',
        'nome': 'Caio Valentim',
        'email': 'caio.valentim@email.com',
        'preferencias': ['Segurança', 'Dados'],
        'eventos': []
    },
    {
        'cpf': '11111111113',
        'nome': 'Paulo Rebello',
        'email': 'paulo.rebello@email.com',
        'preferencias': ['IA'],
        'eventos': []
    }
] + gerar_lista_participantes(5)

""" 
ADICIONAR PARTICIPANTES FICTICIOS PARA TESTES.
POSSÍVEL GERAR COM RANDOM OU IMPORTAR???
MELHORAR A EFICÁCIA DO CÓDIGO
PENSAR EM COMO O USUÁRIO PODE 
DIGITAR ALGO ERRADO E DAR ERRO NO CÓDIGO
CPF PODE SERVIR COMO CÓDIGO ÚNICO DO PARTICIPANTE*****
"""
def cadastrar_participante():
    print("=== Cadastro de Participante ===")
    nome = input("Nome completo: ")
    cpf = input("CPF: ")
    email = input("Email: ")
    preferencias = input("Temas de interesse: "). split(",")

    participante = {"cpf": cpf, "nome": nome, "email": email, "preferencias": [tema.strip() for tema in preferencias], "eventos": []}

    participantes.append(participante)
    print(f"Participante {nome} cadastrado com sucesso!")

def listar_participantes():
    print("=== Lista de Participantes ===")
    for p in participantes:
        print(f"CPF: {p['cpf']}, Nome:{p['nome']} , Email: {p['email']}")
    
def buscar_participante_cpf(cpf):
    for p in participantes:
        if p["cpf"] == cpf:
            return p
    return None