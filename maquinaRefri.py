qntd_fiveCents, qntd_tenCents, qntd_vinteCentavos, qntd_fiftyCents, qntd_umReal, qntd_doisReais,  qntd_cincoReais, qntd_dezReais, qntd_vinteReais = 50, 50, 50, 20, 20, 20, 20, 20, 20
fiveCents, tenCents, twentyCents, fiftyCents, umReal, doisReais,  cincoReais, dezReais, vinteReais = 0.05, 0.10, 0.25, 0.50, 1, 2, 5, 10, 20

preco = 5.50

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
                    pagamento = float(input('Por favor, insira suas moedas individualmete até pagar o preço requerido. \n'))

                    if pagamento == fiveCents or pagamento == tenCents or pagamento == twentyCents or pagamento == fiftyCents or pagamento == umReal or pagamento == doisReais or pagamento == cincoReais or pagamento == dezReais or pagamento == vinteReais:
                        while pagamento < preco:
                            moedaFaltante = pagamento
                            moedaFaltante = float(input(
                                'Moedas faltantes. Por favor insira mais moedas. \nPagamento total no momento: R$' + str(pagamento) + '\n'
                            ))
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
                        dinheiro = 0
                        valorTroco = 20
                        trocoUnit = True
                        while trocoUnit == True:
                            if pagamento > valorTroco:
                                pagamento -= vinteReais
                                dinheiro += 1
                            else:
                                print(f'Seu troco é de: {dinheiro} de R$ {valorTroco}')
                                if valorTroco == 20:
                                    valorTroco = 10
                                    qntd_vinteReais - dinheiro
                                elif valorTroco == 10:
                                    valorTroco = 5
                                    qntd_dezReais - dinheiro
                                elif valorTroco == 5:
                                    valorTroco  = 2
                                    qntd_cincoReais - dinheiro
                                elif valorTroco == 2:
                                    valorTroco == 1
                                    qntd_doisReais - dinheiro
                                elif valorTroco == 1:
                                    valorTroco = 0.5
                                    qntd_umReal - dinheiro
                                elif valorTroco == 0.5:
                                    valorTroco = 0.25
                                    qntd_fiftyCents - dinheiro
                                elif valorTroco == 0.25:
                                    valorTroco == 0.10
                                    qntd_fiftyCents - dinheiro
                                elif valorTroco == 0.10:
                                    valorTroco == 0.5
                                    qntd_tenCents - dinheiro
                                elif valorTroco == 0.5:
                                    qntd_fiveCents - dinheiro
                                if pagamento == 0:
                                   trocoUnit = False    
                                print('Produto sendo entrege... \n Obrigado e volte sempre!')
