print("Cardápio:")
print("1 - Pastel (R$12)")
print("2 - Açaí (R$11)")
print("3 - X-Burger (R$15)")
print("Digite 'q' para sair e ver o total.\n")

cardapio = {
    '1': ('pastel', 12),
    '2': ('acai', 11),
    '3': ('xburger', 15)
}
nome, preco = cardapio['1']

total = 0 

while True:
    comando = input("digite uma opção entre 1-3: ").lower()
    
    if comando == 'q':
        print(f"encerrando... total do pedido: R${total}")
        break
    if comando in cardapio:
        nome, preco = cardapio[comando]
        total += preco
        print(f"voce pediu '{comando}' por R${preco}. ")
    else:
        print("opcao invalida, tente novamente.")
