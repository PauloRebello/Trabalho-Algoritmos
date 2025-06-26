import random

nomes = ["Sara", "Bruna", "Shelton", "Vitória", "João", "Luana", "Leonardo", "Helena", "Alexandre", "Jaqueline"]
sobrenomes = ["Silva", "Souza", "Oliveira", "Lima", "Costa", "Ferreira", "Ribeiro", "Martins", "Gomes", "Barbosa"]
temas = ["IA", "Web", "Segurança", "Dados", "DevOps"]

def gerar_cpf():
    return ''.join([str(random.randint(0, 9)) for _ in range(11)])

def gerar_email(nome):
    return f"{nome.lower()}@exemplo.com"

def gerar_participante():
    nome_completo = f"{random.choice(nomes)} {random.choice(sobrenomes)}"
    cpf = gerar_cpf()
    email = gerar_email(nome_completo.replace(' ', '.'))
    preferencias = random.sample(temas, k=random.randint(1, 3))

    participante = {
        'cpf': cpf,
        'nome': nome_completo,
        'email': email,
        'preferencias': preferencias,
        'eventos': []
    }
    return participante

def gerar_lista_participantes(qtd):
    return [gerar_participante() for _ in range(qtd)]
