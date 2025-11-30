import redis

r = redis.Redis(host='localhost', port=6379, db=0)

r.ping()

# r.set('cor', 'azul')

# r.set('nome', 'açucena')

def save_id(id):
    r.set('id_atual', id)

def getid():
    a = r.get('id_atual')
    return a


def banco(id, d):
    r.hset(id, 'info', d)
    # r.hset(id, 'cpf', d)
    # r.hset(id, 'endereco', d)
    # r.hset(id, 'info', d)

# def indice(aluno):
#     r.lpush("Alunos", aluno)
    

def qtd():
    a = r.keys("*")
    a = str(a)
    a = a.count("Aluno:")
    return a


# salvar o id no banco

# enquanto id menor q 1. faça isso

