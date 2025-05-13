from config import db
from typing import Optional, Tuple, Dict, List

class Professor(db.Model):
    __tablename__ = 'professores'
    
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    idade = db.Column(db.Integer, nullable=False)
    materia = db.Column(db.String(100), nullable=False)
    observacoes = db.Column(db.Text)
    
    turmas = db.relationship('Turma', backref='professor', lazy=True)

    def to_dict(self) -> Dict:
        return {
            'id': self.id,
            'nome': self.nome,
            'idade': self.idade,
            'materia': self.materia,
            'observacoes': self.observacoes
        }

# Funções CRUD
def criar_professor(data: Dict) -> Tuple[Dict, int]:
    try:
        professor = Professor(
            nome=data['nome'],
            idade=data['idade'],
            materia=data['materia'],
            observacoes=data.get('observacoes')
        )
        db.session.add(professor)
        db.session.commit()
        return professor.to_dict(), 201
    except Exception as e:
        db.session.rollback()
        return {'error': str(e)}, 400

def listar_professores_id() -> List[Dict]:
    professores = Professor.query.all()
    return [professor.to_dict() for professor in professores]

def buscar_professor_por_id(professor_id: int) -> Optional[Dict]:
    professor = Professor.query.get(professor_id)
    return professor.to_dict() if professor else None

def atualizar_professor(professor_id: int, data: Dict) -> Tuple[Dict, int]:
    professor = Professor.query.get(professor_id)
    if not professor:
        return {'error': 'Professor não encontrado'}, 404
    
    try:
        professor.nome = data.get('nome', professor.nome)
        professor.idade = data.get('idade', professor.idade)
        professor.materia = data.get('materia', professor.materia)
        professor.observacoes = data.get('observacoes', professor.observacoes)
        
        db.session.commit()
        return professor.to_dict(), 200
    except Exception as e:
        db.session.rollback()
        return {'error': str(e)}, 400

def deletar_professor(professor_id: int) -> Tuple[Dict, int]:
    professor = Professor.query.get(professor_id)
    if not professor:
        return {'error': 'Professor não encontrado'}, 404
    
    try:
        db.session.delete(professor)
        db.session.commit()
        return {'message': 'Professor deletado com sucesso'}, 200
    except Exception as e:
        db.session.rollback()
        return {'error': str(e)}, 400