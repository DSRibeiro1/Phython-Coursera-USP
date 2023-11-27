decrescente = True
anterior = int(input("Digite o primeiro valor da sequência: "))

valor = 1
while valor !=0 and decrescente:
   valor = int(input("Digite o próximo valor da sequência: "))
   if valor > anterior:
      decrescente = False
   anterior = valor
if decrescente:
   print("A sequencia está em ordem decrescente")
else:
   print("Não está em ordem decrescente") 
