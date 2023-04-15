qntd_fiveCents, qntd_tenCents, qntd_vinteCentavos, qntd_fiftyCents, qntd_umReal, qntd_doisReais, qntd_cincoReais, qntd_dezReais, qntd_vinteReais = 50, 50, 50, 20, 20, 20, 20, 20, 20
fiveCents, tenCents, twentyCents, fiftyCents, umReal, doisReais, cincoReais, dezReais, vinteReais = 0.05, 0.10, 0.25, 0.50, 1, 2, 5, 10, 20

preco = 5.50

troco20R = 0
troco10R = 0
troco5R = 0
troco2R = 0
troco1R = 0
troco50C = 0
troco25C = 0
troco10C = 0
troco5C = 0
comando = ''

while comando != 'SAIR':
    comando = int(input(
        'Selecione o usuário:\n[1] Consumidor\n[2] Administrador, \n ou digite [SAIR] para cancelar sua escolha: '
    ))

    if comando == 1:
        produtoSelecionado = int(input('Selecione um produto: \n [1]. Coca-Cola '))
        if produtoSelecionado == 1:
            metodoPagamento = int(input('Qual o método de pagamento? \n [1].Dinheiro \n [2].Cartão de débito/crédito '))
            if metodoPagamento == 1:
                validacaoMoeda = False
                while validacaoMoeda == False:
                    pagamento = float(
                        input('Por favor, insira suas moedas individualmete até pagar o preço requerido. \n'))
                    if pagamento == fiveCents:
                        qntd_fiveCents += 1
                    elif pagamento == tenCents:
                        qntd_tenCents += 1
                    elif pagamento == twentyCents:
                        qntd_vinteCentavos += 1
                    elif pagamento == fiftyCents:
                        qntd_fiftyCents += 1
                    elif pagamento == umReal:
                        qntd_umReal += 1
                    elif pagamento == cincoReais:
                        qntd_cincoReais += 1
                    elif pagamento == dezReais:
                        qntd_dezReais += 1
                    elif pagamento == vinteReais:
                        qntd_vinteReais += 1

                    if pagamento == fiveCents or pagamento == tenCents or pagamento == twentyCents or pagamento == fiftyCents or pagamento == umReal or pagamento == doisReais or pagamento == cincoReais or pagamento == dezReais or pagamento == vinteReais:
                        while pagamento < preco:
                            moedaFaltante = pagamento
                            moedaFaltante = float(input(
                                'Moedas faltantes. Por favor insira mais moedas. \nPagamento total no momento: R$' + str(
                                    pagamento) + '\n'
                            ))

                            if moedaFaltante == fiveCents:
                                qntd_fiveCents += 1
                            elif moedaFaltante == tenCents:
                                qntd_tenCents += 1
                            elif moedaFaltante == twentyCents:
                                qntd_vinteCentavos += 1
                            elif moedaFaltante == fiftyCents:
                                qntd_fiftyCents += 1
                            elif moedaFaltante == umReal:
                                qntd_umReal += 1
                            elif moedaFaltante == cincoReais:
                                qntd_cincoReais += 1
                            elif moedaFaltante == dezReais:
                                qntd_dezReais += 1
                            elif moedaFaltante == vinteReais:
                                qntd_vinteReais += 1


                            if moedaFaltante == fiveCents or moedaFaltante == tenCents or moedaFaltante == twentyCents or moedaFaltante == fiftyCents or moedaFaltante == umReal or moedaFaltante == doisReais or moedaFaltante == cincoReais or moedaFaltante == dezReais or moedaFaltante == vinteReais:
                                pagamento += moedaFaltante
                            else:
                                print('Pagamento invalido. Tente inserir moedas brasileiras válidas.')
                    else:
                        print('Pagamento invalido. Tente inserir moedas brasileiras válidas.')

                    if pagamento == preco:
                        print('Compra finalizada. Volte sempre!')
                        validacaoMoeda = True
                    elif pagamento > preco:
                        troco = pagamento - preco

                        while troco >= vinteReais and qntd_vinteReais > 0:
                            troco20R += 1
                            troco -= vinteReais
                            qntd_vinteReais -= 1

                        while troco >= dezReais and qntd_dezReais > 0:
                            troco10C += 1
                            troco -= dezReais
                            qntd_dezReais -= 1

                        while troco >= cincoReais and qntd_cincoReais > 0:
                            troco5R += 1
                            troco -= cincoReais
                            qntd_cincoReais -= 1

                        while troco >= doisReais and qntd_doisReais > 0:
                            troco2R += 1
                            troco -= doisReais
                            qntd_doisReais -= 1

                        while troco >= umReal and qntd_umReal > 0:
                            troco1R += 1
                            troco -= umReal
                            qntd_umReal -= 1

                        while troco >= fiftyCents and qntd_fiftyCents > 0:
                            troco50C += 1
                            troco -= fiftyCents
                            qntd_fiftyCents -= 1

                        while troco >= twentyCents and qntd_vinteCentavos > 0:
                            troco25C += 1
                            troco -= twentyCents
                            qntd_vinteCentavos -= 1

                        while troco >= tenCents and qntd_tenCents > 0:
                            troco10C += 1
                            troco -= tenCents
                            qntd_tenCents -= 1

                        while troco >= fiveCents and qntd_fiveCents > 0:
                            troco5C += 1
                            troco -= fiveCents
                            qntd_fiveCents -= 1
                    if troco20R > 0:
                        print(f'Seu troco é de {troco20R} notas de R$20,00')
                    if troco10R > 0:
                        print(f'Seu troco é de {troco10R} notas de R$10,00')
                    if troco5R > 0:
                        print(f'Seu troco é de {troco5R} notas de R$5,00')
                    if troco2R > 0:
                        print(f'Seu troco é de {troco2R} notas de R$2,00')
                    if troco1R > 0:
                        print(f'Seu troco é de {troco1R} moedas de R$1,00')
                    if troco50C > 0:
                        print(f'Seu troco é de {troco50C} moedas de R$0,50')
                    if troco25C > 0:
                        print(f'Seu troco é de {troco25C} moedas de R$0,25')
                    if troco10C > 0:
                        print(f'Seu troco é de {troco10C} moedas de R$0,10')
                    if troco5C > 0:
                        print(f'Seu troco é de {troco5C} moedas de R$0,05')

                    print('Produto sendo entrege... \n Obrigado e volte sempre!')
                    validacaoMoeda = True

    if comando == 2:
        senhaAdmin = input('Digite a senha de administrador: ')

        if senhaAdmin == "moedeiroAdmin@123":
            comando = int(input('O que gostaria de fazer? (Selecione o número) \n [1]. Checar Moedeiro\n [2]. Sair'))

            if comando == 1:
                print(
                    f'Existem: \n {qntd_fiveCents} moedas de 5 centavos\n {qntd_tenCents} moedas de 10 centavos \n {qntd_vinteCentavos} moedas de 25 centavos \n {qntd_fiftyCents} de 50 centavos\n {qntd_umReal} moedas de 1 real\n {qntd_doisReais} cédulas de 2 reais\n {qntd_cincoReais} cédulas de 5 reais\n {qntd_dezReais} cédulas de 10 reais\n {qntd_vinteReais} cédulas de 20 reais')
            else:
                print('Saindo de usuário administrador...')
        else:
            print('Senha incorreta. Voltando ao menu principal.')