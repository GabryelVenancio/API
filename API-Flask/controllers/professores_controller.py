from flask import Blueprint, jsonify, request
from models.professores.professores import criar_professor, listar_professores, buscar_professor_por_id

professores_bp = Blueprint('professores', __name__)

professores = listar_professores()

@professores_bp.route('/', methods=['GET'])
def get_professores():
    """
    Lista todos os professores
    ---
    responses:
      200:
        description: Lista de professores retornada com sucesso
        content:
          application/json:
            example: [{"id": 1, "nome": "Carlos"}]
    """
    return jsonify(listar_professores())

@professores_bp.route('/', methods=['POST'])
def add_professor():
    """
    Cria um novo professor
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
                example: Ana
    responses:
      201:
        description: Professor criado com sucesso
        content:
          application/json:
            example: {"id": 2, "nome": "Ana"}
      400:
        description: Dados inválidos
    """
    data = request.get_json()
    if not data or 'nome' not in data:
        return jsonify({"erro": "professor sem nome"}), 400
    professor = criar_professor(data['nome'])
    return jsonify(professor), 201

@professores_bp.route('/<int:id>', methods=['GET'])
def get_professor(id):
    """
    Retorna um professor pelo ID
    ---
    parameters:
      - name: id
        in: path
        required: true
        description: ID do professor
        schema:
          type: integer
    responses:
      200:
        description: Professor encontrado
        content:
          application/json:
            example: {"id": 1, "nome": "Carlos"}
      404:
        description: Professor não encontrado
    """
    professor = buscar_professor_por_id(id)
    if professor:
        return jsonify(professor)
    return jsonify({"erro": "Professor não encontrado"}), 404

@professores_bp.route('/<int:id>', methods=['PUT'])
def update_professor(id):
    """
    Atualiza os dados de um professor
    ---
    parameters:
      - name: id
        in: path
        required: true
        description: ID do professor
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
        description: Professor atualizado
      404:
        description: Professor não encontrado
    """
    data = request.get_json()
    professor = buscar_professor_por_id(id)
    if professor:
        professor.update(data)
        return jsonify(professor)
    return jsonify({"erro": "Professor não encontrado"}), 404

@professores_bp.route('/<int:id>', methods=['DELETE'])
def delete_professor(id):
    """
    Deleta um professor pelo ID
    ---
    parameters:
      - name: id
        in: path
        required: true
        description: ID do professor
        schema:
          type: integer
    responses:
      200:
        description: Professor deletado com sucesso
      404:
        description: Professor não encontrado
    """
    global professores
    professor = buscar_professor_por_id(id)
    if professor:
        professores = [p for p in professores if p['id'] != id]
        return jsonify({"message": "Professor deletado com sucesso"})
    return jsonify({"erro": "Professor não encontrado"}), 404
