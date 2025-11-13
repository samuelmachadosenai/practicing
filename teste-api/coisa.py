import requests

dolar = 0
real = 0

while True:

    requisicao = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")

    dic_requisicao = requisicao.json()

    predolar = dic_requisicao['USDBRL']['bid']
    preeuro = dic_requisicao[]
    dolar = float(predolar)

    real = float(input("Digite a quantidade em reais:\n"))

    resultado = real * dolar
    break


print("{:.2f} Reais em Dólares é: {:.2f}".format(real, resultado))
