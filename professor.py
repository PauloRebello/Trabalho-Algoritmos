professores = []

def cadastrar_professor():
    #ler todos os dados do aluno {cpf:123, nome: beto, endereço: rua x, + 2}
    professor = {'cpf': '123', 'nome': 'beto', 'end': 'rua x', 'titulacao': '123123'}
    professores.append(professor)

def listar_professores():
    print(professores)