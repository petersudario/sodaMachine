# Definição das variáveis globais de armazanamento de dinheiro
global preco

# Variáveis de estoque de refrigerante
est_coca = 1
est_pepsi = 1
est_uva = 1
est_guar = 1

# Variáveis de Estoque de moedas
qnt_dezreais = 0
qnt_cincoreais = 0
qnt_doisreais = 0
qnt_umreal = 0
qnt_cinqcent = 0
qnt_vintecent = 0
qnt_dezcent = 0
qnt_cincocent = 0
# senha do adm
senha_adm = 5040302010
# Soma do total vendido na máquina
totaldinheiro = 0
totalcartao = 0
totalpix = 0
# Listas gerais
moedeiro = []
pixtelefone = []
pixvalor = []
vendido_dinheiro = []
vendido_cartao = []
vendido_pix = []
devolve = []
# Quantidade e tipo de dinheiro que a máquina aceita
tipo_moedas = [0.05, 0.10, 0.25, 0.50, 1.00]
tipo_cedulas = [2.00, 5.00, 10.00]
comando = 0

def devolver_dinheiro():

    global qnt_dezreais, qnt_cincoreais, qnt_doisreais, qnt_umreal, qnt_cinqcent, qnt_vintecent, qnt_dezcent, qnt_cincocent, devolve

    while (len(devolve) > 0):
        if devolve[0] == 10:
            devolve.remove(10)
            qnt_dezreais -= 1
        elif devolve[0] == 5:
            devolve.remove(5)
            qnt_cincoreais -= 1
        elif devolve[0] == 2:
            devolve.remove(2)
            qnt_doisreais -= 1
        elif devolve[0] == 1:
            devolve.remove(1)
            qnt_umreal -= 11
        elif devolve[0] == 0.5:
            devolve.remove(0.5)
            qnt_cinqcent -= 1
        elif devolve[0] == 0.25:
            devolve.remove(0.25)
            qnt_vintecent -= 1
        elif devolve[0] == 0.1:
            devolve.remove(0.1)
            qnt_dezcent -= 1
        elif devolve[0] == 0.05:
            devolve.remove(0.05)
            qnt_cincocent -= 1

# Funcão para a máquina de cartão
def pag_cartao():
    global est_coca, est_pepsi, est_uva, est_guar, preco, totalcartao, selecao
    valcartao = True
    # Validação para a inserção do cartão na máquina.
    while valcartao != False:

        print("Valor a pagar: R$", preco)
        cartao = int(input("Selecione o tipo de cartão:\n [1] Crédito \n [2] Débito \n "))
        if (cartao == 1 or cartao == 2):
            input("Insira seu cartão. Digite qualquer tecla para simular a inserção. \n ")

            input("Digite sua senha: ")
            print("Realizando transação.")

            input("Retire seu cartão. Aperte qualquer tecla para simular a retirada.")

            if selecao == 1:
                est_coca -= 1
            if selecao == 2:
                est_pepsi -= 1
            if selecao == 3:
                est_uva -= 1
            if selecao == 4:
                est_guar -= 1
            print("Produto sndo entregue. Volte sempre.")
            vendido_cartao.append(preco)
            totalcartao += preco
            break

        else:
            print("Escolha inválida.")


# Função para verificar o quanto foi vendido em PIX

def verpix():
    if (len(pixtelefone) > 0):
        print("Foram vendidos: ", len(pixtelefone), "produtos no pix.")
        for x in range(len(pixtelefone)):
            print("Preço vendido: R$", pixvalor[x], "| Telefone do pix:", pixtelefone[x])
    else:
        print("Não foi vendido nada no pix.")


# Função de pagamento em PIX
def pag_pix():
    global est_coca, est_pepsi, est_uva, est_guar, escolha, totalpix, preco
    # Inserção de telefone para registro.
    telefone = int(input("Insira seu número de telefone: EX: 41992436675 \n Digite: "))
    # Inserção do telefone e do preço registrado para o PIX
    pixtelefone.append(telefone)
    pixvalor.append(preco)
    # Remoção de uma lata no estoque.
    if selecao == 1:
        est_coca -= 1
        escolha = 4
        totalpix += preco
    if selecao == 2:
        est_pepsi -= 1
        totalpix += preco
    if selecao == 3:
        escolha = 4
        est_uva -= 1
        totalpix += preco
    if selecao == 4:
        escolha = 4
        est_guar -= 1
        totalpix += preco

    print("Aguardando transferência...")
    print("Produto sendo entregue...")
    print("Produto entregue. Volte sempre.")


# Função de Adicionar moedas no moedeiro.
def contar_moeda(pagamento):
    global qnt_dezreais, qnt_cincoreais, qnt_doisreais, qnt_umreal, qnt_cinqcent, qnt_vintecent, qnt_dezcent, qnt_cincocent

    if pagamento == 0.05:
        qnt_cincocent += 1
    if pagamento == 0.10:
        qnt_dezcent += 1
    if pagamento == 0.25:
        qnt_vintecent += 1
    if pagamento == 0.50:
        qnt_cinqcent += 1
    if pagamento == 1:
        qnt_umreal += 1
    if pagamento == 2:
        qnt_doisreais += 1
    if pagamento == 5:
        qnt_cincoreais += 1
    if pagamento == 10:
        qnt_dezreais += 1


# função de Menu de escolha mostrada para o usuário
def estoque_produto(produto_lista):
    if produto_lista == "Coca-cola":
        if est_coca > 0:
            return " preço: 5,50 | Estoque: " + str(est_coca) + " unidades"
        return "| Esgotado(a)"
    if produto_lista == "Pepsi":
        if est_pepsi > 0:
            return " preço: 4,00 | Estoque: " + str(est_pepsi) + " unidades"
        return "| Esgotado(a)"
    if produto_lista == "Fanta Uva":
        if est_uva > 0:
            return " preço: 4,90 | Estoque: " + str(est_uva) + " unidades"
        return "| Esgotado(a)"
    if produto_lista == "Fanta Guaraná":
        if est_guar > 0:
            return " preço: 4,90 | Estoque: " + str(est_guar) + " unidades"
        return "| Esgotado(a)"


# Função de seleção do produto
def selecao_produto():
    produtos = ["Coca-cola", "Pepsi", "Fanta Uva", "Fanta Guaraná"]
    cont = 0

    for produto in produtos:
        quantidade = estoque_produto(produto)
        cont += 1
        print("[", cont, "] ", produto, quantidade)


# função para o pagamento em dinheiro do usuário
def pagamento_dinheiro(custo):
    global est_coca, est_pepsi, est_uva, est_guar, dinheiro_inserido, tipo_moedas, tipo_cedulas, selecao, totaldinheiro
    total_inserido = []
    pagado = 0

    dinheiro_inserido = float(input('Insira suas moedas (uma vez por vez): '))
    devolve.append(dinheiro_inserido)
    # Verificação se o dinheiro colocado é aceito.
    if (dinheiro_inserido in tipo_moedas or dinheiro_inserido in tipo_cedulas):
        pagado += dinheiro_inserido
        # Adição de moedas e dinheiro no moedeiro.
        contar_moeda(dinheiro_inserido)
        if pagado <= custo:
            while (pagado <= custo):

                if pagado > custo:
                    troco(pagado)

                if (pagado == custo):

                    if (selecao == 1):
                        est_coca -= 1
                        totaldinheiro += preco
                    if (selecao == 2):
                        est_pepsi -= 1
                        totaldinheiro += preco
                    if (selecao == 3):
                        est_uva -= 1
                        totaldinheiro += preco
                    if (selecao == 4):
                        est_guar = 1
                        totaldinheiro += preco

                    print("Contando dinheiro...")
                    print("Entregando produto...")
                    print("Produto entregue, Volte sempre...")

                    break

                dinheiro_faltante = float(
                    input("Dinheiro faltante. Insira mais moedas\nTotal pago até o momento: R$" + str(pagado) + "\n"))

                contar_moeda(dinheiro_faltante)
                devolve.append(dinheiro_faltante)

                if dinheiro_faltante in tipo_cedulas or dinheiro_faltante in tipo_moedas:
                    total_inserido.append(dinheiro_faltante)
                    pagado += dinheiro_faltante

        elif (pagado > custo):
            troco(pagado)
        
        if (pagado > custo):
            troco(pagado)

    else:

        print("Moeda ou cédula inválida, tente novamente")


# Função para quando o usuário escolhe o produto e vai para o pagamento.
def pagamento_produto(produto_selecionado):
    # Definição para uma variável global que será usada até o final do processo de compra.
    global preco

    escolha = 0

    if (produto_selecionado == 1):
        preco = 5.50
        # Escolha do método de pagamento.
        escolha = int(
            input("Qual a forma de pagamento? \n [1] Dinheiro \n [2] PIX \n [3] Cartão \n [4] Cancelar operação \n"))
        if (escolha == 1):
            pagamento_dinheiro(preco)
        elif (escolha == 2):
            pag_pix()
        elif (escolha == 3):
            pag_cartao()
        elif (escolha == 4):
            print("Operação cancelada.")
        else:
            print("Escolha inválida.")

    if (produto_selecionado == 2):
        preco = 4
        # Escolha do método de pagamento.
        escolha = int(
            input("Qual a forma de pagamento? \n [1] Dinheiro \n [2] PIX \n [3] Cartão \n [4] Cancelar operação \n"))
        if (escolha == 1):
            pagamento_dinheiro(preco)
        elif (escolha == 2):
            pag_pix()
        elif (escolha == 3):
            pag_cartao()
        else:
            print("Escolha inválida.")

    if (produto_selecionado == 3):
        preco = 4.9
        # Escolha do método de pagamento.
        escolha = int(
            input("Qual a forma de pagamento? \n [1] Dinheiro \n [2] PIX \n [3] Cartão \n [4] Cancelar operação \n"))
        if (escolha == 1):
            pagamento_dinheiro(preco)
        elif (escolha == 2):
            pag_pix()
        elif (escolha == 3):
            pag_cartao()
        else:
            print("Escolha inválida.")
    if (produto_selecionado == 4):
        preco = 4.9
        # Escolha do método de pagamento.
        escolha = int(
            input("Qual a forma de pagamento? \n [1] Dinheiro \n [2] PIX \n [3] Cartão \n [4] Cancelar operação \n"))
        if (escolha == 1):
            pagamento_dinheiro(preco)
        elif (escolha == 2):
            pag_pix()
        elif (escolha == 3):
            pag_cartao()
        else:
            print("Escolha inválida.")

    if (produto_selecionado >= 5):
        print("\nOperação inválida. Tente novamente")


# Função para adicionar latas no estoque no ADM
def add_lata_adm(escolha_estoque):
    global est_coca, est_pepsi, est_uva, est_guar

    if (escolha_estoque == 1):
        add_lata = int(input("Quantas latas você está adicionando? "))
        if (add_lata + est_coca) <= 15:
            est_coca += add_lata
        else:
            print("Não é possível adicionar essa quantidade, o máximo é de 15 latas.")
    elif (escolha_estoque == 2):
        add_lata = int(input("Quantas latas você está adicionando? "))
        if (add_lata + est_pepsi) <= 15:
            est_pepsi += add_lata
        else:
            print("Não é possível adicionar essa quantidade, o máximo é de 15 latas.")
    elif (escolha_estoque == 3):
        add_lata = int(input("Quantas latas você está adicionando? "))
        if (add_lata + est_uva) <= 10:
            est_uva += add_lata
        else:
            print("Não é possível adicionar essa quantidade, o máximo é de 10 latas.")
    elif (escolha_estoque == 4):
        add_lata = int(input("Quantas latas você está adicionando? "))
        if (add_lata + est_guar) <= 10:
            est_guar += add_lata
        else:
            print("Não é possível adicionar essa quantidade, o máximo é de 10 latas.")
    else:
        print("Escolha inválida.")


# Função para verificação e adição de moedas no estoque de dinheio no ADM
def vericar_moedeiro():
    global qnt_dezreais, qnt_cincoreais, qnt_doisreais, qnt_umreal, qnt_cinqcent, qnt_vintecent, qnt_dezcent, qnt_cincocent

    escolha_moeda = 0
    print("--------------moedeiro--------------")
    print(" Existem: ", qnt_dezreais, " notas de 10 reais\n Existem: ", qnt_cincoreais,
          " notas de 5 reais \n Existem: ", qnt_doisreais, "notas de 2 reais \n Existem: ", qnt_umreal,
          "moedas de 1 real \n Existem: ", qnt_cinqcent, "moedas de 50 centavos \n Existem: ", qnt_vintecent,
          "moedas de 25 centavos \n Existem: ", qnt_dezcent, "moedas de 10 centavos \n Existem: ", qnt_cincocent,
          "moedas de 5 centavos \n")

    escolha_moeda = int(input("Você gostaria de adicionar ou remover moedas?\n [1] Sim \n [2] Não \n"))
    if (escolha_moeda == 1):

        add_dezr = 0
        add_cincor = 0
        add_dois = 0
        add_um = 0
        add_cinq = 0
        add_vinte = 0
        add_dezc = 0
        add_cincoc = 0

        add_dezr = int(input(
            "Quantas notas de 10 reais você está adicionando? \n Digite um valor negativo para retirar notas/moedas ou 0 se não estiver adicionando ou retirando. \n Digite o valor:"))
        if (add_dezr < 0):
            add_dezr = add_dezr * -1
            if (add_dezr > qnt_dezreais):
                print("Não é possível retirar mais do que existe na máquina.")
            else:
                qnt_dezreais -= add_dezr
        else:
            qnt_dezreais += add_dezr
        add_cincor = int(input(
            "Quantas notas de 5 reais você está adicionando? \n Digite um valor negativo para retirar notas/moedas ou 0 se não estiver adicionando ou retirando. \n Digite o valor:"))
        if (add_cincor < 0):
            add_cincor = add_cincor * -1
            if (add_cincor > qnt_cincoreais):
                print("Não é possível retirar mais do que existe na máquina.")
            else:
                qnt_cincoreais -= add_cincor
        else:
            qnt_cincoreais += add_cincor
        add_dois = int(input(
            "Quantas notas de 2 reais você está adicionando? \n Digite um valor negativo para retirar notas/moedas ou 0 se não estiver adicionando ou retirando. \n Digite o valor:"))
        if (add_dois < 0):
            add_dois = add_dois * -1
            if (add_dois > qnt_doisreais):
                print("Não é possível retirar mais do que existe na máquina.")
            else:
                qnt_doisreais -= add_dois
        else:
            qnt_doisreais += add_dois
        add_um = int(input(
            "Quantas moedas de 1 real você está adicionando? \n Digite um valor negativo para retirar notas/moedas ou 0 se não estiver adicionando ou retirando. \n Digite o valor:"))
        if (add_um < 0):
            add_um = add_um * -1
            if (add_um > qnt_umreal):
                print("Não é possível retirar mais do que existe na máquina.")
            else:
                qnt_umreal -= add_um
        else:
            qnt_umreal += add_um
        add_cinq = int(input(
            "Quantas moedas de 50 centavos você está adicionando? \n Digite um valor negativo para retirar notas/moedas ou 0 se não estiver adicionando ou retirando. \n Digite o valor:"))
        if (add_cinq < 0):
            add_cinq = add_cinq * -1
            if (add_cinq > qnt_cinqcent):
                print("Não é possível retirar mais do que existe na máquina.")
            else:
                qnt_cinqcent -= add_cinq
        else:
            qnt_cinqcent += add_cinq
        add_vinte = int(input(
            "Quantas moedas de 25 centavos você está adicionando? \n Digite um valor negativo para retirar notas/moedas ou 0 se não estiver adicionando ou retirando. \n Digite o valor:"))
        if (add_vinte < 0):
            add_vinte = add_vinte * -1
            if (add_vinte > qnt_vintecent):
                print("Não é possível retirar mais do que existe na máquina.")
            else:
                qnt_vintecent -= add_vinte
        else:
            qnt_vintecent += add_vinte
        add_dezc = int(input(
            "Quantas moedas de 10 centavos você está adicionando? \n Digite um valor negativo para retirar notas/moedas ou 0 se não estiver adicionando ou retirando. \n Digite o valor:"))
        if (add_dezc < 0):
            add_dezc = add_dezc * -1
            if (add_dezc > qnt_dezcent):
                print("Não é possível retirar mais do que existe na máquina.")
            else:
                qnt_dezcent -= add_dezc
        else:
            qnt_dezcent += add_dezc
        add_cincoc = int(input(
            "Quantas moedas de 5 centavos você está adicionando? \n Digite um valor negativo para retirar notas/moedas ou 0 se não estiver adicionando ou retirando. \n Digite o valor:"))
        if (add_cincoc < 0):
            add_cincoc = add_cincoc * -1
            if (add_cincoc > qnt_dezcent):
                print("Não é possível retirar mais do que existe na máquina.")
            else:
                qnt_cincocent -= add_cincoc
        else:
            qnt_cincocent += add_cincoc


# Função de troco do sistema.
def troco(pagado):
    # Definição do estoque de produtos na máquina.
    global est_coca, est_pepsi, est_uva, est_guar, totaldinheiro, preco, qnt_dezreais, qnt_cincoreais, qnt_doisreais, qnt_umreal, qnt_cinqcent, qnt_vintecent, qnt_dezcent, qnt_cincocent

    troco_total = 0
    troco_cincor = 0
    troco_dois = 0
    troco_um = 0
    troco_cinq = 0
    troco_vinte = 0
    troco_cincoc = 0
    troco_dezc = 0

    if (selecao == 1):
        troco_total = pagado - 5.5
    elif (selecao == 2):
        troco_total = pagado - 4
    elif (selecao == 3 or selecao == 4):
        troco_total = pagado - 4.9

    while troco_total >= 5 and qnt_dezreais > 0:
        troco_total -= 5
        qnt_cincoreais -= 1
        troco_cincor += 1
    while troco_total >= 2 and qnt_doisreais > 0:
        troco_total -= 2
        qnt_doisreais -= 1
        troco_dois += 1
    while troco_total >= 1 and qnt_umreal > 0:
        troco_total -= 1
        qnt_umreal -= 1
        troco_um += 1
    while troco_total >= 0.5 and qnt_cinqcent > 0:
        troco_total -= 0.5
        qnt_cinqcent -= 1
        troco_cinq += 1
    while troco_total >= 0.25 and qnt_vintecent > 0:
        troco_total -= 0.25
        qnt_vintecent -= 1
        troco_vinte += 1
    while ((troco_total >= 0.1 or troco_total >= 0.0999) and qnt_dezcent > 0):
        troco_total -= 0.1
        qnt_dezcent -= 1
        troco_dezc += 1
    while troco_total >= 0.05 and qnt_cincocent > 0:
        troco_total -= 0.05
        qnt_cincocent -= 1
        troco_cincoc += 1
    # Verificação se a máquina conseguiria dar o troco para o cliente.
    if (troco_total > 0):

        devolver_dinheiro()

        print("Não foi possível devolver troco. \n Devolvendo dinheiro...")
        qnt_cincoreais += troco_cincor
        qnt_doisreais += troco_dois
        qnt_umreal += troco_um
        qnt_cinqcent += troco_cinq
        qnt_vintecent += troco_vinte
        qnt_dezcent += troco_dezc
        qnt_cincocent += troco_cincoc
    else:
        # Impressão de quanto a máquina está dando ao cliente.
        if (troco_cincor > 0):
            print("Seu troco é de: ", troco_cincor, "notas de 5 reais.")
        if (troco_dois > 0):
            print("Seu troco é de: ", troco_dois, "notas de 2 reais.")
        if (troco_um > 0):
            print("Seu troco é de: ", troco_um, "moedas de 1 reais.")
        if (troco_cinq > 0):
            print("Seu troco é de: ", troco_cinq, "moedas de 50 centavos.")
        if (troco_vinte > 0):
            print("Seu troco é de: ", troco_vinte, "moedas de 25 centavos.")
        if (troco_vinte > 0):
            print("Seu troco é de: ", troco_vinte, "moedas de 25 centavos.")
        if (troco_dezc > 0):
            print("Seu troco é de: ", troco_dezc, "moedas de 10 centavos.")
        if (troco_cincoc > 0):
            print("Seu troco é de: ", troco_cincoc, "moedas de 5 centavos.")
        print("Produto enguegue. Volte sempre")

        if (selecao == 1):
            est_coca -= 1
            totaldinheiro += preco
        if (selecao == 2):
            est_pepsi -= 1
            totaldinheiro += preco
        if (selecao == 3):
            est_uva -= 1
            totaldinheiro += preco
        if (selecao == 4):
            est_guar = 1
            totaldinheiro += preco


# Começo do código em si
while (comando != 1 or comando != 2):
    comando = int(input("Qual usuário deseja entrar?\n[1] Consumidor\n[2] Administrador\n"))
    # Seleção de usuário
    if (comando == 1):

        while (comando != 3):
            selecao = 0
            # Menu de Produtos
            print('------------- Produtos --------------')

            selecao_produto()

            selecao = int(input("Selecione um dos produtos: "))
            # Produto selecionado
            if (selecao == 1 and est_coca > 0):
                pagamento_produto(selecao)

            elif (selecao == 2 and est_pepsi > 0):
                pagamento_produto(selecao)

            elif (selecao == 3 and est_uva > 0):
                pagamento_produto(selecao)

            elif (selecao == 4 and est_guar > 0):
                pagamento_produto(selecao)

            else:

                print("Escolha inválida ou produto esgotado.")

            comando = 3
    # Seleção de ADM
    elif (comando == 2):
        senha = 0
        contsenha = 4
        senha = int(input("Insira a senha de ADM: "))
        while (senha != senha_adm or senha == senha_adm):

            comando_adm = 0
            # Se o contador de tentativas se esgotar sai do modo de ADM
            if (contsenha == 1):
                break
            # Se o Usuário digitar 3 na senha, ele sai do modo de ADM
            if (senha == 3):

                break
            # Se usuário digitar senha incorreta
            elif (senha != senha_adm):
                contsenha -= 1
                senha = int(input(f"Senha incorreta, tente novamente. \n Tentativas restantes: {contsenha}. Digite 3 para sair: \n"))
            # Entrou no ADM
            elif (senha == senha_adm):

                comando_adm = int(input(
                    "O que você deseja fazer?\n [1] Verificar o estoque\n [2] Verificar o moedeiro\n [3] Verificar o quanto foi vendido. \n [4] Verificar o quanto foi vendido em pix. \n [5] Sair \n"))

                if (comando_adm == 2):
                    vericar_moedeiro()

                elif (comando_adm == 1):
                    add_lata = 0
                    selecao_produto()
                    escolha_estoque = 0
                    escolha_estoque = int(input("Gostaria de adicionar mais refrigerante? \n [1] Sim \n [2] Não \n "))
                    if (escolha_estoque == 1):
                        escolha_estoque = int(input("Qual refrigerante você vai adicionar? "))
                        add_lata_adm(escolha_estoque)

                elif (comando_adm == 3):
                    if (totaldinheiro > 0):
                        print("Foi vendido: R$", totaldinheiro, " Reais no dinheiro")
                    else:
                        print("Não foi vendido nada no dinheiro.")
                    if (totalcartao > 0):
                        print("Foi vendido: R$", totalcartao, " Reais na máquina de cartão")
                    else:
                        print("Não foi vendido nada no cartão.")
                    if (totalpix > 0):
                        print("Foi vendido: R$", totalpix, " Reais no PIX")
                    else:
                        print("Não foi vendido nada no PIX.")

                elif (comando_adm == 4):
                    verpix()

                elif (comando_adm == 5):

                    break

                else:

                    print("escolha inválida")

    else:

        print("Operação inválida. Tente novamente.")
