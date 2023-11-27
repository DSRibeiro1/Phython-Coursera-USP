meuCartao = int(input("Digite o número do seu cartão de crédito: "))

cartaoLido = 1
encontreiMeuCartaoNaLista = False

while cartaoLido!=0 and not encontreiMeuCartaoNaLista:
   cartaoLido = int(input("Digite número do próximo cartão: "))
   if cartaoLido == meuCartao:
       encontreiMeuCartaoNaLista = True

if encontreiMeuCartaoNaLista:
   print("Encontrei meu cartão")
else:
   print("Não Encontrei meu cartão")   
   
