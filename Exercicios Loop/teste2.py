def desconto(compra):
    if compra >= 100 and compra <= 200:
        return compra * 0.05
    elif compra > 200 and compra < 500:
        return compra * 0.10
    elif compra >= 500:
        return compra * 0.15
    else:
        return 0

def teste2():
    clientes = []
    numcliente = 1
    
    while True:
        print("\n1 - Inserir cliente")
        print("2 - Listar clientes")
        print("3 - Buscar cliente")
        print("4 - Sair")
        op = input("Escolha: ")
        
        if op == "1":
            print("Cliente " + str(numcliente))
            nome = input("Nome: ")
            while nome == "":
                nome = input("Nome obrigatorio: ")
            
            morada = input("Morada: ")
            while morada == "":
                morada = input("Morada obrigatoria: ")
            
            tel = input("Telefone: ")
            while not tel.isdigit():
                tel = input("So numeros: ")
            
            nif = input("NIF: ")
            while not nif.isdigit() or len(nif) != 9:
                nif = input("NIF com 9 digitos: ")
            
            compra = float(input("Valor compra: "))
            
            d = desconto(compra)
            divida = compra - d
            
            c = {
                "num": numcliente,
                "nome": nome,
                "morada": morada,
                "tel": tel,
                "nif": nif,
                "compra": compra,
                "desconto": d,
                "divida": divida
            }
            
            clientes.append(c)
            numcliente = numcliente + 1
            print("Cliente inserido")
        
        elif op == "2":
            if len(clientes) == 0:
                print("Sem clientes")
            else:
                for i in range(len(clientes)):
                    c = clientes[i]
                    print("\nCliente " + str(c["num"]))
                    print("Nome: " + c["nome"])
                    print("Morada: " + c["morada"])
                    print("Telefone: " + c["tel"])
                    print("NIF: " + c["nif"])
                    print("Compra: " + str(c["compra"]) + "€")
                    print("Desconto: " + str(c["desconto"]) + "€")
                    print("Divida: " + str(c["divida"]) + "€")
                    if i < len(clientes)-1:
                        input("Enter para continuar...")
        
        elif op == "3":
            if len(clientes) == 0:
                print("Sem clientes")
            else:
                n = int(input("Numero do cliente: "))
                encontrou = False
                for c in clientes:
                    if c["num"] == n:
                        print("Nome: " + c["nome"])
                        print("Morada: " + c["morada"])
                        print("Telefone: " + c["tel"])
                        print("NIF: " + c["nif"])
                        print("Compra: " + str(c["compra"]) + "€")
                        print("Divida: " + str(c["divida"]) + "€")
                        encontrou = True
                        break
                if encontrou == False:
                    print("Cliente nao encontrado")
        
        elif op == "4":
            print("Adeus")
            break

teste2()