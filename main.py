from flask import Flask, jsonify, request

app = Flask(__name__)

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
        if tarefa["id"] == id:
            return jsonify(tarefa)
    return jsonify({"erro": "Tarefa não encontrada"}), 404


@app.route("/tarefas", methods=["POST"])
def criar_tarefa():
    dados = request.get_json()

    nova_tarefa = {
        "id": len(tarefas) + 1,
        "titulo": dados.get("titulo", "Sem título"),
        "descricao": dados.get("descricao", ""),
        "concluida": False
    }

    tarefas.append(nova_tarefa)
    return jsonify(nova_tarefa), 201


@app.route("/alunos", methods=["POST"])
def criar_aluno():
    dados = request.get_json()

    if not dados:
        return jsonify({"Erro": "Nenhum dado foi enviado."}), 400

    if "nome" not in dados or "Curso" not in dados:
        return jsonify({"Erro": "Os campos 'nome' e 'Curso' são obrigatórios."}), 400

    nova_aluno = {
        "id": len(alunos) + 1,
        "nome": dados["nome"],
        "Curso": dados["Curso"]
    }

    alunos.append(nova_aluno)
    return jsonify(nova_aluno), 201


@app.route("/tarefas/<int:id>", methods=["PUT"])
def atualizar_tarefa(id):
    dados = request.get_json()

    campos_obrigatorios = ["titulo", "descricao", "concluida"]

    for campo in campos_obrigatorios:
        if campo not in dados:
            return jsonify({"erro": f"Campo {campo} é obrigatório"}), 400

    for tarefa in tarefas:
        if tarefa["id"] == id:
            tarefa["titulo"] = dados["titulo"]
            tarefa["descricao"] = dados["descricao"]
            tarefa["concluida"] = dados["concluida"]

            return jsonify(tarefa), 201

    return jsonify({"erro": "Não encontrado"}), 404


@app.route("/alunos/<int:id>", methods=["PUT"])
def atualizar_aluno(id):
    dados_alunos = request.get_json()

    campos_obrigatorios_alunos = ["nome", "Curso"]

    for campo in campos_obrigatorios_alunos:
        if campo not in dados_alunos:
            return jsonify({"erro": f"Campo {campo} é obrigatório"}), 400

    for aluno in alunos:
        if aluno["id"] == id:
            aluno["nome"] = dados_alunos["nome"]
            aluno["Curso"] = dados_alunos["Curso"]

            return jsonify(aluno), 201

    return jsonify({"erro": "ID aluno não encontrado"}), 404


# Nova rota PATCH (vinda das imagens ...at 21.04.35 (1).jpeg e (2).jpeg)
@app.route("/tarefas/<int:id>", methods=["PATCH"])
def atualizar_campo_tarefas(id):
    dados_tarefas = request.get_json()

    for tarefa in tarefas:
        if tarefa["id"] == id:
            # Atualiza apenas os campos fornecidos, caso contrário mantém o original
            tarefa["titulo"] = dados_tarefas.get("titulo", tarefa["titulo"])
            tarefa["descricao"] = dados_tarefas.get("descricao", tarefa["descricao"])
            tarefa["concluida"] = dados_tarefas.get("concluida", tarefa["concluida"])

            return jsonify(tarefa), 201

    return jsonify({"erro": "ID tarefa não encontrado"}), 404


# Nova rota DELETE (vinda das imagens ...at 21.04.35.jpeg e (3).jpeg)
@app.route("/tarefas/<int:id>", methods=["DELETE"])
def excluir_tarefas(id):
    for tarefa in tarefas:
        if tarefa["id"] == id:
            tarefas.remove(tarefa)
            return jsonify({"mensagem": "Tarefa removida com sucesso"}), 200

    return jsonify({"erro": "ID tarefa não encontrado"}), 404


if __name__ == "__main__":
    app.run(debug=True)