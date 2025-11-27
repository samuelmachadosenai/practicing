import defs as d
import sa

while True:


    nome = str(input("Digite seu nome de usuário:\n"))

    data, horario = d.datahora()

    id = d.gerar_id()

    dados = {
        nome: {
            "id": id,
            "data de criacao": data,
            "horario de criacao": horario
        }
    }

    sa.salvar_dados(dados)
    break