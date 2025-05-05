from config import db

class Professor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    disciplina = db.Column(db.String(100), nullable=False)

def criar_professor(nome, disciplina):
    novo_professor = Professor(nome=nome, disciplina=disciplina)
    db.session.add(novo_professor)
    db.session.commit()
    return novo_professor

def listar_professores():
    return Professor.query.all()

def buscar_professor_por_id(professor_id):
    return Professor.query.get(professor_id)

def atualizar_professor(professor_id, nome, disciplina):
    professor = Professor.query.get(professor_id)
    if professor:
        professor.nome = nome
        professor.disciplina = disciplina
        db.session.commit()
    return professor

def deletar_professor(professor_id):
    professor = Professor.query.get(professor_id)
    if professor:
        db.session.delete(professor)
        db.session.commit()
    return professor