dia_mes = int(input("digite o dia do mes: "))
dia_semana = input("digite o dia da semana: ")
valor_produto = float(input("digite o valor do produto: "))
if dia_mes % 7 == 0:
    valor_produto = valor_produto*0.5
elif dia_semana == "sexta-feira":
    valor_produto = valor_produto * 0.75
else:
    valor_produto = valor_produto - dia_mes

print("{:.2f}".format(valor_produto))
if dia_semana == "sábado" or dia_semana == "domingo":
    print("Agradecemos a preferencia,tenha um otimo fim de semana!")
elif dia_semana == "segunda-feira":
    print("É um dia terrível,voce nao devia ter saido da cama!")
else:
    print("agradecemos a preferencia,tenha uma otima",dia_semana,"!")