import random
from flask import Flask, jsonify
from flask_cors import CORS 

app = Flask(__name__)
CORS(app) 

ingredientes_sugestao = [
    'Manjericão', 'Tomate', 'Queijo Parmesão', 'Azeite de Oliva', 'Alho', 'Cebola'
]

@app.route('/ingrediente-do-dia', methods=['GET'])
def get_ingrediente_aleatorio():
    """Retorna um ingrediente aleatório da lista."""
    ingrediente_escolhido = random.choice(ingredientes_sugestao)
    return jsonify({'ingrediente_do_dia': ingrediente_escolhido})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
