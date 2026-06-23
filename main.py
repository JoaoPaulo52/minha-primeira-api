from flask import Flask, jsonify

app = Flask(__name__)

alunos = [{'id': 1, 'nome': 'Ana', 'Curso': 'Técnico em Informática'}, {'id': 2, 'nome': 'Bruno', 'Curso': 'Técnico em Desenvolvimento'}, {'id': 3, 'nome': 'Carla', 'Curso': 'Técnico em Informática'}]
@app.route('/')
def home():
    return jsonify({'message': 'Minha primeira API está funcionando', 'status': 'ok'})

if __name__ == '__main__':
  app.run(debug=True)

@app.route('/health')
def health():
  return jsonify({'status': 'ok', 'message': 'API está saudável e funcionando'})

if __name__ == '__main__':
  app.run(debug=True)

  @app.route('/alunos')
  def listar_alunos():
   return jsonify(alunos)

  @app.route('/alunos/<int:id>')
  def buscar_aluno(id):
      for aluno in alunos:
          if aluno['id'] == id:
              return jsonify(aluno)

      return jsonify({'erro': 'Aluno não encontrado'}), 404


  if __name__ == '__main__':
      app.run(debug=True)

