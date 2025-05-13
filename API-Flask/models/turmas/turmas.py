from config import db
from typing import Optional, Tuple, Dict, List

class Turma(db.Model):
    __tablename__ = 'turmas'
    
    id = db.Column(db.Integer, primary_key=True)
    descricao = db.Column(db.String(100), nullable=False)
    professor_id = db.Column(db.Integer, db.ForeignKey('professores.id'), nullable=False)
    ativo = db.Column(db.Boolean, default=True)
    
    alunos = db.relationship('Aluno', backref='turma', lazy=True)

    def to_dict(self) -> Dict:
        return {
            'id': self.id,
            'descricao': self.descricao,
            'professor_id': self.professor_id,
            'ativo': self.ativo
        }

def criar_turma(data: Dict) -> Tuple[Dict, int]:
    try:
        required_fields = ['descricao', 'professor_id']
        for field in required_fields:
            if field not in data:
                return {'error': f'Campo {field} é obrigatório'}, 400

        turma = Turma(
            descricao=data['descricao'],
            professor_id=data['professor_id'],
            ativo=data.get('ativo', True)
        )
        db.session.add(turma)
        db.session.commit()
        return turma.to_dict(), 201
    except Exception as e:
        db.session.rollback()
        return {'error': str(e)}, 400

def listar_turmas() -> List[Dict]:
    turmas = Turma.query.all()
    return [turma.to_dict() for turma in turmas]

def buscar_turma_por_id(turma_id: int) -> Optional[Dict]:
    turma = Turma.query.get(turma_id)
    return turma.to_dict() if turma else None

def atualizar_turma(turma_id: int, data: Dict) -> Tuple[Dict, int]:
    turma = Turma.query.get(turma_id)
    if not turma:
        return {'error': 'Turma não encontrada'}, 404

    if 'professor_id' in data and not data['professor_id']:
        return {'error': 'Campo professor_id não pode ser vazio'}, 400

    try:
        turma.descricao = data.get('descricao', turma.descricao)
        turma.professor_id = data.get('professor_id', turma.professor_id)
        turma.ativo = data.get('ativo', turma.ativo)
        
        db.session.commit()
        return turma.to_dict(), 200
    except Exception as e:
        db.session.rollback()
        return {'error': str(e)}, 400

def deletar_turma(turma_id: int) -> Tuple[Dict, int]:
    turma = Turma.query.get(turma_id)
    if not turma:
        return {'error': 'Turma não encontrada'}, 404

    if turma.alunos:
        return {'error': 'Não é possível excluir a turma. Existem alunos associados a ela.'}, 400
    
    try:
        db.session.delete(turma)
        db.session.commit()
        return {'message': 'Turma deletada com sucesso'}, 200
    except Exception as e:
        db.session.rollback()
        return {'error': str(e)}, 400
