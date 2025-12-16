def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        
        a, b = b, a + b
        for y in c:
            print(a, y, end=" ")

c = ["C", "D", "E", "F", "G", "A", "B"]

# Exemplo: Gerar os primeiros 10 números da sequência
f = int(input("Quantos números você quer imprimir?"))
fibonacci(f)