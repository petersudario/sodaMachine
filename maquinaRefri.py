# Declaração de moedas na máquina
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
) = (50, 30, 30, 30, 20, 20, 10, 10, 10)

# Declaração de valor das moedas/cédulas
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

# extra Declaração para adicionar mais dinheiro na máquina.
(

    add_cinco_centavos,
    add_dez_centavos,
    add_vinte_centavos,
    add_cinq_centavos,
    add_um_real,
    add_dois_reais,
    add_cinco_reais,
    add_dez_reais,
    add_vinte_reais,

) = (0, 0, 0, 0, 0, 0, 0, 0, 0)

# declaração para criar a variável do troco
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

# criação da variável para a escolha de seleção de usuário
comando = ""

# declaração para a soma das notas do pagamento
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

# declaração dos preços dos produtos
(

    preco_cocalata,
    preco_Fanta,
    preco_guarlata,
    preco_suco,
    preco_coca600,
    preco_guar600

) = (5.5, 5, 5, 4.25, 7.75, 6)

# extra declaração do estoque da máquina
(

    estoque_CocaLata,
    estoque_Fanta,
    estoque_GuarLata,
    estoque_Suco,
    estoque_Coca600,
    estoque_Guar600

) = (15, 15, 15, 5, 5, 5)

# extra declaração de unidades de produtos vendidos
(

    qntd_cocalata_vendido,
    qntd_guarlata_vendido,
    qntd_fanta_vendido,
    qntd_suco_vendido,
    qntd_coca600_vendido,
    qntd_guar600_vendido

) = (0, 0, 0, 0, 0, 0)

# extra declaração de Dinheiro vendido
(

    total_vendido_dinheiro,
    total_vendido_cartao,
    total_tudo

) = (0, 0, 0)

# Início do código
while comando != "SAIR":
    comando = int(
        input(
            "\n Selecione o usuário (Digite o número):\n [1] Consumidor\n [2] Administrador \nou digite [SAIR] para cancelar sua escolha: "
        )
    )

    # Seleção do usuário
    if comando == 1:
        validando_produto = False
        while validando_produto != True:
            produto_selecionado = int(
                input(
                    f"\n Lista de produtos: \n [1]. Coca-Cola Lata : R${preco_cocalata} \n [2] Guaraná lata : R${preco_guarlata} \n [3] Fanta laranja lata : R${preco_Fanta} \n [4] Suco Prats : R${preco_suco} \n [5] Coca 600 Ml : R${preco_coca600} \n [6] Guaraná 600 ml : R${preco_guar600} \n [7] Cancelar a ação. \n Selecione o produto: ")
            )

            # seleção coca lata
            if produto_selecionado == 1 and estoque_CocaLata != 0:
                metodo_pagamento = int(
                    input(
                        "Qual o método de pagamento? (Digite o número) \n [1].Dinheiro \n [2].Cartão de débito/crédito "
                    )
                )

                # Pagamento em dinheiro
                if metodo_pagamento == 1:
                    validando_moeda = False
                    while validando_moeda != True:
                        pagamento = float(
                            input(
                                f"Por favor, insira suas moedas individualmete até pagar o preço requerido. \n Preço a pagar: R${preco_cocalata}:  "
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

                                # Pagamento inserido é igual ao preço do produto
                                if pagamento == preco_cocalata:

                                    print(" \n Compra finalizada. Volte sempre!")

                                    estoque_CocaLata = estoque_CocaLata - 1
                                    total_tudo = total_tudo + preco_cocalata
                                    total_vendido_dinheiro = total_vendido_dinheiro + preco_cocalata
                                    processo_pagamento = True
                                    validando_produto = True
                                    validando_moeda = True

                                # pagamento inserido é maior que o preço do produto
                                elif pagamento > preco_cocalata:
                                    troco = pagamento - preco_cocalata

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

                                    while troco >= vinte_reais and qntd_vinte_reais > 0:
                                        troco_vinte_reais += 1
                                        troco -= vinte_reais
                                        qntd_vinte_reais -= 1

                                    while troco >= dez_reais and qntd_dez_reais > 0:
                                        troco_dez_reais += 1
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
                                    print("Produto sendo entrege... \nObrigado e volte sempre!")

                                    # extra Diminui uma lata do estoque
                                    # extra aumenta o quanto foi vendido hoje.
                                    # extra aumenta a quantidade vendida
                                    estoque_CocaLata = estoque_CocaLata - 1
                                    qntd_cocalata_vendido = qntd_cocalata_vendido + 1
                                    total_tudo = total_tudo + preco_cocalata
                                    total_vendido_dinheiro = total_vendido_dinheiro + preco_cocalata
                                    processo_pagamento = True
                                    validando_produto = True
                                    validando_moeda = True

                                    if qntd_cinco_centavos == 0 or qntd_dez_centavos == 0 or qntd_vinte_centavos == 0 or qntd_vinte_centavos == 0 or qntd_cinq_centavos == 0 or qntd_um_real == 0 or qntd_dois_reais == 0 or qntd_cinco_reais == 0 or qntd_dez_reais == 0 or qntd_vinte_reais == 0:
                                        print(
                                            ' \n Não será possivel fazer a compra. O depósito de moedas e cédulas da máquina está vazio. Devolvendo moedas....')

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
                                    validando_moeda = True

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
                                                " \n Compra cancelada. Moedas devolvidas. Volte sempre."
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
                                            "\n Pagamento invalido. Moeda ou cédula não reconhecida. "
                                        )
                        else:
                            print(
                                "\n Pagamento invalido. Moeda ou cédula não reconhecida. Valor máximo aceito: R$20.00."
                            )


                # extra pagamento com cartão
                elif metodo_pagamento == 2:

                    validando_cartao = True

                    while validando_cartao != False:

                        # seleção de débito ou crédito
                        tipo_cartao = int(
                            input(
                                "\n Selecione o tipo de cartão (Digite o número):\n [1] Débito\n [2] Crédito"
                            )
                        )

                        if tipo_cartao == 1 or tipo_cartao == 2:
                            print(
                                f" \n Valor a pagar: R${preco_cocalata:.2f}\n"
                            )

                            cartao_inserido = True

                            while cartao_inserido != False:
                                validando_insercao = int(
                                    input(
                                        "\n Insira seu cartão.  (Digite [1] para simular inserção)"
                                    )
                                )

                                if validando_insercao == 1:
                                    input("\n Digite sua senha: ")

                                    print("\n Realizando transação....")

                                    retirar_cartao = False

                                    while retirar_cartao != True:

                                        retirada = int(
                                            input(
                                                "\n Retire o cartão. (Digite [1] para simular retirada)"
                                            )
                                        )

                                        if retirada == 1:
                                            retirar_cartao = True

                                            cartao_inserido = False

                                    print(
                                        "\n Pagamento realizado. Liberando produto. Tenha um bom dia!"
                                    )
                                    estoque_CocaLata = estoque_CocaLata - 1
                                    qntd_cocalata_vendido = qntd_cocalata_vendido + 1
                                    total_tudo = total_tudo + preco_cocalata
                                    total_vendido_cartao = total_vendido_cartao + preco_cocalata
                                    processo_pagamento = True
                                    validando_produto = True
                                    validando_moeda = True

                                else:
                                    print(" \n Erro. Re-insira o cartão.")

                            validando_cartao = False

                            validando_produto = True

                        else:
                            print(" \n Seleção inválida, tente novamente.")

                else:
                    print(" \n Seleção inválida, tente")

            # extra selecão do guaraná
            elif produto_selecionado == 2 and estoque_GuarLata != 0:
                metodo_pagamento = int(
                    input(
                        "Qual o método de pagamento? (Digite o número) \n [1].Dinheiro \n [2].Cartão de débito/crédito "
                    )
                )

                # Pagamento em dinheiro
                if metodo_pagamento == 1:
                    validando_moeda = False
                    while validando_moeda != True:
                        pagamento = float(
                            input(
                                f"Por favor, insira suas moedas individualmete até pagar o preço requerido. \n  Preço a se pagar: R${preco_guarlata}:  "
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

                                # Pagamento inserido é igual ao preço do produto
                                if pagamento == preco_guarlata:

                                    print(" \n Compra finalizada. Volte sempre!")

                                    # extra Diminui uma lata do estoque
                                    # extra aumenta o quanto foi vendido hoje.
                                    # extra aumenta a quantidade vendida
                                    estoque_GuarLata = estoque_GuarLata - 1
                                    total_tudo = total_tudo + preco_guarlata
                                    total_vendido_dinheiro = total_vendido_dinheiro + preco_guarlata
                                    processo_pagamento = True
                                    validando_produto = True
                                    validando_moeda = True

                                # pagamento inserido é maior que o preço do produto
                                elif pagamento > preco_cocalata:
                                    troco = pagamento - preco_guarlata

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

                                    while troco >= vinte_reais and qntd_vinte_reais > 0:
                                        troco_vinte_reais += 1
                                        troco -= vinte_reais
                                        qntd_vinte_reais -= 1

                                    while troco >= dez_reais and qntd_dez_reais > 0:
                                        troco_dez_reais += 1
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
                                    print("Produto sendo entrege... \nObrigado e volte sempre!")

                                    # extra Diminui uma lata do estoque
                                    # extra aumenta o quanto foi vendido hoje.
                                    # extra aumenta a quantidade vendida
                                    estoque_GuarLata - 1
                                    qntd_cocalata_vendido + 1
                                    total_tudo + preco_guarlata
                                    total_vendido_dinheiro + preco_guarlata
                                    processo_pagamento = True
                                    validando_produto = True
                                    validando_moeda = True

                                    if qntd_cinco_centavos == 0 or qntd_dez_centavos == 0 or qntd_vinte_centavos == 0 or qntd_vinte_centavos == 0 or qntd_cinq_centavos == 0 or qntd_um_real == 0 or qntd_dois_reais == 0 or qntd_cinco_reais == 0 or qntd_dez_reais == 0 or qntd_vinte_reais == 0:
                                        print(
                                            ' \n Não será possivel fazer a compra. O depósito de moedas e cédulas da máquina está vazio. Devolvendo moedas....')

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
                                    validando_moeda = True

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
                                                " \n Compra cancelada. Moedas devolvidas. Volte sempre."
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
                                            "\n Pagamento invalido. Moeda ou cédula não reconhecida. "
                                        )
                        else:
                            print(
                                "\n Pagamento invalido. Moeda ou cédula não reconhecida. Valor máximo aceito: R$20.00."
                            )


                # funcionalidade extra de cartão
                elif metodo_pagamento == 2:

                    validando_cartao = True

                    while validando_cartao != False:

                        # seleção de débito ou crédito
                        tipo_cartao = int(
                            input(
                                "\n Selecione o tipo de cartão (Digite o número):\n [1] Débito\n [2] Crédito"
                            )
                        )

                        if tipo_cartao == 1 or tipo_cartao == 2:
                            print(
                                f" \n Valor a pagar: R${preco_guarlata:.2f}\n"
                            )

                            cartao_inserido = True

                            while cartao_inserido != False:
                                validando_insercao = int(
                                    input(
                                        "\n Insira seu cartão.  (Digite [1] para simular inserção)"
                                    )
                                )

                                if validando_insercao == 1:
                                    input("\n Digite sua senha: ")

                                    print("\n Realizando transação....")

                                    retirar_cartao = False

                                    while retirar_cartao != True:

                                        retirada = int(
                                            input(
                                                "\n Retire o cartão. (Digite [1] para simular retirada)"
                                            )
                                        )

                                        if retirada == 1:
                                            retirar_cartao = True

                                            cartao_inserido = False

                                    print(
                                        "\n Pagamento realizado. Liberando produto. Tenha um bom dia!"
                                    )

                                    # extra Diminui uma lata do estoque
                                    # extra aumenta o quanto foi vendido hoje.
                                    # extra aumenta a quantidade vendida
                                    estoque_GuarLata = estoque_GuarLata - 1
                                    qntd_cocalata_vendido = qntd_guarlata_vendido + 1
                                    total_tudo = total_tudo + preco_guarlata
                                    total_vendido_dinheiro = preco_guarlata + total_vendido_dinheiro
                                    processo_pagamento = True
                                    validando_produto = True
                                    validando_moeda = True

                                else:
                                    print(" \n Erro. Re-insira o cartão.")

                            validando_cartao = False

                            validando_produto = True

                        else:
                            print(" \n Seleção inválida, tente novamente.")
                else:
                    print(" \n Seleção inválida, tente novamente")

            # Seleção Fanta laranja
            elif produto_selecionado == 3 and estoque_Fanta != 0:
                metodo_pagamento = int(
                    input(
                        "Qual o método de pagamento? (Digite o número) \n [1].Dinheiro \n [2].Cartão de débito/crédito "
                    )
                )

                # Pagamento em dinheiro
                if metodo_pagamento == 1:
                    validando_moeda = False
                    while validando_moeda != True:
                        pagamento = float(
                            input(
                                f"Por favor, insira suas moedas individualmete até pagar o preço requerido. \n  Preço a se pagar: R${preco_Fanta}:   "
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

                                # Pagamento inserido é igual ao preço do produto
                                if pagamento == preco_Fanta:

                                    print(" \n Compra finalizada. Volte sempre!")

                                    # extra Diminui uma lata do estoque
                                    # extra aumenta o quanto foi vendido hoje.
                                    # extra aumenta a quantidade vendida
                                    estoque_Fanta = estoque_Fanta - 1
                                    qntd_fanta_vendido = qntd_fanta_vendido + 1
                                    total_tudo = total_tudo + preco_Fanta
                                    total_vendido_dinheiro = total_vendido_dinheiro + preco_Fanta
                                    processo_pagamento = True
                                    validando_produto = True
                                    validando_moeda = True

                                # pagamento inserido é maior que o preço do produto
                                elif pagamento > preco_Fanta:
                                    troco = pagamento - preco_Fanta

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

                                    while troco >= vinte_reais and qntd_vinte_reais > 0:
                                        troco_vinte_reais += 1
                                        troco -= vinte_reais
                                        qntd_vinte_reais -= 1

                                    while troco >= dez_reais and qntd_dez_reais > 0:
                                        troco_dez_reais += 1
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
                                    print("Produto sendo entrege... \nObrigado e volte sempre!")

                                    # extra Diminui uma lata do estoque
                                    # extra aumenta o quanto foi vendido hoje.
                                    # extra aumenta a quantidade vendida
                                    estoque_Fanta = estoque_Fanta - 1
                                    qntd_fanta_vendido = qntd_fanta_vendido + 1
                                    total_tudo = total_tudo + preco_Fanta
                                    total_vendido_dinheiro = total_vendido_dinheiro + preco_Fanta
                                    processo_pagamento = True
                                    validando_produto = True
                                    validando_moeda = True

                                    if qntd_cinco_centavos == 0 or qntd_dez_centavos == 0 or qntd_vinte_centavos == 0 or qntd_vinte_centavos == 0 or qntd_cinq_centavos == 0 or qntd_um_real == 0 or qntd_dois_reais == 0 or qntd_cinco_reais == 0 or qntd_dez_reais == 0 or qntd_vinte_reais == 0:
                                        print(
                                            ' \n Não será possivel fazer a compra. O depósito de moedas e cédulas da máquina está vazio. Devolvendo moedas....')

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
                                    validando_moeda = True

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
                                                " \n Compra cancelada. Moedas devolvidas. Volte sempre."
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
                                            "\n Pagamento invalido. Moeda ou cédula não reconhecida. "
                                        )
                        else:
                            print(
                                "\n Pagamento invalido. Moeda ou cédula não reconhecida. Valor máximo aceito: R$20.00."
                            )


                # funcionalidade extra de cartão
                elif metodo_pagamento == 2:

                    validando_cartao = True

                    while validando_cartao != False:

                        # seleção de débito ou crédito
                        tipo_cartao = int(
                            input(
                                "\n Selecione o tipo de cartão (Digite o número):\n [1] Débito\n [2] Crédito"
                            )
                        )

                        if tipo_cartao == 1 or tipo_cartao == 2:
                            print(
                                f" \n Valor a pagar: R${preco_Fanta:.2f}\n"
                            )

                            cartao_inserido = True

                            while cartao_inserido != False:
                                validando_insercao = int(
                                    input(
                                        "\n Insira seu cartão.  (Digite [1] para simular inserção)"
                                    )
                                )

                                if validando_insercao == 1:
                                    input("\n Digite sua senha: ")

                                    print("\n Realizando transação....")

                                    retirar_cartao = False

                                    while retirar_cartao != True:

                                        retirada = int(
                                            input(
                                                "\n Retire o cartão. (Digite [1] para simular retirada)"
                                            )
                                        )

                                        if retirada == 1:
                                            retirar_cartao = True

                                            cartao_inserido = False

                                    print(
                                        "\n Pagamento realizado. Liberando produto. Tenha um bom dia!"
                                    )

                                    # extra Diminui uma lata do estoque
                                    # extra aumenta o quanto foi vendido hoje.
                                    # extra aumenta a quantidade vendida
                                    estoque_Fanta = estoque_Fanta - 1
                                    qntd_fanta_vendido = qntd_fanta_vendido + 1
                                    total_tudo = total_tudo + preco_Fanta
                                    total_vendido_cartao = total_vendido_cartao + preco_Fanta
                                    processo_pagamento = True
                                    validando_produto = True
                                    validando_moeda = True
                                else:
                                    print(" \n Erro. Re-insira o cartão.")

                            validando_cartao = False

                            validando_produto = True

                        else:
                            print(" \n Seleção inválida, tente novamente.")
                else:
                    print(" \n Seleção inválida, tente novamente")

                    # seleção suco prats
            elif produto_selecionado == 4 and estoque_Suco != 0:
                metodo_pagamento = int(
                    input(
                        "Qual o método de pagamento? (Digite o número) \n [1].Dinheiro \n [2].Cartão de débito/crédito "
                    )
                )

                # Pagamento em dinheiro
                if metodo_pagamento == 1:
                    validando_moeda = False
                    while validando_moeda != True:
                        pagamento = float(
                            input(
                                f"Por favor, insira suas moedas individualmete até pagar o preço requerido. \n Preço a se pagar: R${preco_suco}:  "
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

                                # Pagamento inserido é igual ao preço do produto
                                if pagamento == preco_cocalata:

                                    print(" \n Compra finalizada. Volte sempre!")

                                    # extra Diminui uma lata do estoque
                                    # extra aumenta o quanto foi vendido hoje.
                                    # extra aumenta a quantidade vendida
                                    estoque_Suco = estoque_Suco - 1
                                    qntd_suco_vendido = qntd_suco_vendido + 1
                                    total_vendido_dinheiro = total_vendido_dinheiro + preco_suco
                                    total_tudo = total_tudo + preco_suco
                                    processo_pagamento = True
                                    validando_produto = True
                                    validando_moeda = True

                                # pagamento inserido é maior que o preço do produto
                                elif pagamento > preco_cocalata:
                                    troco = pagamento - preco_suco

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

                                    while troco >= vinte_reais and qntd_vinte_reais > 0:
                                        troco_vinte_reais += 1
                                        troco -= vinte_reais
                                        qntd_vinte_reais -= 1

                                    while troco >= dez_reais and qntd_dez_reais > 0:
                                        troco_dez_reais += 1
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
                                    print("Produto sendo entrege... \nObrigado e volte sempre!")

                                    # extra Diminui uma lata do estoque
                                    # extra aumenta o quanto foi vendido hoje.
                                    # extra aumenta a quantidade vendida
                                    estoque_Suco = estoque_Suco - 1
                                    qntd_suco_vendido = qntd_suco_vendido + 1
                                    total_vendido_dinheiro = total_vendido_dinheiro + preco_suco
                                    total_tudo = total_tudo + preco_suco
                                    processo_pagamento = True
                                    validando_produto = True
                                    validando_moeda = True

                                    if qntd_cinco_centavos == 0 or qntd_dez_centavos == 0 or qntd_vinte_centavos == 0 or qntd_vinte_centavos == 0 or qntd_cinq_centavos == 0 or qntd_um_real == 0 or qntd_dois_reais == 0 or qntd_cinco_reais == 0 or qntd_dez_reais == 0 or qntd_vinte_reais == 0:
                                        print(
                                            ' \n Não será possivel fazer a compra. O depósito de moedas e cédulas da máquina está vazio. Devolvendo moedas....')

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
                                    validando_moeda = True

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
                                                " \n Compra cancelada. Moedas devolvidas. Volte sempre."
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
                                            "\n Pagamento invalido. Moeda ou cédula não reconhecida. "
                                        )
                        else:
                            print(
                                "\n Pagamento invalido. Moeda ou cédula não reconhecida. Valor máximo aceito: R$20.00."
                            )


                # extra maquina de cartão
                elif metodo_pagamento == 2:

                    validando_cartao = True

                    while validando_cartao != False:

                        # seleção de débito ou crédito
                        tipo_cartao = int(
                            input(
                                "\n Selecione o tipo de cartão (Digite o número):\n [1] Débito\n [2] Crédito"
                            )
                        )

                        if tipo_cartao == 1 or tipo_cartao == 2:
                            print(
                                f" \n Valor a pagar: R${preco_suco:.2f}\n"
                            )

                            cartao_inserido = True

                            while cartao_inserido != False:
                                validando_insercao = int(
                                    input(
                                        "\n Insira seu cartão.  (Digite [1] para simular inserção)"
                                    )
                                )

                                if validando_insercao == 1:
                                    input("\n Digite sua senha: ")

                                    print("\n Realizando transação....")

                                    retirar_cartao = False

                                    while retirar_cartao != True:

                                        retirada = int(
                                            input(
                                                "\n Retire o cartão. (Digite [1] para simular retirada)"
                                            )
                                        )

                                        if retirada == 1:
                                            retirar_cartao = True

                                            cartao_inserido = False

                                    print(
                                        "\n Pagamento realizado. Liberando produto. Tenha um bom dia!"
                                    )

                                    # extra Diminui uma lata do estoque
                                    # extra aumenta o quanto foi vendido hoje.
                                    # extra aumenta a quantidade vendida
                                    estoque_Suco = estoque_Suco - 1
                                    qntd_suco_vendido = qntd_suco_vendido + 1
                                    total_vendido_cartao = total_vendido_cartao + preco_suco
                                    total_tudo = total_tudo + preco_suco
                                    processo_pagamento = True
                                    validando_produto = True
                                    validando_moeda = True

                                else:
                                    print(" \n Erro. Re-insira o cartão.")

                            validando_cartao = False

                            validando_produto = True

                        else:
                            print(" \n Seleção inválida, tente novamente.")
                else:
                    print(" \n Seleção inválida, tente novamente")

            # seleção Coca 600 ml
            elif produto_selecionado == 5 and estoque_Coca600 != 0:
                metodo_pagamento = int(
                    input(
                        "Qual o método de pagamento? (Digite o número) \n [1].Dinheiro \n [2].Cartão de débito/crédito "
                    )
                )

                # Pagamento em dinheiro
                if metodo_pagamento == 1:
                    validando_moeda = False
                    while validando_moeda != True:
                        pagamento = float(
                            input(
                                f"Por favor, insira suas moedas individualmete até pagar o preço requerido. \n  PReço a se pagar: R${preco_coca600}:  "
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

                                # Pagamento inserido é igual ao preço do produto
                                if pagamento == preco_coca600:

                                    print(" \n Compra finalizada. Volte sempre!")

                                    # extra Diminui uma lata do estoque
                                    # extra aumenta o quanto foi vendido hoje.
                                    # extra aumenta a quantidade vendida
                                    estoque_Coca600 = estoque_Coca600 - 1
                                    qntd_coca600_vendido = qntd_coca600_vendido + 1
                                    total_tudo = total_tudo + preco_coca600
                                    total_vendido_dinheiro = total_vendido_dinheiro + preco_coca600
                                    processo_pagamento = True
                                    validando_produto = True
                                    validando_moeda = True

                                # pagamento inserido é maior que o preço do produto
                                elif pagamento > preco_coca600:
                                    troco = pagamento - preco_coca600

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

                                    while troco >= vinte_reais and qntd_vinte_reais > 0:
                                        troco_vinte_reais += 1
                                        troco -= vinte_reais
                                        qntd_vinte_reais -= 1

                                    while troco >= dez_reais and qntd_dez_reais > 0:
                                        troco_dez_reais += 1
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
                                    print("Produto sendo entrege... \nObrigado e volte sempre!")

                                    # extra Diminui uma lata do estoque
                                    # extra aumenta o quanto foi vendido hoje.
                                    # extra aumenta a quantidade vendida
                                    estoque_Coca600 = estoque_Coca600 - 1
                                    qntd_coca600_vendido = qntd_coca600_vendido + 1
                                    total_tudo = total_tudo + preco_coca600
                                    total_vendido_dinheiro = total_vendido_dinheiro + preco_coca600
                                    processo_pagamento = True
                                    validando_produto = True
                                    validando_moeda = True

                                    if qntd_cinco_centavos == 0 or qntd_dez_centavos == 0 or qntd_vinte_centavos == 0 or qntd_vinte_centavos == 0 or qntd_cinq_centavos == 0 or qntd_um_real == 0 or qntd_dois_reais == 0 or qntd_cinco_reais == 0 or qntd_dez_reais == 0 or qntd_vinte_reais == 0:
                                        print(
                                            ' \n Não será possivel fazer a compra. O depósito de moedas e cédulas da máquina está vazio. Devolvendo moedas....')

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
                                    validando_moeda = True

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
                                                " \n Compra cancelada. Moedas devolvidas. Volte sempre."
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
                                            "\n Pagamento invalido. Moeda ou cédula não reconhecida. "
                                        )
                        else:
                            print(
                                "\n Pagamento invalido. Moeda ou cédula não reconhecida. Valor máximo aceito: R$20.00."
                            )


                # extra de cartão
                elif metodo_pagamento == 2:

                    validando_cartao = True

                    while validando_cartao != False:

                        # seleção de débito ou crédito
                        tipo_cartao = int(
                            input(
                                "\n Selecione o tipo de cartão (Digite o número):\n [1] Débito\n [2] Crédito"
                            )
                        )

                        if tipo_cartao == 1 or tipo_cartao == 2:
                            print(
                                f" \n Valor a pagar: R${preco_coca600:.2f}\n"
                            )

                            cartao_inserido = True

                            while cartao_inserido != False:
                                validando_insercao = int(
                                    input(
                                        "\n Insira seu cartão.  (Digite [1] para simular inserção)"
                                    )
                                )

                                if validando_insercao == 1:
                                    input("\n Digite sua senha: ")

                                    print("\n Realizando transação....")

                                    retirar_cartao = False

                                    while retirar_cartao != True:

                                        retirada = int(
                                            input(
                                                "\n Retire o cartão. (Digite [1] para simular retirada)"
                                            )
                                        )

                                        if retirada == 1:
                                            retirar_cartao = True

                                            cartao_inserido = False

                                    print(
                                        "\n Pagamento realizado. Liberando produto. Tenha um bom dia!"
                                    )

                                    # extra Diminui uma lata do estoque
                                    # extra aumenta o quanto foi vendido hoje.
                                    # extra aumenta a quantidade vendida
                                    estoque_Coca600 = estoque_Coca600 - 1
                                    qntd_coca600_vendido = qntd_coca600_vendido + 1
                                    total_tudo = total_tudo + preco_coca600
                                    total_vendido_cartao = total_vendido_cartao + preco_coca600
                                    processo_pagamento = True
                                    validando_produto = True
                                    validando_moeda = True

                                else:
                                    print(" \n Erro. Re-insira o cartão.")

                            validando_cartao = False

                            validando_produto = True

                        else:
                            print(" \n Seleção inválida, tente novamente.")

                else:
                    print(" \n Seleção inválida, tente novamente")

            # seleção guaraná 600 ml

            elif produto_selecionado == 6 and estoque_Guar600 != 0:
                metodo_pagamento = int(
                    input(
                        "Qual o método de pagamento? (Digite o número) \n [1].Dinheiro \n [2].Cartão de débito/crédito "
                    )
                )

                # Pagamento em dinheiro
                if metodo_pagamento == 1:
                    validando_moeda = False
                    while validando_moeda != True:
                        pagamento = float(
                            input(
                                f"Por favor, insira suas moedas individualmete até pagar o preço requerido. \n  PReço a se pagar: R${preco_guar600}:  "
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

                                # Pagamento inserido é igual ao preço do produto
                                if pagamento == preco_guar600:

                                    print(" \n Compra finalizada. Volte sempre!")

                                    # extra Diminui uma lata do estoque
                                    # extra aumenta o quanto foi vendido hoje.
                                    # extra aumenta a quantidade vendida
                                    estoque_Guar600 = estoque_Guar600 - 1
                                    qntd_guar600_vendido = qntd_guar600_vendido + 1
                                    total_vendido_dinheiro = total_vendido_dinheiro + preco_guar600
                                    total_tudo = total_tudo + preco_guar600
                                    processo_pagamento = True
                                    validando_produto = True
                                    validando_moeda = True

                                # pagamento inserido é maior que o preço do produto
                                elif pagamento > preco_guar600:
                                    troco = pagamento - preco_guar600

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

                                    while troco >= vinte_reais and qntd_vinte_reais > 0:
                                        troco_vinte_reais += 1
                                        troco -= vinte_reais
                                        qntd_vinte_reais -= 1

                                    while troco >= dez_reais and qntd_dez_reais > 0:
                                        troco_dez_reais += 1
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
                                    print("Produto sendo entrege... \nObrigado e volte sempre!")

                                    # extra Diminui uma lata do estoque
                                    # extra aumenta o quanto foi vendido hoje.
                                    # extra aumenta a quantidade vendida
                                    estoque_Guar600 = estoque_Guar600 - 1
                                    qntd_guar600_vendido = qntd_guar600_vendido + 1
                                    total_vendido_dinheiro = total_vendido_dinheiro + preco_guar600
                                    total_tudo = total_tudo + preco_guar600
                                    processo_pagamento = True
                                    validando_produto = True
                                    validando_moeda = True

                                    if qntd_cinco_centavos == 0 or qntd_dez_centavos == 0 or qntd_vinte_centavos == 0 or qntd_vinte_centavos == 0 or qntd_cinq_centavos == 0 or qntd_um_real == 0 or qntd_dois_reais == 0 or qntd_cinco_reais == 0 or qntd_dez_reais == 0 or qntd_vinte_reais == 0:
                                        print(
                                            ' \n Não será possivel fazer a compra. O depósito de moedas e cédulas da máquina está vazio. Devolvendo moedas....')

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
                                    validando_moeda = True

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
                                                " \n Compra cancelada. Moedas devolvidas. Volte sempre."
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
                                            "\n Pagamento invalido. Moeda ou cédula não reconhecida. "
                                        )
                        else:
                            print(
                                "\n Pagamento invalido. Moeda ou cédula não reconhecida. Valor máximo aceito: R$20.00."
                            )


                # extra de cartão
                elif metodo_pagamento == 2:

                    validando_cartao = True

                    while validando_cartao != False:

                        # seleção de débito ou crédito
                        tipo_cartao = int(
                            input(
                                "\n Selecione o tipo de cartão (Digite o número):\n [1] Débito\n [2] Crédito"
                            )
                        )

                        if tipo_cartao == 1 or tipo_cartao == 2:
                            print(
                                f" \n Valor a pagar: R${preco_guar600:.2f}\n"
                            )

                            cartao_inserido = True

                            while cartao_inserido != False:
                                validando_insercao = int(
                                    input(
                                        "\n Insira seu cartão.  (Digite [1] para simular inserção)"
                                    )
                                )

                                if validando_insercao == 1:
                                    input("\n Digite sua senha: ")

                                    print("\n Realizando transação....")

                                    retirar_cartao = False

                                    while retirar_cartao != True:

                                        retirada = int(
                                            input(
                                                "\n Retire o cartão. (Digite [1] para simular retirada)"
                                            )
                                        )

                                        if retirada == 1:
                                            retirar_cartao = True

                                            cartao_inserido = False

                                    print(
                                        "\n Pagamento realizado. Liberando produto. Tenha um bom dia!"
                                    )

                                    # extra Diminui uma lata do estoque
                                    # extra aumenta o quanto foi vendido hoje.
                                    # extra aumenta a quantidade vendida
                                    estoque_Guar600 = estoque_Guar600 - 1
                                    qntd_guar600_vendido = qntd_guar600_vendido + 1
                                    total_vendido_cartao = total_vendido_cartao + preco_guar600
                                    total_tudo = total_tudo + preco_guar600
                                    processo_pagamento = True
                                    validando_produto = True
                                    validando_moeda = True

                                else:
                                    print(" \n Erro. Re-insira o cartão.")

                            validando_cartao = False

                            validando_produto = True

                        else:
                            print(" \n Seleção inválida, tente novamente.")

                else:
                    print(" \n Seleção inválida, tente novamente")

            elif produto_selecionado == 7:
                validando_produto = True

            else:
                print(
                    " \n Produto inexistente ou em falta na máquina. Por favor escolha outro produto."
                )

    # comando para entrar no Admin
    elif comando == 2:

        validando_senha = True

        while validando_senha != False:

            senha_admin = input("Digite a senha de administrador: ")

            if senha_admin == "moedeiroAdmin@123":

                # comando para acessar as funcionalidades do Admin
                comando = int(
                    input(
                        "\n O que gostaria de fazer? (Selecione o número) \n [1]. Checar Moedeiro\n [2] Adicionar mais dinheiro ao moedeiro \n [3] Checar o estoquer da máquina \n [4] Colocar mais produtos em estoque \n [5] Verificar o Número de vendas e o dinheiro ganho \n [6]. Sair\n"
                    )
                )

                # checar moedeiro
                if comando == 1:

                    print(
                        f" \n Existem: \n {qntd_cinco_centavos} moedas de 5 centavos\n {qntd_dez_centavos} moedas de 10 centavos \n {qntd_vinte_centavos} moedas de 25 centavos \n {qntd_cinq_centavos} moedas de 50 centavos\n {qntd_um_real} moedas de 1 real\n {qntd_dois_reais} cédulas de 2 reais\n {qntd_cinco_reais} cédulas de 5 reais\n {qntd_dez_reais} cédulas de 10 reais\n {qntd_vinte_reais} cédulas de 20 reais"
                    )

                # extra Adicionar ou retirar dinheiro no moeedeiro
                elif comando == 2:

                    # zerar a quantidade do add para que não adicione mais do que está adicionando agora
                    (
                        add_cinco_centavos,
                        add_dez_centavos,
                        add_vinte_centavos,
                        add_cinq_centavos,
                        add_um_real,
                        add_dois_reais,
                        add_cinco_reais,
                        add_dez_reais,
                        add_vinte_reais,

                    ) = (0, 0, 0, 0, 0, 0, 0, 0, 0)

                    add_vinte_reais = int(input(
                        "\n Quantas notas de R$20,00 você gostaria de adicionar? \n Coloque 0 para nâo adicionar nenhuma ou um número negativo para retirar: "))

                    if qntd_vinte_reais + add_vinte_reais <= 20:
                        qntd_vinte_reais = qntd_vinte_reais + add_vinte_reais
                    else:
                        print(
                            "Não foi possível adicionar essa quantidade na máquina, o máximo de notas de 20 reais é de 20")

                    add_dez_reais = int(input(
                        "\n Quantas notas de R$10,00 você gostaria de adicionar? \n Coloque 0 para nâo adicionar nenhuma ou um número negativo para retirar: "))

                    if qntd_dez_reais + add_dez_reais <= 20:
                        qntd_dez_reais = qntd_dez_reais + add_dez_reais
                    else:
                        print(
                            "Não foi possível adicionar essa quantidade na máquina, o máximo de notas de 10 reais é de 20")

                    add_cinco_reais = int(input(
                        "\n Quantas notas de R$5,00 Você gostaria de adicionar? \n Coloque 0 para nâo adicionar nenhuma ou um número negativo para retirar: "))

                    if qntd_cinco_reais + add_cinco_reais <= 30:
                        qntd_cinco_reais = qntd_dez_reais + add_dez_reais
                    else:
                        print(
                            "Não foi possível adicionar essa quantidade na máquina, o máximo de notas de 5 reais é de 30")

                    add_dois_reais = int(input(
                        "\n Quantas notas de R$2,00 você gostaria de adicionar? \n Coloque 0 para nâo adicionar nenhuma ou um número negativo para retirar: "))

                    if qntd_dois_reais + add_dois_reais <= 40:
                        qntd_dois_reais = qntd_dois_reais + add_dois_reais
                    else:
                        print(
                            "Não foi possível adicionar essa quantidade na máquina, o máximo de notas de 2 reais é de 40")

                    add_um_real = int(input(
                        "\n Quantas moedas de R$1,00 você gostaria de adicionar? \n Coloque 0 para nâo adicionar nenhuma ou um número negativo para retirar: "))

                    if qntd_um_real + add_um_real <= 100:
                        qntd_um_real = qntd_um_real + add_um_real
                    else:
                        print(
                            "Não foi possível adicionar essa quantidade na máquina, o máximo de moedas de 1 real é de 100")

                    add_cinco_centavos = int(input(
                        "\n Quantas moedas de R$0,50 você gostaria de adicionar? \n Coloque 0 para nâo adicionar nenhuma ou um número negativo para retirar: "))

                    if qntd_cinq_centavos + add_cinq_centavos <= 200:
                        qntd_cinq_centavos = qntd_cinq_centavos + add_cinq_centavos
                    else:
                        print(
                            "Não foi possível adicionar essa quantidade na máquina, o máximo de moedas de 50 centavos é de 100")

                    add_vinte_centavos = int(input(
                        "\n Quantas moedas de R$0,25 você gostaria de adicionar? \n Coloque 0 para nâo adicionar nenhuma ou um número negativo para retirar: "))

                    if qntd_vinte_centavos + add_vinte_centavos <= 200:
                        qntd_vinte_centavos = qntd_vinte_centavos + add_vinte_centavos
                    else:
                        print(
                            "Não foi possível adicionar essa quantidade na máquina, o máximo de moedas de 25 centavos é de 100")

                    add_dez_centavos = int(input(
                        "\n Quantas moedas de R$0,10 você gostaria de adicionar? \n Coloque 0 para nâo adicionar nenhuma ou um número negativo para retirar: "))

                    if qntd_vinte_centavos + add_vinte_centavos <= 100:
                        qntd_vinte_centavos = qntd_vinte_centavos + add_vinte_centavos
                    else:
                        print(
                            "Não foi possível adicionar essa quantidade na máquina, o máximo de moedas de 25 centavos é de 100")

                    add_cinco_centavos = int(input(
                        "\n Quantas moedas de R$0,05 você gostaria de adicionar? \n Coloque 0 para nâo adicionar nenhuma ou um número negativo para retirar: "))

                    if qntd_cinco_centavos + add_cinco_centavos <= 50:
                        qntd_cinq_centavos = qntd_cinco_centavos + add_cinco_centavos
                    else:
                        print(
                            "Não foi possível adicionar essa quantidade na máquina, o máximo de moedas de 5 centavos é de 50")

                    validando_senha = False

                elif comando == 3:

                    print(
                        f'\n Existe no momento na máquina: \n {estoque_CocaLata} latas de Coca-cola \n {estoque_GuarLata} latas de Guaraná Antártica \n {estoque_Fanta} Latas de Fanta Laranja \n {estoque_Suco} garrafas de suco Prats \n {estoque_Coca600} garrafas de 600 ml de Coca-Cola \n {estoque_Guar600} garrafas de 600 ml de Guaraná Antártica')

                elif comando == 4:

                    (

                        add_cocalata,
                        add_guarlata,
                        add_fantalata,
                        add_suco,
                        add_coca600,
                        add_guar600

                    ) = (0, 0, 0, 0, 0, 0)

                    add_cocalata = int(input(
                        "\n Quantas latas de Coca-Cola você está adicionando? \n Se não estiver adicionando nenhuma coloque 0. \n  "))

                    if estoque_CocaLata + add_cocalata <= 20:

                        estoque_CocaLata + add_cocalata

                    else:
                        print(
                            "Não foi possível adicionar adicionar essa quantidade, o máximo de Coca cola lata que é possível armazenar é 20.")

                    add_guarlata = int(input(
                        "\n Quantas latas de Guaraná você está adicionando? \n Se não estiver adicionando nenhuma coloque 0. \n  "))

                    if estoque_GuarLata + add_guarlata <= 20:

                        estoque_GuarLata + add_guarlata

                    else:

                        print(
                            "Não foi possível adicionar essa quantidade, o máximo de latas de Guaraná que é possível armazenar é 20")

                    add_fantalata = int(input(
                        "\n Quantas latas de Fanta laranja você está adicionando? \n Se não estiver adicionando nenhuma coloque 0. \n  "))

                    if estoque_Fanta + add_fantalata <= 20:

                        estoque_Fanta + add_fantalata
                    else:
                        print(
                            "Não foi possível adicionar essa quantidade, o máximo de latas de Fanta laranja que é possível adicionar é de 20 latas.")

                    add_suco = int(input(
                        "\n Quantas garrafas de suco Prats você está adicionando? \n Se não estiver adicionando nenhuma coloque 0. \n "))

                    if estoque_Suco + add_suco <= 10:
                        estoque_Suco + add_suco

                    else:
                        print(
                            "Não foi possível adicionar essa quantidade de garrafas de suco, o máximo de garrafas que é possível armazenar é de 10.")

                    add_coca600 = int(input(
                        "\n Quantas garrafas de 600 ml de Coca-Cola você está adicionando? \n Se não estiver adicionando nenhuma coloque 0. \n  "))

                    if estoque_Coca600 + add_coca600 <= 10:

                        estoque_Coca600 + add_coca600

                    else:
                        print(
                            "Não foi possível adicionar essa quantidade de garrafas de Coca-Cola, o máximo que é possível adicionar é de 10")

                    add_guar600 = int(input(
                        "\n Quantas garrafas de 600 ml de Guaraná Antartica você está adicionando? \n Se não estiver adicionando nenhuma coloque 0. \n "))

                    if estoque_Guar600 + add_guar600 <= 10:
                        estoque_Guar600 + add_guar600
                    else:
                        print(
                            "Não foi possível adicionar essa quantidade de garrafas de guaraná, o máximo que é possível armazenar é de 10")

                    validando_senha = False

                elif comando == 5:

                    if qntd_cocalata_vendido > 0:
                        print(f"Foram vendidas {qntd_cocalata_vendido} unidades de latas de Coca-cola")

                    if qntd_guarlata_vendido > 0:
                        print(f"Foram vendidas {qntd_guarlata_vendido} unidades de latas de Guaraná")

                    if qntd_fanta_vendido > 0:
                        print(f"Foram vendidas {qntd_fanta_vendido} unidades de latas de Fanta laranja")

                    if qntd_suco_vendido > 0:
                        print(f"Foram vendidas {qntd_suco_vendido} unidades de garrafas de suco Prats")

                    if qntd_coca600_vendido > 0:
                        print(f"Foram vendidas {qntd_coca600_vendido} unidades de garrafas de 600 ml de Coca-Cola")

                    if qntd_guar600_vendido > 0:
                        print(f"Foram vendidas {qntd_guar600_vendido} unidades de barrafs de 600 ml de Guaraná")

                    print(
                        f" \n O total vendido desde a abertura da máquina até agora é de: R${total_tudo} \n Foi vendido R${total_vendido_dinheiro} no dinheiro. \n Foi vendido: R${total_vendido_cartao} em cartões de débito e crédito.")

                elif comando == 6:

                    print("Saindo de usuário administrador...")

                    validando_senha = False
                else:
                    print("Comando inválido, tente novamente...")

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
