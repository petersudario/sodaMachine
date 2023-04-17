(
    qntd_cinco_centavos,
    qntd_dez_centavos,
    qntd_vinte_centavos,
    qntd_cinq_centavos,
    qntd_um_real,
    qntd_dois_reais,
    qntd_cinco_reais,
    qntd_dez_reais,
    qntd_vinte_reais,
) = (0, 0, 0, 0, 0, 0, 0, 0, 0)
(
    cinco_centavos,
    dez_centavos,
    vinte_centavos,
    cinq_centavos,
    um_real,
    dois_reais,
    cinco_reais,
    dez_reais,
    vinte_reais,

) = (0.05, 0.10, 0.25, 0.50, 1, 2, 5, 10, 20)

preco = 5.00
(
    troco_vinte_reais,
    troco_dez_reais,
    troco_cinco_reais,
    troco_dois_reais,
    troco_um_real,
    troco_cinq_centavos,
    troco_vinte_centavos,
    troco_dez_centavos,
    troco_cinco_centavos

) = (0, 0, 0, 0, 0, 0, 0, 0, 0)

comando = ""

(
    soma_vinte_reais,
    soma_dez_reais,
    soma_cinco_reais,
    soma_dois_reais,
    soma_um_real,
    soma_cinq_centavos,
    soma_vinte_centavos,
    soma_dez_centavos,
    soma_cinco_centavos,

) = (0, 0, 0, 0, 0, 0, 0, 0, 0)

while comando != "SAIR":
    comando = int(
        input(
            "Selecione o usuário (Digite o número):\n [1] Consumidor\n [2] Administrador \nou digite [SAIR] para cancelar sua escolha: "
        )
    )

    if comando == 1:
        validando_produto = False
        while validando_produto != True:
            produto_selecionado = int(
                input("Selecione um produto (Digite o número): \n  [1]. Coca-Cola ")
            )

            if produto_selecionado == 1:
                metodo_pagamento = int(
                    input(
                        "Qual o método de pagamento? (Digite o número) \n [1].Dinheiro \n [2].Cartão de débito/crédito "
                    )
                )

                if metodo_pagamento == 1:
                    validando_moeda = False
                    while validando_moeda != True:
                        pagamento = float(
                            input(
                                "Por favor, insira suas moedas individualmete até pagar o preço requerido. \n"
                            )
                        )

                        if pagamento == cinco_centavos:
                            qntd_cinco_centavos += 1
                            soma_cinco_centavos += 1

                        elif pagamento == dez_centavos:
                            qntd_dez_centavos += 1
                            soma_dez_centavos += 1

                        elif pagamento == vinte_centavos:
                            qntd_vinte_centavos += 1
                            soma_vinte_centavos += 1

                        elif pagamento == cinq_centavos:
                            qntd_cinq_centavos += 1
                            soma_cinq_centavos += 1

                        elif pagamento == um_real:
                            qntd_um_real += 1
                            soma_um_real += 1

                        elif pagamento == dois_reais:
                            qntd_dois_reais += 1
                            soma_dois_reais += 1

                        elif pagamento == cinco_reais:
                            qntd_cinco_reais += 1
                            soma_cinco_reais += 1

                        elif pagamento == dez_reais:
                            qntd_dez_reais += 1
                            soma_dez_reais += 1

                        elif pagamento == vinte_reais:
                            qntd_vinte_reais += 1
                            soma_vinte_reais += 1

                        if (
                            pagamento == cinco_centavos
                            or pagamento == dez_centavos
                            or pagamento == vinte_centavos
                            or pagamento == cinq_centavos
                            or pagamento == um_real
                            or pagamento == dois_reais
                            or pagamento == cinco_reais
                            or pagamento == dez_reais
                            or pagamento == vinte_reais
                            or pagamento == 0
                        ):
                            processo_pagamento = False

                            while processo_pagamento != True:

                                moeda_faltante = pagamento

                                if pagamento == preco:

                                    print("Compra finalizada. Volte sempre!")

                                    processo_pagamento = True

                                    validando_produto = True

                                elif pagamento > preco:
                                    troco = pagamento - preco

                                    while troco >= vinte_reais and qntd_vinte_reais > 0:
                                        troco_vinte_reais += 1
                                        troco -= vinte_reais
                                        qntd_vinte_reais -= 1

                                    while troco >= dez_reais and qntd_dez_reais > 0:
                                        troco_dez_centavos += 1
                                        troco -= dez_reais
                                        qntd_dez_reais -= 1

                                    while troco >= cinco_reais and qntd_cinco_reais > 0:
                                        troco_cinco_reais += 1
                                        troco -= cinco_reais
                                        qntd_cinco_reais -= 1

                                    while troco >= dois_reais and qntd_dois_reais > 0:
                                        troco_dois_reais += 1
                                        troco -= dois_reais
                                        qntd_dois_reais -= 1

                                    while troco >= um_real and qntd_um_real > 0:
                                        troco_um_real += 1
                                        troco -= um_real
                                        qntd_um_real -= 1

                                    while troco >= cinq_centavos and qntd_cinq_centavos > 0:
                                        troco_cinq_centavos += 1
                                        troco -= cinq_centavos
                                        qntd_cinq_centavos -= 1

                                    while troco >= vinte_centavos and qntd_vinte_centavos > 0:
                                        troco_vinte_centavos += 1
                                        troco -= vinte_centavos
                                        qntd_vinte_centavos -= 1

                                    while troco >= dez_centavos and qntd_dez_centavos > 0:
                                        troco_dez_centavos += 1
                                        troco -= dez_centavos
                                        qntd_dez_centavos -= 1

                                    while troco >= cinco_centavos and qntd_cinco_centavos > 0:
                                        troco_cinco_centavos += 1
                                        troco -= cinco_centavos
                                        qntd_cinco_centavos -= 1

                                    if qntd_cinco_centavos == 0 or qntd_dez_centavos == 0 or qntd_vinte_centavos == 0 or qntd_vinte_centavos == 0 or qntd_cinq_centavos == 0 or qntd_um_real == 0 or qntd_dois_reais == 0 or qntd_cinco_reais == 0 or qntd_dez_reais == 0 or qntd_vinte_reais == 0:
                                        print('Não será possivel fazer a compra. O depósito de moedas e cédulas da máquina está vazio. Devolvendo moedas....')

                                        qntd_vinte_reais -= soma_vinte_reais
                                        soma_vinte_reais = 0
                                        qntd_dez_reais -= soma_dez_reais
                                        soma_dez_reais = 0
                                        qntd_cinco_reais -= soma_cinco_reais
                                        soma_cinco_reais = 0
                                        qntd_dois_reais -= soma_dois_reais
                                        soma_dois_reais = 0
                                        qntd_um_real -= soma_um_real
                                        soma_um_real = 0
                                        qntd_cinq_centavos -= soma_cinq_centavos
                                        soma_cinq_centavos = 0
                                        qntd_vinte_centavos -= soma_vinte_centavos
                                        soma_vinte_centavos = 0
                                        qntd_dez_centavos -= soma_dez_centavos
                                        soma_dez_centavos = 0
                                        qntd_cinco_centavos -= soma_cinco_centavos
                                        soma_cinco_centavos = 0

                                    processo_pagamento = True
                                    validando_produto = True

                                if processo_pagamento != True:

                                    moeda_faltante = float(
                                        input(
                                            "Moedas ou cédulas faltantes. Por favor insira mais moedas ou cédulas ou aperte [0] para cancelar a compra. \nPagamento total no momento: R$"
                                            + str(pagamento)
                                            + "\n"
                                        )
                                    )

                                    if moeda_faltante == cinco_centavos:
                                        qntd_cinco_centavos += 1
                                        soma_cinco_centavos += 1

                                    elif moeda_faltante == dez_centavos:
                                        qntd_dez_centavos += 1
                                        soma_dez_centavos += 1

                                    elif moeda_faltante == vinte_centavos:
                                        qntd_vinte_centavos += 1
                                        soma_vinte_centavos += 1

                                    elif moeda_faltante == cinq_centavos:
                                        qntd_cinq_centavos += 1
                                        soma_cinq_centavos += 1

                                    elif moeda_faltante == um_real:
                                        qntd_um_real += 1
                                        soma_um_real += 1

                                    elif moeda_faltante == dois_reais:
                                        qntd_dois_reais += 1
                                        soma_dois_reais += 1

                                    elif moeda_faltante == cinco_reais:
                                        qntd_cinco_reais += 1
                                        soma_cinco_reais += 1

                                    elif moeda_faltante == dez_reais:
                                        qntd_dez_reais += 1
                                        soma_dez_reais += 1

                                    elif moeda_faltante == vinte_reais:
                                        qntd_vinte_reais += 1
                                        soma_vinte_reais += 1

                                    if (
                                        moeda_faltante == cinco_centavos
                                        or moeda_faltante == dez_centavos
                                        or moeda_faltante == vinte_centavos
                                        or moeda_faltante == cinq_centavos
                                        or moeda_faltante == um_real
                                        or moeda_faltante == dois_reais
                                        or moeda_faltante == cinco_reais
                                        or moeda_faltante == dez_reais
                                        or moeda_faltante == vinte_reais
                                        or moeda_faltante == 0
                                    ):
                                        if moeda_faltante == 0:
                                            print(
                                                "Compra cancelada. Moedas devolvidas. Volte sempre."
                                            )

                                            if soma_vinte_reais > 0:
                                                qntd_vinte_reais -= soma_vinte_reais
                                                soma_vinte_reais = 0

                                            if soma_dez_reais > 0:
                                                qntd_dez_reais -= soma_dez_reais
                                                soma_dez_reais = 0

                                            if soma_cinco_reais > 0:
                                                qntd_cinco_reais -= soma_cinco_reais
                                                soma_cinco_reais = 0

                                            if soma_dois_reais > 0:
                                                qntd_dois_reais -= soma_dois_reais
                                                soma_dois_reais = 0

                                            if soma_um_real > 0:
                                                qntd_um_real -= soma_um_real
                                                soma_um_real = 0

                                            if soma_cinq_centavos > 0:
                                                qntd_cinq_centavos -= soma_cinq_centavos
                                                soma_cinq_centavos = 0

                                            if soma_vinte_centavos > 0:
                                                qntd_vinte_centavos -= soma_vinte_centavos
                                                soma_vinte_centavos = 0

                                            if soma_dez_centavos > 0:
                                                qntd_dez_centavos -= soma_dez_centavos
                                                soma_dez_centavos = 0

                                            if soma_cinco_centavos > 0:
                                                qntd_cinco_centavos -= soma_cinco_centavos

                                                soma_cinco_centavos = 0

                                            processo_pagamento = True
                                            validando_moeda = True
                                            validando_produto = True

                                        else:
                                            pagamento += moeda_faltante

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

                            while troco >= vinte_reais and qntd_vinte_reais > 0:
                                troco_vinte_reais += 1
                                troco -= vinte_reais
                                qntd_vinte_reais -= 1

                            while troco >= dez_reais and qntd_dez_reais > 0:
                                troco_dez_centavos += 1
                                troco -= dez_reais
                                qntd_dez_reais -= 1

                            while troco >= cinco_reais and qntd_cinco_reais > 0:
                                troco_cinco_reais += 1
                                troco -= cinco_reais
                                qntd_cinco_reais -= 1

                            while troco >= dois_reais and qntd_dois_reais > 0:
                                troco_dois_reais += 1
                                troco -= dois_reais
                                qntd_dois_reais -= 1

                            while troco >= um_real and qntd_um_real > 0:
                                troco_um_real += 1
                                troco -= um_real
                                qntd_um_real -= 1

                            while troco >= cinq_centavos and qntd_cinq_centavos > 0:
                                troco_cinq_centavos += 1
                                troco -= cinq_centavos
                                qntd_cinq_centavos -= 1

                            while troco >= vinte_centavos and qntd_vinte_centavos > 0:
                                troco_vinte_centavos += 1
                                troco -= vinte_centavos
                                qntd_vinte_centavos -= 1

                            while troco >= dez_centavos and qntd_dez_centavos > 0:
                                troco_dez_centavos += 1
                                troco -= dez_centavos
                                qntd_dez_centavos -= 1

                            while troco >= cinco_centavos and qntd_cinco_centavos > 0:
                                troco_cinco_centavos += 1
                                troco -= cinco_centavos
                                qntd_cinco_centavos -= 1

                            if troco_vinte_reais > 0:
                                print(f"Seu troco é de {troco_vinte_reais} notas de R$20,00")
                            if troco_dez_reais > 0:
                                print(f"Seu troco é de {troco_dez_reais} notas de R$10,00")
                            if troco_cinco_reais > 0:
                                print(f"Seu troco é de {troco_cinco_reais} notas de R$5,00")
                            if troco_dois_reais > 0:
                                print(f"Seu troco é de {troco_dois_reais} notas de R$2,00")
                            if troco_um_real > 0:
                                print(f"Seu troco é de {troco_um_real} moedas de R$1,00")
                            if troco_cinq_centavos > 0:
                                print(f"Seu troco é de {troco_cinq_centavos} moedas de R$0,50")
                            if troco_vinte_centavos > 0:
                                print(f"Seu troco é de {troco_vinte_centavos} moedas de R$0,25")
                            if troco_dez_centavos > 0:
                                print(f"Seu troco é de {troco_dez_centavos} moedas de R$0,10")
                            if troco_cinco_centavos > 0:
                                print(f"Seu troco é de {troco_cinco_centavos} moedas de R$0,05")

                        validando_moeda = True

                # funcionalidade extra de cartão
                if metodo_pagamento == 2:

                    validando_cartao = True

                    while validando_cartao != False:

                        tipo_cartao = int(
                            input(
                                "Selecione o tipo de cartão (Digite o número):\n [1] Débito\n [2] Crédito"
                            )
                        )

                        if tipo_cartao == 1 or tipo_cartao == 2:
                            print(
                                f"Selecionado: Débito\n\nValor a pagar: R${preco:.2f}\n"
                            )

                            cartao_inserido = True

                            while cartao_inserido != False:
                                validando_insercao = int(
                                    input(
                                        "Insira seu cartão.  (Digite [1] para simular inserção)"
                                    )
                                )

                                if validando_insercao == 1:
                                    input("Digite sua senha: ")

                                    print("Realizando transação....")

                                    retirar_cartao = False

                                    while retirar_cartao != True:

                                        retirada = int(
                                            input(
                                                "Retire o cartão. (Digite [1] para simular retirada)"
                                            )
                                        )

                                        if retirada == 1:

                                            retirar_cartao = True

                                            cartao_inserido = False

                                    print(
                                        "Pagamento realizado. Liberando produto. Tenha um bom dia!"
                                    )
                                else:
                                    print("Erro. Re-insira o cartão.")

                            validando_cartao = False

                            validando_produto = True

                        else:
                            print("Seleção inválida, tente novamente.")

            else:
                print(
                    "Produto inexistente. Selecione os produtos que estão disponiveis!"
                )

    elif comando == 2:

        validando_senha = True

        while validando_senha != False:

            senha_admin = input("Digite a senha de administrador: ")

            if senha_admin == "moedeiroAdmin@123":

                comando = int(
                    input(
                        "O que gostaria de fazer? (Selecione o número) \n [1]. Checar Moedeiro\n [2]. Sair\n"
                    )
                )

                if comando == 1:

                    print(
                        f"Existem: \n {qntd_cinco_centavos} moedas de 5 centavos\n {qntd_dez_centavos} moedas de 10 centavos \n {qntd_vinte_centavos} moedas de 25 centavos \n {qntd_cinq_centavos} moedas de 50 centavos\n {qntd_um_real} moedas de 1 real\n {qntd_dois_reais} cédulas de 2 reais\n {qntd_cinco_reais} cédulas de 5 reais\n {qntd_dez_reais} cédulas de 10 reais\n {qntd_vinte_reais} cédulas de 20 reais"
                    )

                    validando_senha = False

                else:

                    print("Saindo de usuário administrador...")

                    validando_senha = False

            elif senha_admin == "3":

                print("Cancelando login....")

                validando_senha = False

            else:
                print(
                    "Senha incorreta. Tente novamente ou digite [3] para cancelar o login."
                )

    else:
        print(
            "Seleção incorreta. Por favor selecione um dos usuários disponiveis na lista."
        )
