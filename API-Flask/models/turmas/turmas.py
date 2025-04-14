turmas = []

def criar_turma(nome):
    nova = {'id': len(turmas) + 1, 'nome': nome}
    turmas.append(nova)
    return nova

def listar_turmas():
    return turmas

def buscar_turma_por_id(id):
    return next((t for t in turmas if t['id'] == id), None)