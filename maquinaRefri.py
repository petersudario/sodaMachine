qntd_fiveCents, qntd_tenCents, qntd_vinteCentavos, qntd_fiftyCents, qntd_umReal, qntd_doisReais,  qntd_cincoReais, qntd_dezReais, qntd_vinteReais = 0, 0, 0, 0, 0, 0, 0, 0, 0
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
                        troco = pagamento - preco
                        print('Compra finalizada, volte sempre!\n Seu troco: R$', troco)
                        validacaoMoeda = True

