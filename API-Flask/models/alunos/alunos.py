alunos = []

def criar_aluno(nome):
    novo = {'id': len(alunos) + 1, 'nome': nome}
    alunos.append(novo)
    return novo

def listar_alunos():
    return alunos

def buscar_aluno_por_id(id):
    return next((a for a in alunos if a['id'] == id), None)