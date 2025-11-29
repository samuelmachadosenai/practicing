import r
import random
# import json



while True:
  cpf = str(input("Digite seu CPF:\n"))
  nome = str(input("Digite seu nome:\n"))
  data_nasc = int(input("Digite sua data de nascimento:\n"))

  break




# Traceback (most recent call last):
#   File "C:\Users\samuel\OneDrive\Documentos\GitHub\practicing\redis\a.py", line 55, in <module>
#     a = f()
#         ^^^
#   File "C:\Users\samuel\OneDrive\Documentos\GitHub\practicing\redis\a.py", line 44, in f
#     b += 1
# TypeError: unsupported operand type(s) for +=: 'NoneType' and 'int'





def gen():
    m = random.randint(1000, 9000)
    return m

matricula = gen()


data = {
    "matricula": cpf,
    "nome": nome,
    "data_de_nascimento": data_nasc
  }



data = str(data)

def zee():
  zero = 0
  r.save_id(zero)

def f():
  b = r.getid()
  b = int(b)
  b += 1
  r.save_id(b)
  return b

# def ff():
#   c = 1
#   r.save_id(c)
#   return 

if r.getid() == None:
  a = zee()
else:
  a = f()


a = f()
a = str(a)

lista = ['Aluno', a]

aluno_id = ':'.join(lista)

r.banco(aluno_id, data)


print("Matrícula concluída.")


# def salvar(m):
#     with open("matricula.json", "a") as f:
#       json.dump(m, f, indent=4)

# salvar(matricula)