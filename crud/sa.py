import json


def salvar_dados(dados):
    with open("dados.json", "a") as f:
        json.dump(dados, f, indent=4)

def tarefa(tarefa):
    with open("tarefa.json", "a") as f:
        json.dump(tarefa, f, indent=4)



def login_check(user, senha):
    with open("dados.json", "r") as f:
        dados = json.load(f)

    if user in dados["usuario"] and senha in dados["usuario"]["senha"]:
        return True

