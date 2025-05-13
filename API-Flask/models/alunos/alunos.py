from config import db
from datetime import datetime
from typing import Optional, Tuple, Dict

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
        """Calcula a média final do aluno."""
        if self.nota_primeiro_semestre is None or self.nota_segundo_semestre is None:
            raise ValueError("As notas não podem ser None")
        
        self.media_final = (self.nota_primeiro_semestre + self.nota_segundo_semestre) / 2
        return self.media_final

    def to_dict(self):
        """Converte a instância do aluno em um dicionário."""
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

def criar_aluno(data: dict) -> Tuple[Dict, int]:
    """Cria um novo aluno no banco de dados."""
    try:
        # Verifica se todas as notas são válidas
        nota_primeiro_semestre = data.get('nota_primeiro_semestre')
        nota_segundo_semestre = data.get('nota_segundo_semestre')

        # Verificar se as notas estão presentes no corpo da requisição
        if nota_primeiro_semestre is None or nota_segundo_semestre is None:
            return {'error': 'Notas do primeiro ou segundo semestre não podem ser vazias. Recebido: nota_primeiro_semestre = {}, nota_segundo_semestre = {}'.format(nota_primeiro_semestre, nota_segundo_semestre)}, 400

        # Converte data_nascimento para formato de data
        try:
            data_nascimento = datetime.strptime(data['data_nascimento'], '%Y-%m-%d').date()
        except ValueError:
            return {'error': 'Formato de data inválido. Use YYYY-MM-DD.'}, 400
        
        aluno = Aluno(
            nome=data['nome'],
            idade=data['idade'],
            turma_id=data['turma_id'],
            data_nascimento=data_nascimento,
            nota_primeiro_semestre=nota_primeiro_semestre,
            nota_segundo_semestre=nota_segundo_semestre
        )
        
        aluno.calcular_media()  # Calcula a média após adicionar os dados válidos
        db.session.add(aluno)
        db.session.commit()
        
        return aluno.to_dict(), 201
    except Exception as e:
        db.session.rollback()
        return {'error': 'Erro ao criar aluno: {}'.format(str(e))}, 400
    
def listar_alunos_id() -> dict:
    """Retorna todos os alunos do banco de dados, incluindo a contagem total."""
    alunos = Aluno.query.all()  # Obtém todos os alunos
    alunos_dict = [aluno.to_dict() for aluno in alunos]  # Converte alunos para dicionário
    total_alunos = len(alunos_dict)  # Conta o número total de alunos
    return {
        "data": alunos_dict,
        "total_alunos": total_alunos
    }

def buscar_aluno_por_id(aluno_id: int) -> Optional[dict]:
    """Busca um aluno pelo ID no banco de dados."""
    aluno = db.session.get(Aluno, aluno_id)  # Usando db.session.get() no lugar de query.get()
    return aluno.to_dict() if aluno else None

def atualizar_aluno(aluno_id: int, data: dict) -> Tuple[Dict, int]:
    """Atualiza as informações de um aluno existente."""
    aluno = db.session.get(Aluno, aluno_id)  # Usando db.session.get() no lugar de query.get()
    if not aluno:
        return {'error': 'Aluno não encontrado'}, 404
    
    try:
        aluno.nome = data.get('nome', aluno.nome)
        aluno.idade = data.get('idade', aluno.idade)
        aluno.turma_id = data.get('turma_id', aluno.turma_id)
        
        if 'data_nascimento' in data:
            # Validação de formato de data
            try:
                aluno.data_nascimento = datetime.strptime(data['data_nascimento'], '%Y-%m-%d').date()
            except ValueError:
                return {'error': 'Formato de data inválido. Use YYYY-MM-DD.'}, 400
        
        if 'nota_primeiro_semestre' in data:
            aluno.nota_primeiro_semestre = data['nota_primeiro_semestre']
        
        if 'nota_segundo_semestre' in data:
            aluno.nota_segundo_semestre = data['nota_segundo_semestre']
        
        aluno.calcular_media()  # Recalcula a média após a atualização
        db.session.commit()
        return aluno.to_dict(), 200
    except Exception as e:
        db.session.rollback()
        return {'error': str(e)}, 400

def deletar_aluno(aluno_id: int) -> Tuple[Dict, int]:
    """Deleta um aluno pelo ID."""
    aluno = db.session.get(Aluno, aluno_id)  # Usando db.session.get() no lugar de query.get()
    if not aluno:
        return {'error': 'Aluno não encontrado'}, 404
    
    try:
        db.session.delete(aluno)
        db.session.commit()
        return {'message': 'Aluno deletado com sucesso'}, 200
    except Exception as e:
        db.session.rollback()
        return {'error': str(e)}, 400
