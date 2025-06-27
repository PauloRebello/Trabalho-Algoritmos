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

def validar_cpf(cpf):
    return cpf.isdigit() and len(cpf) == 11

def validar_email(email):
    return "@" in email and "." in email.split("@")[-1]

def cadastrar_participante():
    print("=== Cadastro de Participante ===")
    nome = input("Nome completo: ")
    
    while True:
        cpf = input("CPF (somente números, 11 dígitos): ")
        if validar_cpf(cpf):
            break
        print("CPF inválido. Deve conter exatamente 11 dígitos numéricos.")
        
    while True:
        email = input("Email (ex: nome@email.com): ")
        if validar_email(email):
            break
        print("Email inválido. Certifique-se de incluir '@' e um domínio válido (ex: usuario@dominio.com)")

    preferencias = input("Temas de interesse: "). split(",")

    participante = {"cpf": cpf, "nome": nome, "email": email, "preferencias": [tema.strip() for tema in preferencias], "eventos": []}

    participantes.append(participante)
    print(f"Participante {nome} cadastrado com sucesso!")

def listar_participantes():
    print("=== Lista de Participantes ===")
    for p in participantes:
        print(f"CPF: {p['cpf']}, Nome:{p['nome']} , Email: {p['email']}")
    input("\nPressione Enter para voltar...")

def buscar_participante_cpf(cpf):
    for p in participantes:
        if p["cpf"] == cpf:
            return p
    return None