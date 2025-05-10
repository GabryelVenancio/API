from config import db
from datetime import datetime
from typing import Optional

class Aluno(db.Model):
    __tablename__ = 'alunos'
    
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    idade = db.Column(db.Integer, nullable=False)
    turma_id = db.Column(db.Integer, db.ForeignKey('turmas.id'), nullable=False)
    data_nascimento = db.Column(db.Date, nullable=False)
    nota_primeiro_semestre = db.Column(db.Float, nullable=False)
    nota_segundo_semestre = db.Column(db.Float, nullable=False)
    media_final = db.Column(db.Float, nullable=False)

    def calcular_media(self):
        self.media_final = (self.nota_primeiro_semestre + self.nota_segundo_semestre) / 2
        return self.media_final

    def to_dict(self):
        return {
            'id': self.id,
            'nome': self.nome,
            'idade': self.idade,
            'turma_id': self.turma_id,
            'data_nascimento': str(self.data_nascimento),
            'nota_primeiro_semestre': self.nota_primeiro_semestre,
            'nota_segundo_semestre': self.nota_segundo_semestre,
            'media_final': self.media_final
        }

# Funções CRUD
def criar_aluno(data: dict) -> tuple:
    try:
        data_nascimento = datetime.strptime(data['data_nascimento'], '%Y-%m-%d').date()
        aluno = Aluno(
            nome=data['nome'],
            idade=data['idade'],
            turma_id=data['turma_id'],
            data_nascimento=data_nascimento,
            nota_primeiro_semestre=data['nota_primeiro_semestre'],
            nota_segundo_semestre=data['nota_segundo_semestre']
        )
        aluno.calcular_media()
        db.session.add(aluno)
        db.session.commit()
        return aluno.to_dict(), 201
    except Exception as e:
        db.session.rollback()
        return {'error': str(e)}, 400

def listar_alunos() -> list:
    alunos = Aluno.query.all()
    return [aluno.to_dict() for aluno in alunos]

def buscar_aluno_por_id(aluno_id: int) -> Optional[dict]:
    aluno = Aluno.query.get(aluno_id)
    return aluno.to_dict() if aluno else None

def atualizar_aluno(aluno_id: int, data: dict) -> tuple:
    aluno = Aluno.query.get(aluno_id)
    if not aluno:
        return {'error': 'Aluno não encontrado'}, 404
    
    try:
        aluno.nome = data.get('nome', aluno.nome)
        aluno.idade = data.get('idade', aluno.idade)
        aluno.turma_id = data.get('turma_id', aluno.turma_id)
        
        if 'data_nascimento' in data:
            aluno.data_nascimento = datetime.strptime(data['data_nascimento'], '%Y-%m-%d').date()
        
        if 'nota_primeiro_semestre' in data:
            aluno.nota_primeiro_semestre = data['nota_primeiro_semestre']
        
        if 'nota_segundo_semestre' in data:
            aluno.nota_segundo_semestre = data['nota_segundo_semestre']
        
        aluno.calcular_media()
        db.session.commit()
        return aluno.to_dict(), 200
    except Exception as e:
        db.session.rollback()
        return {'error': str(e)}, 400

def deletar_aluno(aluno_id: int) -> tuple:
    aluno = Aluno.query.get(aluno_id)
    if not aluno:
        return {'error': 'Aluno não encontrado'}, 404
    
    try:
        db.session.delete(aluno)
        db.session.commit()
        return {'message': 'Aluno deletado com sucesso'}, 200
    except Exception as e:
        db.session.rollback()
        return {'error': str(e)}, 400