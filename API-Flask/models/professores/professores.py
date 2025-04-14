
professores = []

def criar_professor(nome):
    novo = {'id': len(professores) + 1, 'nome': nome}
    professores.append(novo)
    return novo

def listar_professores():
    return professores

def buscar_professor_por_id(id):
    return next((p for p in professores if p['id'] == id), None)