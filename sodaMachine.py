import os

os.system('cls')

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
pixtelefone = []
pixvalor = []
senha_adm = 5040302010

# fazer o pix

global preco
totaldinheiro = 0
totalcartao = 0
totalpix = 0
vendido_dinheiro = []
vendido_cartao = []
vendido_pix = []

tipo_moedas = [0.05, 0.10, 0.25, 0.50, 1.00]

tipo_cedulas = [2.00, 5.00, 10.00]

comando = 0

def funccartao(escolha):    
    global est_coca, est_pepsi, est_uva, est_guar, preco, totalcartao, selecao
    valcartao = True
        
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
                escolha = 4
            if selecao == 2:
                est_pepsi -= 1
            if selecao == 3:
                escolha = 4
                est_uva -= 1
            if selecao == 4:
                escolha = 4
                est_guar -= 1
            os.system('cls')
            print("Produto sndo entregue. Volte sempre.")
            vendido_cartao.append(preco)
            totalcartao += preco
            break            
     
        else:
            print("Escolha inválida.")
            os.system('cls')

def verpix():

    if (len(pixtelefone) > 0):
        print("Foram vendidos: ", len(pixtelefone), "produtos no pix.")
        for x in range(len(pixtelefone)):
            print("Preço vendido: R$", pixvalor[x], "| Telefone do pix:", pixtelefone[x])
    else:
        print("Não foi vendido nada no pix.")

def funcpix():
    global est_coca, est_pepsi, est_uva, est_guar, escolha

    telefone = int(input("Insira seu número de telefone: EX: 41992436675 \n Digite: "))
    pixtelefone.append(telefone)
    pixvalor.append(preco)
    if selecao == 1:
        est_coca -= 1
        escolha = 4
    if selecao == 2:
        est_pepsi -= 1
    if selecao == 3:
        escolha = 4
        est_uva -= 1
    if selecao == 4:
        escolha = 4
        est_guar -= 1

    os.system('cls')
    print("Aguardando transferência...")
    print("Produto sendo entregue...")
    print("Produto entregue. Volte sempre.")


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

    global est_coca, est_pepsi, est_uva, est_guar, dinheiro_inserido, tipo_moedas, tipo_cedulas, selecao
    total_inserido = []
    pagado = 0

    dinheiro_inserido = float(input('Insira suas moedas (uma vez por vez): '))

    if (dinheiro_inserido in tipo_moedas or dinheiro_inserido in tipo_cedulas):
        pagado += dinheiro_inserido
        if pagado <= custo:
            while (pagado <= custo):
                
                if (pagado == custo):
                    os.system('cls')
                    if (selecao == 1):
                        est_coca -= 1
                    if (selecao == 2):
                        est_pepsi -= 1
                    if (selecao == 3):
                        est_uva -= 1
                    if (selecao == 4):
                        est_guar = 1
                    os.system('cls')
                    print("Produto entregue, Volte sempre...")
                    break

                dinheiro_faltante = float(
                    input("Dinheiro faltante. Insira mais moedas\nTotal pago até o momento: R$" + str(pagado) + "\n"))

                if dinheiro_faltante in tipo_cedulas or dinheiro_faltante in tipo_moedas:
                    total_inserido.append(dinheiro_faltante)
                    pagado += dinheiro_faltante

                if pagado > custo:
                    troco(qnt_dezreais, qnt_cincoreais, qnt_doisreais, qnt_umreal, qnt_cinqcent, qnt_vintecent, qnt_dezcent, qnt_cincocent, pagado)
                
            contar_moeda(total_inserido, qnt_cincocent, qnt_dezreais, qnt_vintecent, qnt_cinqcent, qnt_umreal, qnt_doisreais)
        elif (pagado > custo):
            troco(qnt_dezreais, qnt_cincoreais, qnt_doisreais, qnt_umreal, qnt_cinqcent, qnt_vintecent, qnt_dezcent, qnt_cincocent, pagado)

        
    else:
        os.system('cls')
        print("Moeda ou cédula inválida, tente novamente")

def pagamento_produto(produto_selecionado):
    
    global preco
    
    escolha = 0

    if (produto_selecionado == 1):
        preco = 5.50
        
        escolha = int(input("Qual a forma de pagamento? \n [1] Dinheiro \n [2] PIX \n [3] Cartão \n [4] Cancelar operação \n"))
        if (escolha == 1):
            pagamento_dinheiro(preco)
        elif (escolha == 2):
            funcpix()
        elif (escolha == 3):
            funccartao(escolha)
        else:
            print("Escolha inválida.")
        
    if (produto_selecionado == 2):
        preco = 4
        escolha = int(input("Qual a forma de pagamento? \n [1] Dinheiro \n [2] PIX \n [3] Cartão \n [4] Cancelar operação \n"))
        if (escolha == 1):
            pagamento_dinheiro(preco)
        elif (escolha == 2):
            funcpix()
        elif (escolha == 3):
            funccartao(escolha)
        else:
            print("Escolha inválida.")
        os.system('cls')
    if (produto_selecionado == 3):
        preco = 4.9
        escolha = int(input("Qual a forma de pagamento? \n [1] Dinheiro \n [2] PIX \n [3] Cartão \n [4] Cancelar operação \n"))
        if (escolha == 1):
            pagamento_dinheiro(preco)
        elif (escolha == 2):
            funcpix()
        elif (escolha == 3):
            funccartao(escolha)
        else:
            print("Escolha inválida.")
    if (produto_selecionado == 4):
        preco = 4.9
        escolha = int(input("Qual a forma de pagamento? \n [1] Dinheiro \n [2] PIX \n [3] Cartão \n [4] Cancelar operação \n"))
        if (escolha == 1):
            pagamento_dinheiro(preco)
        elif (escolha == 2):
            funcpix()
        elif (escolha == 3):
            funccartao(escolha)
        else:
            print("Escolha inválida.")
        os.system('cls')
    if (produto_selecionado >= 5):
        os.system('cls')
        print("\nOperação inválida. Tente novamente")

def add_lata_adm(escolha_estoque):
    
    global est_coca, est_pepsi, est_uva, est_guar
    
    if (escolha_estoque == 1):
        add_lata = int(input("Quantas latas você está adicionando? "))
        est_coca += add_lata
    elif (escolha_estoque == 2):
        add_lata = int(input("Quantas latas você está adicionando? "))
        est_pepsi += add_lata
    elif (escolha_estoque == 3):
        add_lata = int(input("Quantas latas você está adicionando? "))
        est_uva += add_lata
    elif (escolha_estoque == 4):
        add_lata = int(input("Quantas latas você está adicionando? "))
        est_guar += add_lata
    else:
        print("Escolha inválida.")

def vericar_moedeiro():
    global qnt_dezreais, qnt_cincoreais, qnt_doisreais, qnt_umreal, qnt_cinqcent, qnt_vintecent, qnt_dezcent, qnt_cincocent
    
    escolha_moeda = 0
    print("--------------moedeiro--------------")
    print(" Existem: ", qnt_dezreais, " notas de 10 reais\n Existem: ", qnt_cincoreais, " notas de 5 reais \n Existem: ", qnt_doisreais, "notas de 2 reais \n Existem: ", qnt_umreal, "moedas de 1 real \n Existem: ", qnt_cinqcent, "moedas de 50 centavos \n Existem: ", qnt_vintecent, "moedas de 25 centavos \n Existem: ", qnt_dezcent, "moedas de 10 centavos \n Existem: ", qnt_cincocent, "moedas de 5 centavos \n")

    escolha_moeda = int(input("Você gostaria de adicionar mais moedas?\n [1] Sim \n [2] Não \n"))
    if (escolha_moeda == 1):
        
        add_dezr = 0
        add_cincor = 0
        add_dois = 0
        add_um = 0
        add_cinq = 0
        add_vinte = 0
        add_dezc = 0
        add_cincoc = 0
        
        add_dezr = int(input("Quantas notas de 10 reais você está adicionando? \n Digite um valor negativo para retirar notas/moedas ou 0 se não estiver adicionando ou retirando. \n Digite o valor:"))
        if (add_dezr < 0):
            add_dezr * -1
            if (add_dezr > qnt_dezreais):
                print("Não é possível retirar mais do que existe na máquina.")
            else:
                qnt_dezreais -= add_dezr
        add_cincor = int(input("Quantas notas de 5 reais você está adicionando? \n Digite um valor negativo para retirar notas/moedas ou 0 se não estiver adicionando ou retirando. \n Digite o valor:"))
        if (add_cincor < 0):
            add_cincor * -1
            if (add_cincor > qnt_cincoreais):
                print("Não é possível retirar mais do que existe na máquina.")
            else:
                qnt_cincoreais -= add_cincor
        add_dois = int(input("Quantas notas de 2 reais você está adicionando? \n Digite um valor negativo para retirar notas/moedas ou 0 se não estiver adicionando ou retirando. \n Digite o valor:"))
        if (add_dois < 0):
            add_dois * -1
            if (add_dois > qnt_doisreais):
                print("Não é possível retirar mais do que existe na máquina.")
            else:
                qnt_doisreais -= add_dois
        add_um = int(input("Quantas moedas de 1 real você está adicionando? \n Digite um valor negativo para retirar notas/moedas ou 0 se não estiver adicionando ou retirando. \n Digite o valor:"))
        if (add_um < 0):
            add_um * -1
            if (add_um > qnt_umreal):
                print("Não é possível retirar mais do que existe na máquina.")
            else:
                qnt_umreal -= add_um
        add_cinq = int(input("Quantas moedas de 50 centavos você está adicionando? \n Digite um valor negativo para retirar notas/moedas ou 0 se não estiver adicionando ou retirando. \n Digite o valor:"))
        if (add_cinq < 0):
            add_cinq * -1
            if (add_cinq > qnt_cinqcent):
                print("Não é possível retirar mais do que existe na máquina.")
            else:
                qnt_cinqcent -= add_cinq
        add_vinte = int(input("Quantas moedas de 25 centavos você está adicionando? \n Digite um valor negativo para retirar notas/moedas ou 0 se não estiver adicionando ou retirando. \n Digite o valor:"))
        if (add_vinte < 0):
            add_vinte * -1
            if (add_vinte > qnt_vintecent):
                print("Não é possível retirar mais do que existe na máquina.")
            else:
                qnt_vintecent -= add_vinte
        add_dezc = int(input("Quantas moedas de 10 centavos você está adicionando? \n Digite um valor negativo para retirar notas/moedas ou 0 se não estiver adicionando ou retirando. \n Digite o valor:"))
        if (add_dezc < 0):
            add_dezc * -1
            if (add_dezc > qnt_dezcent):
                print("Não é possível retirar mais do que existe na máquina.")
            else:
                qnt_dezcent -= add_dezc
        add_cincoc = int(input("Quantas moedas de 5 centavos você está adicionando? \n Digite um valor negativo para retirar notas/moedas ou 0 se não estiver adicionando ou retirando. \n Digite o valor:"))
        if (add_cincoc < 0):
            add_cincoc * -1
            if (add_cincoc > qnt_dezcent):
                print("Não é possível retirar mais do que existe na máquina.")
            else:
                qnt_cincocent -= add_cincoc
        os.system('cls')
        
        

def troco(qnt_dezreais, qnt_cincoreais, qnt_doisreais, qnt_umreal, qnt_cinqcent, qnt_vintecent, qnt_dezcent, qnt_cincocent, pagado):

    global est_coca, est_pepsi, est_uva, est_guar

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
        qnt_dezreais -= 1
        troco_cincor +=1
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
    if (troco_total > 0):
        os.system('cls')
        print("Não foi possível devolver troco. \n Devolvendo dinheiro...")
        qnt_cincoreais += troco_cincor
        qnt_doisreais += troco_dois
        qnt_umreal += troco_um
        qnt_cinqcent += troco_cinq
        qnt_vintecent += troco_vinte
        qnt_dezcent += troco_dezc
        qnt_cincocent += troco_cincoc
    else:
        os.system('cls')
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
        if (selecao == 2):
            est_pepsi -= 1
        if (selecao == 3):
            est_uva -= 1
        if (selecao == 4):
            est_guar = 1

while (comando != 1 or comando != 2):
    comando = int(input("Qual usuário deseja entrar?\n[1] Consumidor\n[2] Administrador\n"))

    if (comando == 1):

        while (comando != 3):
            selecao = 0
            print('------------- Produtos --------------')

            selecao_produto()

            selecao = int(input("Selecione um dos produtos: "))
            
            if (selecao == 1 and est_coca > 0):
                pagamento_produto(selecao)
                
            elif (selecao == 2 and est_pepsi > 0):
                pagamento_produto(selecao)
                
            elif (selecao == 3 and est_uva > 0):
                pagamento_produto(selecao)
                
            elif (selecao == 4 and est_guar > 0):
                pagamento_produto(selecao)
                
            else:
                os.system('cls')
                print("Escolha inválida ou produto esgotado.")

            

            comando = 3

    elif (comando == 2):
            senha = 0
            contsenha = 4
            senha = int(input("Insira a senha de ADM: "))
            while(senha != senha_adm or senha == senha_adm):
                
                
                comando_adm = 0
                
                if (contsenha == 1):
                    os.system('cls')
                    break

                if (senha == 3):
                    os.system('cls')
                    break
                
                elif (senha != senha_adm):
                    contsenha -= 1
                    senha = int(input(f"Senha incorreta, tente novamente. \n Tentativas restantes: {contsenha}. Digite 3 para sair: \n"))

                elif (senha == senha_adm):
                    
                    comando_adm = int(input("O que você deseja fazer?\n [1] Verificar o estoque\n [2] Verificar o moedeiro\n [3] Verificar o quanto foi vendido. \n [4] Verificar o quanto foi vendido em pix. \n [5] Sair \n"))

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
                            os.system('cls')
                        elif (escolha_estoque == 2):
                            os.system('cls')
                        
                    elif (comando_adm == 3):
                        print("Foi vendido: R$", totaldinheiro, " Reais no dinheiro")
                        print("Foi vendido: R$", totalcartao, " Reais na máquina de cartão")
                        print("Foi vendido: R$", totalpix, " Reais no PIX")

                    elif (comando_adm == 4):
                        verpix()
                        
                    elif (comando_adm == 5):
                        os.system('cls')
                        break
                        
                    else:
                       os.system('cls')
                       print("escolha inválida")

    else:
        os.system('cls')
        print("Operação inválida. Tente novamente.")