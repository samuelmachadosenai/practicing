import json


def salvar_dados(dados):
    with open("dados.json", "a") as f:
        json.dump(dados, f, indent=4)