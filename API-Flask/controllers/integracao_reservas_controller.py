import requests
from flask import Blueprint, request, jsonify

integracao_reserva_bp = Blueprint('integracao_reserva', __name__)

URL_API_RESERVAS = "http://localhost:5001/reservas"

@integracao_reserva_bp.route('/reservas', methods=['GET'])
def listar_reservas():
    try:
        resposta = requests.get(URL_API_RESERVAS)
        return jsonify(resposta.json()), resposta.status_code
    except requests.exceptions.RequestException as e:
        return jsonify({'erro': 'Não foi possível conectar ao serviço de reservas', 'detalhes': str(e)}), 500

@integracao_reserva_bp.route('/reservas', methods=['POST'])
def criar_reserva():
    dados = request.get_json()
    try:
        resposta = requests.post(URL_API_RESERVAS, json=dados)
        return jsonify(resposta.json()), resposta.status_code
    except requests.exceptions.RequestException as e:
        return jsonify({'erro': 'Não foi possível conectar ao serviço de reservas', 'detalhes': str(e)}), 500

@integracao_reserva_bp.route('/reservas/<int:id>', methods=['DELETE'])
def deletar_reserva(id):
    try:
        resposta = requests.delete(f"{URL_API_RESERVAS}/{id}")
        return jsonify(resposta.json()), resposta.status_code
    except requests.exceptions.RequestException as e:
        return jsonify({'erro': 'Não foi possível conectar ao serviço de reservas', 'detalhes': str(e)}), 500
