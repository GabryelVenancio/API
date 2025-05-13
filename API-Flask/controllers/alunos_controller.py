from flask import Blueprint, request, jsonify
from models.alunos import (
    criar_aluno,
    listar_alunos_id,
    atualizar_aluno,
    deletar_aluno
)

aluno_bp = Blueprint('aluno', __name__)

@aluno_bp.route('', methods=['GET'])
def listar_alunos_route():
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
              type: object
              properties:
                data:
                  type: array
                  items:
                    $ref: '#/components/schemas/Aluno'
                total_alunos:
                  type: integer
    """
    response = listar_alunos_id()
    return jsonify(response), 200

@aluno_bp.route('', methods=['POST'])
def criar_aluno_route():
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
    if not data:
        return jsonify({'error': 'JSON inválido ou ausente'}), 400

    required_fields = ['nome', 'idade', 'turma_id', 'data_nascimento', 'nota_primeiro_semestre', 'nota_segundo_semestre']
    for field in required_fields:
        if field not in data:
            return jsonify({'error': f'Campo {field} é obrigatório'}), 400

    resposta, status = criar_aluno(data)
    return jsonify(resposta), status

@aluno_bp.route('/<int:id>', methods=['PUT'])
def atualizar_aluno_route(id):
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
    if not data:
        return jsonify({'error': 'JSON inválido ou ausente'}), 400

    resposta, status = atualizar_aluno(id, data)
    return jsonify(resposta), status

@aluno_bp.route('/<int:id>', methods=['DELETE'])
def deletar_aluno_route(id):
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
