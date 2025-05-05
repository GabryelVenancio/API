from config import db

class Turma(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    periodo = db.Column(db.String(100), nullable=False)

def criar_turma(nome, periodo):
    nova_turma = Turma(nome=nome, periodo=periodo)
    db.session.add(nova_turma)
    db.session.commit()
    return nova_turma

def listar_turmas():
    return Turma.query.all()

def buscar_turma_por_id(turma_id):
    return Turma.query.get(turma_id)

def atualizar_turma(turma_id, nome, periodo):
    turma = Turma.query.get(turma_id)
    if turma:
        turma.nome = nome
        turma.periodo = periodo
        db.session.commit()
    return turma

def deletar_turma(turma_id):
    turma = Turma.query.get(turma_id)
    if turma:
        db.session.delete(turma)
        db.session.commit()
    return turma