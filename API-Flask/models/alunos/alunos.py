from typing import Optional, List
from config import db

class Aluno(db.Model):
    __tablename__ = 'alunos'  # Nome explícito da tabela
    
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    turma_id = db.Column(db.Integer, db.ForeignKey('turmas.id'), nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'nome': self.nome,
            'email': self.email,
            'turma_id': self.turma_id
        }

def criar_aluno(nome: str, email: str) -> Aluno:
    """Cria e persiste um novo aluno no banco de dados.
    
    Args:
        nome: Nome completo do aluno
        email: Email único do aluno
        
    Returns:
        Objeto Aluno criado
    """
    novo_aluno = Aluno(nome=nome, email=email)
    db.session.add(novo_aluno)
    try:
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        raise e
    return novo_aluno

def listar_alunos() -> List[Aluno]:
    """Retorna todos os alunos cadastrados.
    
    Returns:
        Lista de objetos Aluno
    """
    return Aluno.query.order_by(Aluno.nome).all()

def buscar_aluno_por_id(aluno_id: int) -> Optional[Aluno]:
    """Busca um aluno pelo ID.
    
    Args:
        aluno_id: ID do aluno
        
    Returns:
        Objeto Aluno ou None se não encontrado
    """
    return Aluno.query.get(aluno_id)

def atualizar_aluno(aluno_id: int, nome: str, email: str) -> Optional[Aluno]:
    """Atualiza os dados de um aluno existente.
    
    Args:
        aluno_id: ID do aluno a ser atualizado
        nome: Novo nome
        email: Novo email
        
    Returns:
        Objeto Aluno atualizado ou None se não encontrado
    """
    aluno = buscar_aluno_por_id(aluno_id)
    if aluno:
        aluno.nome = nome
        aluno.email = email
        try:
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            raise e
    return aluno

def deletar_aluno(aluno_id: int) -> Optional[Aluno]:
    """Remove um aluno do banco de dados.
    
    Args:
        aluno_id: ID do aluno a ser removido
        
    Returns:
        Objeto Aluno removido ou None se não encontrado
    """
    aluno = buscar_aluno_por_id(aluno_id)
    if aluno:
        try:
            db.session.delete(aluno)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            raise e
    return aluno