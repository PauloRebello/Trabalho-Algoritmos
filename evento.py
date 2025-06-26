eventos = [
    {
    'nome': 'Workshop GitHub',
    'data': '15-07-2025',
    'tema': 'GitHub',
    'participantes': [''] #adicionar cpf de cada participante, criar banco de dados? manual:? teste? ['']
    }
]
def cadastrar_evento():
    #ler todos os dados do aluno {cpf:123, nome: beto, endereço: rua x, + 2}
    professor = {'cpf': '123', 'nome': 'beto', 'end': 'rua x', 'titulacao': '123123'}
    #professores.append(professor)

def listar_eventos():
    print("--- Lista de Eventos ---")

def buscar_evento_por_nome(nome):
    for i in eventos:
        if i['nome'].lower() == nome.lower():
            return i
    return None 