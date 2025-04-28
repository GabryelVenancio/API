from flask import Blueprint, jsonify, request
from models.alunos.alunos import criar_aluno, listar_alunos, buscar_aluno_por_id

alunos_bp = Blueprint('alunos', __name__)

alunos = listar_alunos()

@alunos_bp.route('/', methods=['GET'])
def get_alunos():
    """
    Lista todos os alunos
    ---
    responses:
      200:
        description: Lista de alunos retornada com sucesso
        content:
          application/json:
            example: [{"id": 1, "nome": "João"}]
    """
    return jsonify(listar_alunos())

@alunos_bp.route('/', methods=['POST'])
def add_aluno():
    """
    Cria um novo aluno
    ---
    requestBody:
      required: true
      content:
        application/json:
          schema:
            type: object
            required:
              - nome
            properties:
              nome:
                type: string
                example: Maria
    responses:
      201:
        description: Aluno criado com sucesso
        content:
          application/json:
            example: {"id": 2, "nome": "Maria"}
      400:
        description: Dados inválidos
    """
    data = request.get_json()
    if not data or 'nome' not in data:
        return jsonify({"erro": "aluno sem nome"}), 400
    aluno = criar_aluno(data['nome'])
    return jsonify(aluno), 201

@alunos_bp.route('/<int:id>', methods=['GET'])
def get_aluno(id):
    """
    Retorna um aluno pelo ID
    ---
    parameters:
      - name: id
        in: path
        required: true
        description: ID do aluno
        schema:
          type: integer
    responses:
      200:
        description: Aluno encontrado
        content:
          application/json:
            example: {"id": 1, "nome": "João"}
      404:
        description: Aluno não encontrado
    """
    aluno = buscar_aluno_por_id(id)
    if aluno:
        return jsonify(aluno)
    return jsonify({"erro": "Aluno não encontrado"}), 404

@alunos_bp.route('/<int:id>', methods=['PUT'])
def update_aluno(id):
    """
    Atualiza os dados de um aluno
    ---
    parameters:
      - name: id
        in: path
        required: true
        description: ID do aluno
        schema:
          type: integer
    requestBody:
      required: true
      content:
        application/json:
          schema:
            type: object
            properties:
              nome:
                type: string
                example: "Novo Nome"
    responses:
      200:
        description: Aluno atualizado
      404:
        description: Aluno não encontrado
    """
    data = request.get_json()
    aluno = buscar_aluno_por_id(id)
    if aluno:
        aluno.update(data)
        return jsonify(aluno)
    return jsonify({"erro": "Aluno não encontrado"}), 404

@alunos_bp.route('/<int:id>', methods=['DELETE'])
def delete_aluno(id):
    """
    Deleta um aluno pelo ID
    ---
    parameters:
      - name: id
        in: path
        required: true
        description: ID do aluno
        schema:
          type: integer
    responses:
      200:
        description: Aluno deletado com sucesso
      404:
        description: Aluno não encontrado
    """
    global alunos
    aluno = buscar_aluno_por_id(id)
    if aluno:
        alunos = [a for a in alunos if a['id'] != id]
        return jsonify({"message": "Aluno deletado com sucesso"})
    return jsonify({"erro": "Aluno não encontrado"}), 404
