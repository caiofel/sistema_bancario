menu = """

[d] depositar
[s] sacar 
[e] extrato 
[q] sair 

=> """

saldo = 0
limite = 500
extrato = ""
limite_saques = 3
quantidade_saques = 0

while True:
    opcao = input(menu)

    if opcao == "d":
      valor = float(input("Informe o valor do depósito: "))
      
      if valor > 0:
          saldo += valor
          extrato += f"Deposito: R$ {valor:.2f}\n"


    elif opcao == "s":
      valor = float(input("Informe o valor do saque: "))
      
      excedeu_saldo = valor > saldo
      
      excedeu_limite = valor > limite
      
      excedeu_saques = quantidade_saques >= limite_saques
      
      if excedeu_saldo:
          print("Operação falhou! Você não tem saldo suficiente, seu saldo é: ", saldo)
          
      elif excedeu_limite:
          print("Operação falhou! O valor do saque excedeu o limite.\nSeu limite é: ", limite)
      
      elif excedeu_saques:
          print("Operação falhou! Número máximo de saques excedido.\nSeu limite saque é: ", limite_saques)
      
      elif valor > 0:
          saldo -= valor
          extrato += f"Saque: R$ {valor:.2f}\n"
          quantidade_saques += 1
          
      else:
          print("Operação falhou! O valor informado é inválido.")

    elif opcao == "e":
      print("\n============== extrato ===============")
      print("Não foram realizadas movimentações." if not extrato else extrato)
      print(f"\nSaldo: R$ {saldo:.2f}")
      print("======================================")
    
    elif opcao == "q":
        break

    else:
        print ("operação nao realizada, por favor selecione novamente a operação desejada.")