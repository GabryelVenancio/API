from flask import Blueprint, request, jsonify
from models.alunos import (
    criar_aluno,
    listar_alunos,
    buscar_aluno_por_id,
    atualizar_aluno,
    deletar_aluno
)

aluno_bp = Blueprint('aluno', __name__)

@aluno_bp.route('', methods=['GET'])
def listar_alunos():
    """
    Lista todos os alunos
    ---
    tags:
      - Alunos
    responses:
      200:
        description: Lista de alunos retornada com sucesso
        content:
          application/json:
            schema:
              type: array
              items:
                $ref: '#/components/schemas/Aluno'
    """
    alunos = listar_alunos()
    return jsonify(alunos)

@aluno_bp.route('', methods=['POST'])
def criar_aluno():
    """
    Cria um novo aluno
    ---
    tags:
      - Alunos
    requestBody:
      required: true
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/AlunoInput'
    responses:
      201:
        description: Aluno criado com sucesso
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/Aluno'
      400:
        description: Erro na requisição
    """
    data = request.get_json()
    resposta, status = criar_aluno(data)
    return jsonify(resposta), status

@aluno_bp.route('/<int:id>', methods=['PUT'])
def atualizar_aluno(id):
    """
    Atualiza um aluno existente
    ---
    tags:
      - Alunos
    parameters:
      - name: id
        in: path
        required: true
        schema:
          type: integer
        description: ID do aluno a ser atualizado
    requestBody:
      required: true
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/AlunoInput'
    responses:
      200:
        description: Aluno atualizado com sucesso
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/Aluno'
      400:
        description: Erro na validação dos dados
      404:
        description: Aluno não encontrado
    """
    data = request.get_json()
    resposta, status = atualizar_aluno(id, data)
    return jsonify(resposta), status

@aluno_bp.route('/<int:id>', methods=['DELETE'])
def deletar_aluno(id):
    """
    Remove um aluno pelo ID
    ---
    tags:
      - Alunos
    parameters:
      - name: id
        in: path
        required: true
        schema:
          type: integer
        description: ID do aluno a ser removido
    responses:
      200:
        description: Aluno removido com sucesso
        content:
          application/json:
            schema:
              type: object
              properties:
                message:
                  type: string
                  example: "Aluno removido com sucesso"
      404:
        description: Aluno não encontrado
    """
    resposta, status = deletar_aluno(id)
    return jsonify(resposta), status