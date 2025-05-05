from flask import Blueprint

reset_bp = Blueprint('reset', __name__)

@reset_bp.route('/reset', methods=['POST'])
def reset():
    return {"mensagem": "Banco de dados resetado com sucesso!"}, 200
