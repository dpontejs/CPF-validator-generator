from random import randint
numero = str(randint(10000000000, 99999999999))
lista = list(range(10, 1, -1))
cpf3 = numero[:-2]

soma = 0
x = 0

for n in cpf3:
    soma += int(n) * int(lista[x])
    x += 1

primeiro_digitop = 11 - (soma % 11)

if 9 < primeiro_digitop:
    primeiro_digito = "0"
    cpf3 += primeiro_digito
else:
    cpf3 += str(primeiro_digitop)

lista2 = list(range(11, 1, -1))
soma2 = 0
x1 = 0

for n in cpf3:
    soma2 += int(n) * int(lista2[x1])
    x1 += 1

segundo_digitop = 11 - (soma2 % 11)

if 9 < segundo_digitop:
    segundo_digitop = "0"
    cpf3 += segundo_digitop
else:
    cpf3 += str(segundo_digitop)

print(cpf3)
