from config import db
from typing import Dict, Union, List, Optional

class Turma(db.Model):
    __tablename__ = 'turmas'  # Nome explícito da tabela
    
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    periodo = db.Column(db.String(50), nullable=False)
    
    alunos = db.relationship('Aluno', backref='turma_rel', lazy=True)
    
    def to_dict(self) -> Dict[str, Union[int, str]]:
        """Converte o objeto Turma para dicionário."""
        return {
            'id': self.id,
            'nome': self.nome,
            'periodo': self.periodo
        }

def criar_turma(nome: str, periodo: str) -> Turma:
    """Cria e persiste uma nova turma no banco de dados."""
    nova_turma = Turma(nome=nome, periodo=periodo)
    db.session.add(nova_turma)
    try:
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        raise e
    return nova_turma

def listar_turmas() -> List[Turma]:
    """Retorna todas as turmas cadastradas."""
    return Turma.query.order_by(Turma.nome).all()

def buscar_turma_por_id(turma_id: int) -> Optional[Turma]:
    """Busca uma turma pelo ID."""
    return Turma.query.get(turma_id)

def atualizar_turma(turma_id: int, nome: str, periodo: str) -> Optional[Turma]:
    """Atualiza os dados de uma turma existente."""
    turma = buscar_turma_por_id(turma_id)
    if turma:
        turma.nome = nome
        turma.periodo = periodo
        try:
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            raise e
    return turma

def deletar_turma(turma_id: int) -> Optional[Turma]:
    """Remove uma turma do banco de dados."""
    turma = buscar_turma_por_id(turma_id)
    if turma:
        try:
            db.session.delete(turma)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            raise e
    return turma