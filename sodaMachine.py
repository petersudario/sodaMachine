est_coca = 3
est_pepsi = 1
est_uva = 1
est_guar = 1
qnt_dezreais = 2
qnt_cincoreais = 20
qnt_doisreais = 10
qnt_umreal = 20
qnt_cinqcent = 5
qnt_vintecent = 30
qnt_dezcent = 10
qnt_cincocent = 5
moedeiro = []
senha_adm = 5040302010

vendido_dinheiro = []

vendido_pix = []

tipo_moedas = [0.05, 0.10, 0.25, 0.50, 1.00]

tipo_cedulas = [2.00, 5.00, 10.00]

comando = 0

global selecao

def contar_moeda(pagamento, cinco, dez, vinte, cinq, um, dois):
    for moeda in pagamento:
        if moeda == 0.5:
            cinco += 1
        if moeda == 0.10:
            dez += 1
        if moeda == 0.25:
            vinte += 1
        if moeda == 0.50:
            cinq += 1
        if moeda == 1:
            um += 1
        if moeda == 2:
            dois += 1


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


def selecao_produto():
    produtos = ["Coca-cola", "Pepsi", "Fanta Uva", "Fanta Guaraná"]
    cont = 0

    for produto in produtos:
        quantidade = estoque_produto(produto)

        cont += 1
        print("[", cont, "] ", produto, quantidade)

def pagamento_dinheiro(custo):

    global est_coca, est_pepsi, est_uva, est_guar, dinheiro_inserido, tipo_moedas, tipo_cedulas
    total_inserido = []
    pagado = 0

    dinheiro_inserido = float(input('Insira suas moedas (uma vez por vez): '))

    if (dinheiro_inserido in tipo_moedas or dinheiro_inserido in tipo_cedulas):
        pagado += dinheiro_inserido
        if pagado < custo:
            while (pagado < custo):
                # if pagado = custo:
                    #terminar o igual o custo

                dinheiro_faltante = float(
                    input("Dinheiro faltante. Insira mais moedas\nTotal pago até o momento: R$" + str(pagado) + "\n"))

                if dinheiro_faltante in tipo_cedulas or dinheiro_faltante in tipo_moedas:
                    total_inserido.append(dinheiro_faltante)
                    pagado += dinheiro_faltante

            print('Pagamento finalizado. Volte sempre!')
            contar_moeda(total_inserido, qnt_cincocent, qnt_dezreais, qnt_vintecent, qnt_cinqcent, qnt_umreal, qnt_doisreais)

        elif pagado > custo:
            troco(qnt_dezreais, qnt_cincoreais, qnt_doisreais, qnt_umreal, qnt_cinqcent, qnt_vintecent, qnt_dezcent, qnt_cincocent, pagado)
    else:
        print("Moeda ou cédula inválida, tente novamente")
def pagamento_produto(produto_selecionado):


    if (produto_selecionado == 1):
        preco = 5.50
        pagamento_dinheiro(preco)
    if (produto_selecionado == 2):
        preco = 4
        pagamento_dinheiro(preco)
    if (produto_selecionado == 3):
        preco = 4.9
        pagamento_dinheiro(preco)
    if (produto_selecionado == 4):
        preco = 4.9
        pagamento_dinheiro(preco)
    if (produto_selecionado > 6):
        print("\nOperação inválida. Tente novamente")

def add_lata_adm(escolha_estoque, qnt_coca, qnt_pepsi, qnt_uva, qnt_guar):
    if (escolha_estoque == 1):
        add_lata = int(input("Quantas latas você está adicionando?"))
        qnt_coca += add_lata
    elif (escolha_estoque == 2):
        add_lata = int(input("Quantas latas você está adicionando?"))
        qnt_pepsi += add_lata
    elif (escolha_estoque == 3):
        add_lata = int(input("Quantas latas você está adicionando?"))
        qnt_uva += add_lata
    elif (escolha_estoque == 4):
        add_lata = int(input("Quantas latas você está adicionando?"))
        qnt_guar += add_lata
    else:
        print("Escolha inválida.")

def vericar_moedeiro():
    escolha_moeda = 0
    print("Existem: ", qnt_dezreais, " notas de 10 reais\n \
          Existem: ", qnt_cincoreais, " notas de 5 reais \n \
          Existem: ", qnt_doisreais, "notas de 2 reais \n \
          Existem: ", qnt_umreal, "moedas de 1 real \n \
          Existem: ", qnt_cinqcent, "moedas de 50 centavos \n \
          Existem: ", qnt_vintecent, "moedas de 25 centavos \n \
          Existem: ", qnt_dezcent, "moedas de 10 centavos \n \
          Existem: ", qnt_cincocent, "moedas de 5 centavos \n")

    # escolha_moeda = int(input("Você gostaria de adicionar mais moedas?\n [1] Sim \n [2] Não] \n"))
    #  if (escolha_moeda == 1):
    #      add_vinte = 0
    #      add_dez = 0
    #      add_cinco = 0
    #      add

def troco(qnt_dezreais, qnt_cincoreais, qnt_doisreais, qnt_umreal, qnt_cinqcent, qnt_vintecent, qnt_dezcent, qnt_cincocent, pagado):

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
        qnt_dezreais -=1
        troco_cincor +=1
    while troco_total >= 2 and qnt_doisreais > 0:
        troco_total -= 2
        qnt_doisreais -= 2
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
    while troco_total >= 0.1 and qnt_dezcent > 0:
        troco_total -= 0.1
        qnt_dezcent -= 1
        troco_dezc += 1
    while troco_cincor >= 0.05 and qnt_cincocent > 0:
        troco_total -= 0.05
        qnt_cincocent -= 1
        troco_cincoc += 1
    if (troco_total > 0):
        print("Não foi possível devolver troco. \n Devolvendo dinheiro...")
        qnt_cincoreais += troco_cincor
        qnt_doisreais += troco_dois
        qnt_umreal += troco_um
        qnt_cinqcent += troco_cinq
        qnt_vintecent += troco_vinte
        qnt_dezcent += troco_dezc
        qnt_cincocent += troco_cincoc
    elif (troco_total == 0):
        if (troco_cincor > 0):
            print("seu troco é de: ", troco_cincor, "notas de 5 reais.")
        if (troco_dois > 0):
            print("seu troco é de: ", troco_dois, "notas de 2 reais.")
        if (troco_um > 0):
            print("seu troco é de: ", troco_um, "moedas de 1 reais.")
        if (troco_cinq > 0):
            print("seu troco é de: ", troco_cinq, "moedas de 50 centavos.")
        if (troco_vinte > 0):
            print("seu troco é de: ", troco_vinte, "moedas de 25 centavos.")
        if (troco_vinte > 0):
            print("seu troco é de: ", troco_vinte, "moedas de 25 centavos.")
        if (troco_dezc > 0):
            print("seu troco é de: ", troco_dezc, "moedas de 10 centavos.")
        if (troco_cincoc > 0):
            print("seu troco é de: ", troco_cincoc, "moedas de 5 centavos.")
    elif (troco_total < 0):
        print("fudeu")
    else:
        print("fudeu pra caralho")




while (comando != 1 or comando != 2):
    comando = int(input("Qual usuário deseja entrar?\n[1] Consumidor\n[2] Administrador\n"))

    if (comando == 1):

        while (comando != 3):
            selecao = 0
            print('------- Produtos --------')

            selecao_produto()

            selecao = int(input("Selecione um dos produtos: "))

            pagamento_produto(selecao)

            comando = 3

    elif (comando == 2):
            senha = 0
            senha = int(input("Insira a senha de ADM: "))
            while(senha != senha_adm):

                if (senha != senha_adm):
                    senha = int(input("Senha incorreta, tente novamente. Digite 3 para sair: \n"))

                elif (senha == senha_adm):
                    comando_adm = 0
                    comando_adm = int(input("O que você deseja fazer?\n \
                    [1] Verificar o estoque\n \
                    [2] Verificar o moedeiro\n \
                    [3] Sair"))

                    if (comando_adm == 1):
                        print("Existem:", est_coca, " latas de coca-cola")
                        print("Existem:", est_pepsi, " latas de pepsi")
                        print("Existem:", est_uva, " latas de fanta uva")
                        print("Existem:", est_guar, " latas de fanta guaraná")

                    elif (comando_adm == 2):
                        add_lata = 0
                        escolha_estoque = int(input("Qual refrigerante você vai adicionar?"))
                        selecao_produto()
                        add_lata_adm(escolha_estoque, est_coca, est_pepsi, est_uva, est_guar)
                    elif (comando_adm == 3):
                       print("escolha inválida")

                elif (senha == 3):
                    break
    else:
        print("Operação inválida. Tente novamente.")