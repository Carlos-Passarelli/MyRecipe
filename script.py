import json

# implementação dos arquivos .json
try:
    with open("receitas.json", "r", encoding="utf-8") as arquivo:
        receitas = json.load(arquivo)
except FileNotFoundError:
    receitas = []

try:
    with open("ingredientes.json", "r", encoding="utf-8") as arquivo:
        ingredientes = json.load(arquivo)
except FileNotFoundError:
    ingredientes = []

print("-----------------------------------")
print("Bem-vindo ao My Recipe, o que deseja?")
print("-----------------------------------")

# loop principal de funcionamento do site, disponibilizando 6 opções:
while True:
    print("1- Receitas registradas")
    print("2- Ingredientes registrados")
    print("3- Receita a partir dos meus ingredientes")
    print("4- Finalizar Programa")
    print("5- Excluir receita ou ingrediente")
    print("6- Tabela Nutricional")

    try:
        resposta = int(input("Insira a opção: "))
    except ValueError:
        print("Por favor, insira um número válido.")
        continue
        
    print("-----------------------------------")

    if resposta < 1 or resposta > 6:
        print("Opção inválida!")
        
    elif resposta == 4:
        print("Programa Finalizado!")
        break

    # adicionar receita / visualizar ingredientes e modo de preparo
    elif resposta == 1:
        for receita in receitas:
            print(receita["nome"])

        print(" ")
        print("Digite 0 para cancelar")
        print("Deseja adicionar uma nova receita?")
        print("1- SIM; 2- NÃO")

        opcao_nova_receita = int(input("Insira a opção: "))

        if opcao_nova_receita < 0 or opcao_nova_receita > 2:
            print("Opção Inválida!")
            
        elif opcao_nova_receita == 0:
            continue

        elif opcao_nova_receita == 1:
            novo_nome = input("Insira o nome da receita: ")
            novo_tempo = input("Insira o tempo de preparo da receita: ")
            novo_preparo = input("Descreva o preparo da receita: ")
            quant_novo_ingrediente = int(input("Quantos ingredientes haverão na sua receita? "))

            novos_ingredientes = []
            cancelado = False

            print("Escreva SAIR para cancelar")
            for i in range(quant_novo_ingrediente):
                add_novo_ingrediente = input("Insira o ingrediente: ")
                if add_novo_ingrediente.upper() == "SAIR":
                    print("Cadastro cancelado.")
                    cancelado = True
                    break
                novos_ingredientes.append(add_novo_ingrediente.lower())

            if not cancelado:
                nova_receita = {
                    "nome": novo_nome.lower(),
                    "tempo": int(novo_tempo),
                    "preparo": novo_preparo.lower(),
                    "ingredientes": novos_ingredientes
                }

                receitas.append(nova_receita)

                # salva a nova receita no .json
                with open("receitas.json", "w", encoding="utf-8") as arquivo:
                    json.dump(receitas, arquivo, indent=4, ensure_ascii=False)
                print("Receita adicionada!")
        
        else:
            print("Escolha uma receita para acessar")
            nome_pesquisa = input("Digite o nome da receita: ")
            
            # pesquisa do nome da receita no json e carga dos resultados
            for receita in receitas:
                if receita["nome"].lower() == nome_pesquisa.lower():
                    print("\nReceita encontrada!\n")
                    print("Nome:", receita["nome"])
                    print("Tempo:", receita["tempo"])
                    print("Modo de preparo:", receita["preparo"])
                    print("Ingredientes:")
                    for ingrediente in receita["ingredientes"]:
                        print("-", ingrediente)
        
    elif resposta == 2:
        for ingrediente in ingredientes:
            print(ingrediente["nome"])

        print(" ")
        print("Deseja adicionar um novo ingrediente?")
        print("1- SIM; 2- NÃO")
        
        opcao_novo_ingrediente = int(input("Insira a opção: "))
        
        if opcao_novo_ingrediente < 1 or opcao_novo_ingrediente > 2:
            print("Opção Inválida")
        
        elif opcao_novo_ingrediente == 1:
            novo_nome_ingrediente = input("Insira o nome do ingrediente: ")
            nova_caloria = int(input("Insira a quantidade de calorias do ingrediente: "))
            nova_categoria = input("Insira a categoria do ingrediente: ")

            novo_ingrediente = {
                "nome": novo_nome_ingrediente.lower(),
                "caloria": int(nova_caloria),
                "categoria": nova_categoria.lower(),
            }
            
            ingredientes.append(novo_ingrediente)

            # salva novo ingrediente no .json
            with open("ingredientes.json", "w", encoding="utf-8") as arquivo:
                json.dump(ingredientes, arquivo, indent=3, ensure_ascii=False)
            print("Ingrediente adicionado!")
        
    elif resposta == 3:
        quant_ingrediente = int(input("Quantos ingredientes você deseja pesquisar? "))
        pesquisa_ingrediente = []
        print("Escreva SAIR para cancelar")
        
        for i in range(0, quant_ingrediente):
            ingrediente_add = input("Insira o ingrediente: ")
            if ingrediente_add.upper() == "SAIR":
                break
            pesquisa_ingrediente.append(ingrediente_add.lower())
        
        encontrou = False
        print("\n--- Buscando Receitas ---")
        
        # se todos os ingredientes estiverem presentes na receita, ela é apresentada
        for receita in receitas:
            if all(ingrediente.lower() in pesquisa_ingrediente for ingrediente in receita["ingredientes"]):
                print("Receita Compatível:", receita["nome"])
                encontrou = True
        if not encontrou:
            print("Nenhuma receita compatível encontrada com esses ingredientes.")

    elif resposta == 5:
        print("O que deseja excluir?")
        print("1- Última Receita")
        print("2- Último Ingrediente")
        opcao_excluir = int(input("Insira a opção: "))

        if opcao_excluir < 1 or opcao_excluir > 2:
            print("Opção Inválida")
        
        elif opcao_excluir == 1:
            if receitas:
                
                # receitas.pop() exclui sempre a última receita ao .json
                receitas.pop()
                with open("receitas.json", "w", encoding="utf-8") as arquivo:
                    json.dump(receitas, arquivo, indent=4, ensure_ascii=False)
                print("Receita removida!")
            else:
                print("Nenhuma receita para remover.")
                
        else:
            if ingredientes:
                ingredientes.pop()
                
                # salva no .json o ingrediente retirado
                with open("ingredientes.json", "w", encoding="utf-8") as arquivo:
                    json.dump(ingredientes, arquivo, indent=3, ensure_ascii=False)
                print("Ingrediente removido!")
            else:
                print("Nenhuma ingrediente para remover.")
            
    else: 
        '''
            a tabela nutricional funciona como uma matriz, 
            exibindo caloria e categoria dos ingredientes registrados no .json
        '''
        tabela_nutricional = []
        for ingrediente in ingredientes:
            linha = [
                ingrediente["nome"],
                ingrediente["caloria"],
                ingrediente["categoria"]
            ]
            tabela_nutricional.append(linha)
            
        print("\nTABELA NUTRICIONAL\n")
    
        for linha in tabela_nutricional:
            print("Ingrediente:", linha[0])
            print("Calorias:", linha[1])
            print("Categoria:", linha[2])
            print("----------------")