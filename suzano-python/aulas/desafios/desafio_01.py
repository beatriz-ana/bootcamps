menu = """

        MENU

    [1] Depositar
    [2] Sacar
    [3] Extrato
    [0] Sair
=> """ 

saldo = 0
limite = 500
extrato = []
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    
    opcao = int(input(menu))

    if opcao == 1:
        deposito = float(input('Valor do depósito: '))
        if deposito > 0:
            saldo+=deposito
            extrato.append(f'Depósito: R$ {deposito:.2f}')
            print(f'Depósito de R$ {deposito:.2f} realizado com sucesso!')
        else:
            print('Erro: O valor do depósito deve ser positivo.')
        input("\nPressione Enter para continuar...")

    elif opcao == 2:
        if numero_saques < LIMITE_SAQUES:
            saque = float(input('Valor do saque: '))
            if saque> 0 and saque <= limite:
                if saldo>=saque:
                    saldo-=saque
                    extrato.append(f'Saque: R$ {saque:.2f}')
                    numero_saques += 1
                    print(f'Saque de R$ {saque:.2f} realizado com sucesso!')
                else:
                    print('Não é possivel sacar. Saldo insuficiente!')
            else:
                print(f'Erro: O saque deve ser positivo e até R$ {limite:.2f}.')
        else:
            print('Erro: Limite de 3 saques diários atingido.')
        input("\nPressione Enter para continuar...")

    elif opcao == 3:
        print('\n================ EXTRATO ================')

        if extrato:
            for transacao in extrato:
                print(transacao)
        else:
            print("Nenhuma movimentação realizada.")

        print(f'\nSaldo atual: R$ {saldo:.2f}')
        print("==========================================")
        input("\nPressione Enter para continuar...")

    elif opcao == 0:
        print('Encerrando o sistema...')
        break

    else:
        print('Operação Inválida, por favor selecione novamente a  operação desejada.')
        input("\nPressione Enter para continuar...")
   

