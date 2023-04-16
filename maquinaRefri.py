(
    qntd_fiveCents,
    qntd_tenCents,
    qntd_vinteCentavos,
    qntd_fiftyCents,
    qntd_umReal,
    qntd_doisReais,
    qntd_cincoReais,
    qntd_dezReais,
    qntd_vinteReais,
) = (0, 0, 0, 0, 0, 0, 0, 0, 0)
(
    fiveCents,
    tenCents,
    twentyCents,
    fiftyCents,
    umReal,
    doisReais,
    cincoReais,
    dezReais,
    vinteReais,
) = (0.05, 0.10, 0.25, 0.50, 1, 2, 5, 10, 20)

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
comando = ""

soma_dezReais = 0
soma_cincoReais = 0
soma_doisReais = 0
soma_umReal = 0
soma_fiftyCents = 0
soma_vinteCentavos = 0
soma_tenCents = 0
soma_fiveCents = 0
soma_vinteReais = 0


while comando != "SAIR":
    comando = int(
        input(
            "Selecione o usuário (Digite o número):\n [1] Consumidor\n [2] Administrador \nou digite [SAIR] para cancelar sua escolha: "
        )
    )

    if comando == 1:
        validandoProduto = False
        while validandoProduto != True:
            produtoSelecionado = int(
                input("Selecione um produto (Digite o número): \n  [1]. Coca-Cola ")
            )

            if produtoSelecionado == 1:
                metodoPagamento = int(
                    input(
                        "Qual o método de pagamento? (Digite o número) \n [1].Dinheiro \n [2].Cartão de débito/crédito "
                    )
                )

                if metodoPagamento == 1:
                    validacaoMoeda = False
                    while validacaoMoeda != True:
                        pagamento = float(
                            input(
                                "Por favor, insira suas moedas individualmete até pagar o preço requerido. \n"
                            )
                        )

                        if pagamento == fiveCents:
                            qntd_fiveCents += 1
                            soma_fiveCents += 1

                        elif pagamento == tenCents:
                            qntd_tenCents += 1
                            soma_tenCents += 1

                        elif pagamento == twentyCents:
                            qntd_vinteCentavos += 1
                            soma_vinteCentavos += 1

                        elif pagamento == fiftyCents:
                            qntd_fiftyCents += 1
                            soma_fiftyCents += 1

                        elif pagamento == umReal:
                            qntd_umReal += 1
                            soma_umReal += 1

                        elif pagamento == doisReais:
                            qntd_doisReais += 1
                            soma_doisReais += 1

                        elif pagamento == cincoReais:
                            qntd_cincoReais += 1
                            soma_cincoReais += 1

                        elif pagamento == dezReais:
                            qntd_dezReais += 1
                            soma_dezReais += 1

                        elif pagamento == vinteReais:
                            qntd_vinteReais += 1
                            soma_vinteReais += 1

                        if (
                            pagamento == fiveCents
                            or pagamento == tenCents
                            or pagamento == twentyCents
                            or pagamento == fiftyCents
                            or pagamento == umReal
                            or pagamento == doisReais
                            or pagamento == cincoReais
                            or pagamento == dezReais
                            or pagamento == vinteReais
                            or pagamento == 0
                        ):
                            processoPagamento = False

                            while processoPagamento != True:

                                moedaFaltante = pagamento

                                if pagamento == preco:

                                    print("Compra finalizada. Volte sempre!")

                                    processoPagamento = True

                                    validandoProduto = True

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

                                    if qntd_fiveCents == 0 or qntd_tenCents == 0 or qntd_vinteCentavos == 0 or qntd_vinteCentavos == 0 or qntd_fiftyCents == 0 or qntd_umReal == 0 or qntd_doisReais == 0 or qntd_cincoReais == 0 or qntd_dezReais == 0 or qntd_vinteReais == 0:
                                        print('Não será possivel fazer a compra. O depósito de moedas e cédulas da máquina está vazio. Devolvendo moedas....')

                                        qntd_vinteReais -= soma_vinteReais
                                        soma_vinteReais = 0
                                        qntd_dezReais -= soma_dezReais
                                        soma_dezReais = 0
                                        qntd_cincoReais -= soma_cincoReais
                                        soma_cincoReais = 0
                                        qntd_doisReais -= soma_doisReais
                                        soma_doisReais = 0
                                        qntd_umReal -= soma_umReal
                                        soma_umReal = 0
                                        qntd_fiftyCents -= soma_fiftyCents
                                        soma_fiftyCents = 0
                                        qntd_vinteCentavos -= soma_vinteCentavos
                                        soma_vinteCentavos = 0
                                        qntd_tenCents -= soma_tenCents
                                        soma_tenCents = 0
                                        qntd_fiveCents -= soma_fiveCents
                                        soma_fiveCents = 0

                                    processoPagamento = True
                                    validandoProduto = True

                                if processoPagamento != True:

                                    moedaFaltante = float(
                                        input(
                                            "Moedas ou cédulas faltantes. Por favor insira mais moedas ou cédulas ou aperte [0] para cancelar a compra. \nPagamento total no momento: R$"
                                            + str(pagamento)
                                            + "\n"
                                        )
                                    )

                                    if moedaFaltante == fiveCents:
                                        qntd_fiveCents += 1
                                        soma_fiveCents += 1

                                    elif moedaFaltante == tenCents:
                                        qntd_tenCents += 1
                                        soma_tenCents += 1

                                    elif moedaFaltante == twentyCents:
                                        qntd_vinteCentavos += 1
                                        soma_vinteCentavos += 1

                                    elif moedaFaltante == fiftyCents:
                                        qntd_fiftyCents += 1
                                        soma_fiftyCents += 1

                                    elif moedaFaltante == umReal:
                                        qntd_umReal += 1
                                        soma_umReal += 1

                                    elif moedaFaltante == doisReais:
                                        qntd_doisReais += 1
                                        soma_doisReais += 1

                                    elif moedaFaltante == cincoReais:
                                        qntd_cincoReais += 1
                                        soma_cincoReais += 1

                                    elif moedaFaltante == dezReais:
                                        qntd_dezReais += 1
                                        soma_dezReais += 1

                                    elif moedaFaltante == vinteReais:
                                        qntd_vinteReais += 1
                                        soma_vinteReais += 1

                                    if (
                                        moedaFaltante == fiveCents
                                        or moedaFaltante == tenCents
                                        or moedaFaltante == twentyCents
                                        or moedaFaltante == fiftyCents
                                        or moedaFaltante == umReal
                                        or moedaFaltante == doisReais
                                        or moedaFaltante == cincoReais
                                        or moedaFaltante == dezReais
                                        or moedaFaltante == vinteReais
                                        or moedaFaltante == 0
                                    ):
                                        if moedaFaltante == 0:
                                            print(
                                                "Compra cancelada. Moedas devolvidas. Volte sempre."
                                            )

                                            if soma_vinteReais > 0:
                                                qntd_vinteReais -= soma_vinteReais
                                                soma_vinteReais = 0

                                            if soma_dezReais > 0:
                                                qntd_dezReais -= soma_dezReais
                                                soma_dezReais = 0

                                            if soma_cincoReais > 0:
                                                qntd_cincoReais -= soma_cincoReais
                                                soma_cincoReais = 0

                                            if soma_doisReais > 0:
                                                qntd_doisReais -= soma_doisReais
                                                soma_doisReais = 0

                                            if soma_umReal > 0:
                                                qntd_umReal -= soma_umReal
                                                soma_umReal = 0

                                            if soma_fiftyCents > 0:
                                                qntd_fiftyCents -= soma_fiftyCents
                                                soma_fiftyCents = 0

                                            if soma_vinteCentavos > 0:
                                                qntd_vinteCentavos -= soma_vinteCentavos
                                                soma_vinteCentavos = 0

                                            if soma_tenCents > 0:
                                                qntd_tenCents -= soma_tenCents
                                                soma_tenCents = 0

                                            if soma_fiveCents > 0:
                                                qntd_fiveCents -= soma_fiveCents

                                                soma_fiveCents = 0

                                            processoPagamento = True
                                            validacaoMoeda = True
                                            validandoProduto = True

                                        else:
                                            pagamento += moedaFaltante

                                    else:
                                        print(
                                            "Pagamento invalido. Moeda ou cédula não reconhecida. "
                                        )
                        else:
                            print(
                                "Pagamento invalido. Moeda ou cédula não reconhecida. Valor máximo aceito: R$20.00."
                            )

                        if pagamento > preco:
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
                                print(f"Seu troco é de {troco20R} notas de R$20,00")
                            if troco10R > 0:
                                print(f"Seu troco é de {troco10R} notas de R$10,00")
                            if troco5R > 0:
                                print(f"Seu troco é de {troco5R} notas de R$5,00")
                            if troco2R > 0:
                                print(f"Seu troco é de {troco2R} notas de R$2,00")
                            if troco1R > 0:
                                print(f"Seu troco é de {troco1R} moedas de R$1,00")
                            if troco50C > 0:
                                print(f"Seu troco é de {troco50C} moedas de R$0,50")
                            if troco25C > 0:
                                print(f"Seu troco é de {troco25C} moedas de R$0,25")
                            if troco10C > 0:
                                print(f"Seu troco é de {troco10C} moedas de R$0,10")
                            if troco5C > 0:
                                print(f"Seu troco é de {troco5C} moedas de R$0,05")

                        validacaoMoeda = True

                # funcionalidade extra de cartão
                if metodoPagamento == 2:

                    validandoCartao = True

                    while validandoCartao != False:

                        tipoCartao = int(
                            input(
                                "Selecione o tipo de cartão (Digite o número):\n [1] Débito\n [2] Crédito"
                            )
                        )

                        if tipoCartao == 1 or tipoCartao == 2:
                            print(
                                f"Selecionado: Débito\n\nValor a pagar: R${preco:.2f}\n"
                            )

                            cartaoInserido = True

                            while cartaoInserido != False:
                                validarInsercao = int(
                                    input(
                                        "Insira seu cartão.  (Digite [1] para simular inserção)"
                                    )
                                )

                                if validarInsercao == 1:
                                    input("Digite sua senha: ")

                                    print("Realizando transação....")

                                    retirarCartao = False

                                    while retirarCartao != True:

                                        retirada = int(
                                            input(
                                                "Retire o cartão. (Digite [1] para simular retirada)"
                                            )
                                        )

                                        if retirada == 1:

                                            retirarCartao = True

                                            cartaoInserido = False

                                    print(
                                        "Pagamento realizado. Liberando produto. Tenha um bom dia!"
                                    )
                                else:
                                    print("Erro. Re-insira o cartão.")

                            validandoCartao = False

                            validandoProduto = True

                        else:
                            print("Seleção inválida, tente novamente.")

            else:
                print(
                    "Produto inexistente. Selecione os produtos que estão disponiveis!"
                )

    elif comando == 2:

        validacaoSenha = True

        while validacaoSenha != False:

            senhaAdmin = input("Digite a senha de administrador: ")

            if senhaAdmin == "moedeiroAdmin@123":

                comando = int(
                    input(
                        "O que gostaria de fazer? (Selecione o número) \n [1]. Checar Moedeiro\n [2]. Sair\n"
                    )
                )

                if comando == 1:

                    print(
                        f"Existem: \n {qntd_fiveCents} moedas de 5 centavos\n {qntd_tenCents} moedas de 10 centavos \n {qntd_vinteCentavos} moedas de 25 centavos \n {qntd_fiftyCents} moedas de 50 centavos\n {qntd_umReal} moedas de 1 real\n {qntd_doisReais} cédulas de 2 reais\n {qntd_cincoReais} cédulas de 5 reais\n {qntd_dezReais} cédulas de 10 reais\n {qntd_vinteReais} cédulas de 20 reais"
                    )

                    validacaoSenha = False

                else:

                    print("Saindo de usuário administrador...")

                    validacaoSenha = False

            elif senhaAdmin == "3":

                print("Cancelando login....")

                validacaoSenha = False

            else:
                print(
                    "Senha incorreta. Tente novamente ou digite [3] para cancelar o login."
                )

    else:
        print(
            "Seleção incorreta. Por favor selecione um dos usuários disponiveis na lista."
        )
