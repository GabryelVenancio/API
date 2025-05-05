from config import db
from typing import Dict, Union, List, Optional

class Professor(db.Model):
    """Modelo de representação de um professor no banco de dados."""
    __tablename__ = 'professores'
    
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    disciplina = db.Column(db.String(100), nullable=False)
    
    def to_dict(self) -> Dict[str, Union[int, str]]:
        """Converte o objeto Professor para dicionário."""
        return {
            'id': self.id,
            'nome': self.nome,
            'disciplina': self.disciplina
        }

def criar_professor(nome: str, disciplina: str) -> Professor:
    """Cria e persiste um novo professor no banco de dados."""
    novo_professor = Professor(nome=nome, disciplina=disciplina)
    db.session.add(novo_professor)
    try:
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        raise e
    return novo_professor

def listar_professores() -> List[Professor]:
    """Retorna todos os professores cadastrados."""
    return Professor.query.order_by(Professor.nome).all()

def buscar_professor_por_id(professor_id: int) -> Optional[Professor]:
    """Busca um professor pelo ID."""
    return Professor.query.get(professor_id)

def atualizar_professor(professor_id: int, nome: str, disciplina: str) -> Optional[Professor]:
    """Atualiza os dados de um professor existente."""
    professor = buscar_professor_por_id(professor_id)
    if professor:
        professor.nome = nome
        professor.disciplina = disciplina
        try:
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            raise e
    return professor

def deletar_professor(professor_id: int) -> Optional[Professor]:
    """Remove um professor do banco de dados."""
    professor = buscar_professor_por_id(professor_id)
    if professor:
        try:
            db.session.delete(professor)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            raise e
    return professor