"""""-------------------------- Questão 1 ---------------------

indice = 13
soma = 0
k = 0

while k < indice:
    k = k +1
    soma = soma + k

print(soma)

"Resposta = 91"

"""


""" --------------------------Questão 2 -----------------------
entrada = int(input("Entrada >"))
fib0 = int(0)
fib1 = int(1)

while fib1 < entrada:
    cache = fib1
    fib1 = fib1 + fib0
    fib0 = cache

if fib1 == entrada:
    print('Pertence')
else:
    print("Não pertence")

"""
"""--------------------- Questão 3 ---------------

1 - 9
2 - 128
3 - 49
4 - 100
5 - 13
6 - 200



"""
 
""" ---------------------- Questão 4 ---------------------
Bora resolver programando que é mais divertido :)

Percurso = 100mk
Carro = 110km/h que é igual à 1.833333333333333 km/m
Caminhão = 80km/h que é igual à 1.333333333333333 km/m

Resposta = O código abaixo executa a resposta, o resultado obtido é obtido diz que os carros se encontram mais próximos da cidade de franca

   --------------------- Código Questão 4 -----------------------
"""
"""
PercursoCarro = 0
PercursoCaminhão = 100
carro = 1.833333333333333
caminhão = 1.333333333333333
cont = 0
minuto = 0

while PercursoCarro < PercursoCaminhão:
    minuto += 1
    if cont < 10:        
        cont += 1
    else:
        PercursoCaminhão = PercursoCaminhão - caminhão
    
    PercursoCarro = PercursoCarro + carro

print('os carros se cruzaram entre os kilometros {:.2f}'.format(PercursoCarro), 'e {:.2f}'.format(PercursoCaminhão), "aos", minuto, "minutos")
if PercursoCarro > 50:
    print("Logo, se encontraram mais próximos da cidade de frança")
else: 
    print("Logo, se encontraram mais próximos da cidade de Ribeirão Preto")

"""
""" -------------------- Questão 5 --------------------------------------

Entrada = input("Entrda > ")
Saida = ("")
Tamanho = len(Entrada)
cont = 0
while len(Entrada) > cont:
    cont += 1
    Saida = Saida + (Entrada[Tamanho-cont])

print(Saida)

"""





