from config import db
from datetime import datetime
from typing import Optional, Tuple, Dict, Union

class Aluno(db.Model):
    __tablename__ = 'alunos'
    
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    idade = db.Column(db.Integer, nullable=False)
    turma_id = db.Column(db.Integer, db.ForeignKey('turmas.id'), nullable=False)
    data_nascimento = db.Column(db.Date, nullable=False)
    nota_primeiro_semestre = db.Column(db.Float, nullable=False)
    nota_segundo_semestre = db.Column(db.Float, nullable=False)
    media_final = db.Column(db.Float, nullable=True)

    def calcular_media(self):
        if self.nota_primeiro_semestre is None or self.nota_segundo_semestre is None:
            raise ValueError("As notas não podem ser None")
        
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

def criar_aluno(data: dict) -> Tuple[Dict, int]:
    """Cria um novo aluno no banco de dados."""
    try:
        # Verificar se as notas estão presentes
        if 'nota_primeiro_semestre' not in data or 'nota_segundo_semestre' not in data:
            return {'error': 'Notas do primeiro ou segundo semestre não fornecidas'}, 400

        try:
            nota_primeiro_semestre = float(data['nota_primeiro_semestre'])
            nota_segundo_semestre = float(data['nota_segundo_semestre'])
        except (TypeError, ValueError):
            return {'error': 'Notas devem ser números válidos'}, 400

        # Verificar se a data de nascimento é válida
        try:
            data_nascimento = datetime.strptime(data['data_nascimento'], '%Y-%m-%d').date()
        except (KeyError, ValueError):
            return {'error': 'Formato de data inválido. Use YYYY-MM-DD.'}, 400

        aluno = Aluno(
            nome=data['nome'],
            idade=data['idade'],
            turma_id=data['turma_id'],
            data_nascimento=data_nascimento,
            nota_primeiro_semestre=nota_primeiro_semestre,
            nota_segundo_semestre=nota_segundo_semestre
        )

        aluno.calcular_media()
        db.session.add(aluno)
        db.session.commit()

        return aluno.to_dict(), 201

    except Exception as e:
        db.session.rollback()
        return {'error': f'Erro ao criar aluno: {str(e)}'}, 400

def listar_alunos() -> dict:
    alunos = Aluno.query.all()
    alunos_dict = [aluno.to_dict() for aluno in alunos]
    return {
        "data": alunos_dict,
        "total_alunos": len(alunos_dict)
    }

def buscar_aluno_por_id(aluno_id: int) -> Optional[dict]:
    aluno = db.session.get(Aluno, aluno_id)
    return aluno.to_dict() if aluno else None

def atualizar_aluno(aluno_id: int, data: dict) -> Tuple[Dict, int]:
    aluno = db.session.get(Aluno, aluno_id)
    if not aluno:
        return {'error': 'Aluno não encontrado'}, 404
    
    try:
        aluno.nome = data.get('nome', aluno.nome)
        aluno.idade = data.get('idade', aluno.idade)
        aluno.turma_id = data.get('turma_id', aluno.turma_id)

        if 'data_nascimento' in data:
            try:
                aluno.data_nascimento = datetime.strptime(data['data_nascimento'], '%Y-%m-%d').date()
            except ValueError:
                return {'error': 'Formato de data inválido. Use YYYY-MM-DD.'}, 400

        if 'nota_primeiro_semestre' in data:
            nota1 = data['nota_primeiro_semestre']
            if not isinstance(nota1, (int, float)):
                return {'error': 'A nota do primeiro semestre deve ser numérica'}, 400
            aluno.nota_primeiro_semestre = nota1

        if 'nota_segundo_semestre' in data:
            nota2 = data['nota_segundo_semestre']
            if not isinstance(nota2, (int, float)):
                return {'error': 'A nota do segundo semestre deve ser numérica'}, 400
            aluno.nota_segundo_semestre = nota2

        aluno.calcular_media()
        db.session.commit()
        return aluno.to_dict(), 200

    except Exception as e:
        db.session.rollback()
        return {'error': f'Erro ao atualizar aluno: {str(e)}'}, 400

def deletar_aluno(aluno_id: int) -> Tuple[Dict, int]:
    aluno = db.session.get(Aluno, aluno_id)
    if not aluno:
        return {'error': 'Aluno não encontrado'}, 404

    try:
        db.session.delete(aluno)
        db.session.commit()
        return {'message': 'Aluno deletado com sucesso'}, 200
    except Exception as e:
        db.session.rollback()
        return {'error': f'Erro ao deletar aluno: {str(e)}'}, 400
