from config import db

class Aluno(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)

def criar_aluno(nome, email):
    novo_aluno = Aluno(nome=nome, email=email)
    db.session.add(novo_aluno)
    db.session.commit()
    return novo_aluno

def listar_alunos():
    return Aluno.query.all()

def buscar_aluno_por_id(aluno_id):
    return Aluno.query.get(aluno_id)

def atualizar_aluno(aluno_id, nome, email):
    aluno = Aluno.query.get(aluno_id)
    if aluno:
        aluno.nome = nome
        aluno.email = email
        db.session.commit()
    return aluno

def deletar_aluno(aluno_id):
    aluno = Aluno.query.get(aluno_id)
    if aluno:
        db.session.delete(aluno)
        db.session.commit()
    return aluno