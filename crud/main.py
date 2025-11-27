import defs as d
import sa

def cria():
    while True:

        while True:
            nome = str(input("Digite seu nome de usuário:\n"))
            senha = str(input("Digite sua senha:\n"))


            if d.name_checker(nome) == True:
                break
            else:
                continue

        data, horario = d.datahora()
        
        id, status = d.gerar_id()
    

        dados = {
            "usuario": {
                "nome": nome,
                "senha": senha,
                "id": id,
                "status": status,
                "data de criacao": data,
                "horario de criacao": horario
            }
        }

        sa.salvar_dados(dados)
        break

def t():
    while True:
        print("""1. Criar tarefa""")
        input()

        id_tarefa, status_tarefa = d.gerar_id()

        nome_tarefa = input("Digite o nome da tarefa:\n")
        data_tarefa = input("Digite a data da tarefa (apenas números):\n")
        desc = input("\nDigite a descrição da tarefa:\n")


        data_c, horario_c = d.datahora()

        tarefas = {
            "id do autor": id,
            "nome da tarefa": nome_tarefa,
            "descricao da tarefa": desc,
            "data para conclusao": data_tarefa,
            "status da tarefa": status_tarefa,
            "data de criacao": data_c,
            "horario de criacao": horario_c
        }

        sa.tarefa(tarefas)
        break

def login():
    while True:
        user = input("Digite seu nome de usuário:\n")
        senha = print("Digite sua senha:\n")
        sa.login_check(user, senha)
        break

login()

