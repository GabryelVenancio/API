from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Professor(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # Identificador único para cada professor
    nome = db.Column(db.String(100), nullable=False)  # Nome do professor (obrigatório)
    email = db.Column(db.String(100), unique=True, nullable=False)  # E-mail único (obrigatório)
    disciplina = db.Column(db.String(100), nullable=False)  # Disciplina que o professor leciona

class Turma(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # Identificador único para cada turma
    nome = db.Column(db.String(100), nullable=False)  # Nome da turma (obrigatório)
    professor_id = db.Column(db.Integer, db.ForeignKey('professor.id'), nullable=False)  # Chave estrangeira para associar um professor à turma
    professor = db.relationship('Professor', backref=db.backref('turmas', lazy=True))  # Relacionamento entre Turma e Professor

class Aluno(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # Identificador único para cada aluno
    nome = db.Column(db.String(100), nullable=False)  # Nome do aluno (obrigatório)
    email = db.Column(db.String(100), unique=True, nullable=False)  # E-mail único do aluno (obrigatório)
    turma_id = db.Column(db.Integer, db.ForeignKey('turma.id'), nullable=False)  # Chave estrangeira para associar um aluno a uma turma
    turma = db.relationship('Turma', backref=db.backref('alunos', lazy=True))  # Relacionamento entre Aluno e Turma
