from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app) 
receitas = [
    {'id': 1, 'nome': 'Bolo de Chocolate', 'instrucoes': 'Misture tudo e asse.'},
    {'id': 2, 'nome': 'Mousse de Maracujá', 'instrucoes': 'Bata no liquidificador e gele.'},
    {'id': 3, 'nome': 'Pão de Queijo', 'instrucoes': 'Misture os ingredientes e leve ao forno.'}
]

@app.route('/receitas', methods=['GET'])
def get_todas_receitas():
    """Retorna a lista completa de receitas."""
    return jsonify(receitas)

@app.route('/receitas/<int:id_receita>', methods=['GET'])
def get_receita_por_id(id_receita):
    """Retorna uma receita específica pelo seu ID."""
    receita = next((r for r in receitas if r['id'] == id_receita), None)
    
    if receita:
        return jsonify(receita)
    else:
        return jsonify({'message': 'Receita não encontrada'}), 404

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
