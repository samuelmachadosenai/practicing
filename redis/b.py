import r


a = r.getid()
print(a)

texto = """{b'info': b"{'matricula': 5221, 'nome': 'sssssssss', 'data_de_nascimento': 3333333333}"}"""



texto = str(texto.split("{", 2))

texto = str(texto.rsplit("}", 2))

print(texto)
