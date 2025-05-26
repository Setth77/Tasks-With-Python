while True:
    comando = str(input("digite uma opção(ou q pra sair): "))
    if comando.lower() == 'q':
        print("encerrando... ")
        break
    else:
        while True:
          print(f"voce digitou: '{comando}'")
          break