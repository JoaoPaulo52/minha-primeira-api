from flask import Flask, jsonify, request

app = Flask(__name__)

# 1. Correção: Dicionários separados na lista
alunos = [
    {"id": 1, "nome": "Ana", "Curso": "Técnico em Informática"},
    {"id": 2, "nome": "Bruno", "Curso": "Técnico em Desenvolvimento"},
    {"id": 3, "nome": "Carla", "Curso": "Técnico em Informática"}
]

tarefas = [
    {"id": 1, "titulo": "Estudar Flask", "descricao": "Criar minha primeira API", "concluida": False},
    {"id": 2, "titulo": "Fazer Exercicios", "descricao": "Praticar endpoints da API", "concluida": False}
]


@app.route("/")
def home():
    return jsonify({"message": "Minha primeira API está funcionando", "status": "ok"})


@app.route("/health")
def health():
    return jsonify({"status": "ok", "message": "API está saudável e funcionando"})


# 2. Correção: Indentação ajustada para o escopo global
@app.route("/alunos")
def listar_alunos():
    return jsonify(alunos)


@app.route("/alunos/<int:id>")
def buscar_aluno(id):
    for aluno in alunos:
        if aluno["id"] == id:
            return jsonify(aluno)
    return jsonify({"erro": "Aluno não encontrado"}), 404


@app.route("/tarefas")
def listar_tarefas():
    return jsonify(tarefas)


@app.route("/tarefas/<int:id>")
def buscar_tarefa(id):
    for tarefa in tarefas:
        # 3. Correção: Usar 'tarefa' (singular) e não 'tarefas'
        if tarefa["id"] == id:
            return jsonify(tarefa)
    return jsonify({"erro": "Tarefa não encontrada"}), 404


# 4. Correção: Sintaxe do argumento corrigida para '='
@app.route("/tarefas", methods=["POST"])
def criar_tarefa():
    dados = request.get_json()

    # 5. Correção: Indentação do bloco interno da função
    nova_tarefa = {
        "id": len(tarefas) + 1,
        "titulo": dados["titulo"],
        "descricao": dados["descricao"],
        "concluida": False
    }

    tarefas.append(nova_tarefa)
    return jsonify(nova_tarefa), 201


if __name__ == "__main__":
    app.run(debug=True)