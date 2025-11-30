import r
import random
# import json
import os



def cls():
   os.system("cls")

def formatar(cpf):
  #  '146.564.549-74"
  um = cpf[0:3]
  dois = cpf[3:6]
  tres = cpf[6:9]



def cpf_checker(cpf_str):

    # código de neandertal do caralhooooo

    while True:
        cpf_str = cpf_str.strip()
        cpf_str = cpf_str.replace(".", "")
        cpf_str = cpf_str.replace("-", "")

        quant = len(cpf_str)
        #123234345
        # lista = []
        cont = 0

        if quant < 11 or quant > 11 or cpf_str.isalpha == True:
            return False
        
        else:
            while True:
                n1 = int(cpf_str[0])
                n2 = int(cpf_str[1])
                n3 = int(cpf_str[2])
                n4 = int(cpf_str[3])
                n5 = int(cpf_str[4])
                n6 = int(cpf_str[5])
                n7 = int(cpf_str[6])
                n8 = int(cpf_str[7])
                n9 = int(cpf_str[8])

                n1 *= 1
                n2 *= 2
                n3 *= 3
                n4 *= 4
                n5 *= 5
                n6 *= 6
                n7 *= 7
                n8 *= 8
                n9 *= 9

                numero_final = n1 + n2 + n3 + n4 + n5 + n6 + n7 + n8 + n9
                num_top = numero_final % 11

                num_a = str(num_top)

                num_b = num_a[-1]

                strong = cpf_str + num_b

                # __________________________________________

                nn1 = int(strong[0])
                nn2 = int(strong[1])
                nn3 = int(strong[2])
                nn4 = int(strong[3])
                nn5 = int(strong[4])
                nn6 = int(strong[5])
                nn7 = int(strong[6])
                nn8 = int(strong[7])
                nn9 = int(strong[8])
                nn10 = int(strong[9])

                nn1 *= 0
                nn2 *= 1
                nn3 *= 2
                nn4 *= 3
                nn5 *= 4
                nn6 *= 5
                nn7 *= 6
                nn8 *= 7
                nn9 *= 8
                nn10 *= 9

                numero_final2 = nn1 + nn2 + nn3 + nn4 + nn5 + nn6 + nn7 + nn8 + nn9 + nn10

                num_top2 = numero_final2 % 11

                num_a2 = str(num_top2)

                num_b2 = num_a2[-1]
                break

            # verificador1 = num_b
            # verificador2 = num_b2
            

            if num_b == cpf_str[-2] and num_b2 == cpf_str[-1]:
                return True
            else:
                return False

def cadastrar():
  while True:
    cls()
    cpf = str(input("Digite seu CPF:\n"))

    a = cpf_checker(cpf)

    if a == False:
      cls()
      print("\nInválido. Tente novamente.\n")
      continue

    cls()
    nome = str(input("Digite seu nome:\n"))
    cls()
    data_nasc = int(input("Digite sua data de nascimento:\n"))
    cls()
    break

  return cpf, nome, data_nasc

def ver():
  cls()
  s = r.getid()
  s = int(s)
  n = 1





  print("-"*10, "Alunos", "-"*10)
  while n < s:
    print(f"Aluno:{n}")
    n += 1

  esc = int(input("\nSelecione o número do aluno para ver detalhes: "))

  if esc > s or esc < 1:
     print("\nO aluno não existe.")
  else:
    esc = str(esc)
    cu = "Aluno:" + esc
    print(cu)
    print("Informações: ", r.getaluno(cu))





# Traceback (most recent call last):
#   File "C:\Users\samuel\OneDrive\Documentos\GitHub\practicing\redis\a.py", line 55, in <module>
#     a = f()
#         ^^^
#   File "C:\Users\samuel\OneDrive\Documentos\GitHub\practicing\redis\a.py", line 44, in f
#     b += 1
# TypeError: unsupported operand type(s) for +=: 'NoneType' and 'int'
# def menu():




def gen():
    m = random.randint(1000, 9000)
    return m

matricula = gen()





global cpf

# menu()
while True:


  
  print("1. Cadastrar aluno")
  print("2. Ver alunos")
  e = int(input())

  if e  == 1:
      break
  elif e == 2:
      ver()
  else:
      continue
  
cpf, nome, data_nasc = cadastrar()


data = {"Matricula": matricula, "CPF": cpf, "Nome": nome, "DataNascimento": data_nasc}





data = str(data)

# ____________________________________________________

def zee():
  zero = 1
  return zero

def f():
  b = r.getid()
  b = int(b)
  b += 1
  return b

# def ff():
#   c = 1
#   r.save_id(c)
#   return 
z = r.getid()

if z == None:
  a = zee()
else:
  a = f()

r.save_id(a)


a = str(a)

lista = ['Aluno', a]

aluno_id = ':'.join(lista)

# r.indice(aluno_id)

r.banco(aluno_id, data)

# qtd = r.qtd()



# print(aluno_id)


print("Matrícula concluída.")



      

# print('Quantidade de alunos: \n', s)




# def salvar(m):
#     with open("matricula.json", "a") as f:
#       json.dump(m, f, indent=4)

# salvar(matricula)





