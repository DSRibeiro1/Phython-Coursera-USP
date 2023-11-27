input("Digite uma sequencia a de valores terminada com zero.")
soma = 0

valor = 1
while valor != 0:
	valor = int(input("Digite valor a ser somado: "))
	soma = soma + valor

print("A soma dos valores digitados é", soma)
