import requests
from flask import Blueprint, request, jsonify

integracao_atividade_bp = Blueprint('integracao_atividade', __name__)

URL_API_ATIVIDADES = "http://localhost:5002/atividades"

@integracao_atividade_bp.route('/atividades', methods=['GET'])
def listar_atividades():
    try:
        resposta = requests.get(URL_API_ATIVIDADES)
        return jsonify(resposta.json()), resposta.status_code
    except requests.exceptions.RequestException as e:
        return jsonify({'erro': 'Não foi possível conectar ao serviço de atividades', 'detalhes': str(e)}), 500

@integracao_atividade_bp.route('/atividades', methods=['POST'])
def criar_atividade():
    dados = request.get_json()
    try:
        resposta = requests.post(URL_API_ATIVIDADES, json=dados)
        return jsonify(resposta.json()), resposta.status_code
    except requests.exceptions.RequestException as e:
        return jsonify({'erro': 'Não foi possível conectar ao serviço de atividades', 'detalhes': str(e)}), 500

@integracao_atividade_bp.route('/atividades/<int:id>', methods=['DELETE'])
def deletar_atividade(id):
    try:
        resposta = requests.delete(f"{URL_API_ATIVIDADES}/{id}")
        return jsonify(resposta.json()), resposta.status_code
    except requests.exceptions.RequestException as e:
        return jsonify({'erro': 'Não foi possível conectar ao serviço de atividades', 'detalhes': str(e)}), 500
