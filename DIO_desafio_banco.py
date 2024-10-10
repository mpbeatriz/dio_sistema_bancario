menu = '''Sistema bancário

1. Depositar;
2. Sacar;
3. Extrato;
4. Sair.

Digite sua opção: '''

saldo = 0
cont_saque = 0
extrato = ''

while True:
    opcao = input(menu)

    if opcao == '1':
        valor = float(input("Digite o valor a ser depositado: "))
        if valor <= 0:
            print("Valor incorreto! O valor precisa ser positivo.")
        else:
            saldo += valor
            extrato += f'\nDepósito: R${valor:.2f}'

    if opcao == '2':
        if cont_saque >= 3:
            print("Limite de saques atingido.")
        else:
            valor_saque = float(input("Digite o valor do saque:"))
            while valor_saque > 500.0:
                print("Valor maior do que o limite! Digite outro valor:")
                valor_saque = float(input("Digite o valor do saque:"))
            if valor_saque > saldo:
                print("Saque indisponível. Saldo insuficiente.")
            else:
                print("Valor sacado com sucesso.")
                cont_saque +=1
                saldo -= valor_saque
                extrato += f'\nSaque: R${valor_saque:.2f}'
            
                
    if opcao == '3':
        if extrato == '':
            print('Não foram realizadas movimentações.')
        else:
            print(extrato, f'\nSaldo da conta: R${saldo:.2f}')
            
    if opcao == '4':
        break