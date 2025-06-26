eventos = [
    {
    'nome': 'Workshop GitHub',
    'data': '15-07-2025',
    'tema': 'GitHub',
    'participantes': [''] #adicionar cpf de cada participante, criar banco de dados? manual:? teste? ['']
    }
]

def cadastrar_evento():
    print("--- Cadastro de Evento ---")
    nome = input("Nome do evento: ")
    data = input("Data (dd-mm-aaaa): ")
    tema = input("Tema central: ")
#PRECISO FAZER VALIDAÇÕES PARA ERROS E FPRMATOS ERRADOS
    evento = {
        'nome': nome,
        'data': data,
        'tema': tema,
        'participantes': []
    }
    eventos.append(evento)
    print(f"Evento '{nome}' cadastrado com sucesso!")

def listar_eventos():
    print("--- Lista de Eventos ---")
    for i in eventos:
        print(f'nome: {i['nome']}, Data: {i['data']}, Tema: {i['tema']}, Participantes: {len(i['participantes'])}')

def buscar_evento_por_nome(nome):
    for i in eventos:
        if i['nome'].lower() == nome.lower():
            return i
    return None 