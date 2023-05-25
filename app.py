from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
import mysql.connector


DATABASE_URI =  {
    'host': 'localhost',
    'user': 'root',
    'password': 'Abcd321',
    'database': 'db_ac4'
}

connection = mysql.connector.connect(**DATABASE_URI)

cursor = connection.cursor()

app = Flask(__name__)
CORS(app)


@app.route('/first', methods=['GET'])
def get_first():
    query = "SELECT * FROM first"
    cursor.execute(query)
    resultado = cursor.fetchall()
    return jsonify(resultado)


@app.route('/first', methods=['POST'])
@cross_origin()
def post_first():
    nome = request.json.get('nome')
    sobrenome = request.json.get('sobrenome')
    numero = request.json.get('numero')

    query = "INSERT INTO first (nome, sobrenome, numero) VALUES (%s, %s, %s)"
    values = (nome, sobrenome, numero)
    
    cursor.execute(query, values)
    connection.commit()
    return 'Dados adicionados com sucesso'


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)