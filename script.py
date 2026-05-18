import json

with open("receitas.json", "r", encoding="utf-8") as arquivo:
    receitas = json.load(arquivo)

with open("ingredientes.json", "r", encoding="utf-8") as arquivo:
    ingredientes = json.load(arquivo)

print("-----------------------------------")
print("Bem-vindo ao My Recipe, o que deseja?")
print("-----------------------------------")

while True:
    print("1- Receitas registradas")
    print("2- Ingredientes registrados")
    print("3- Receita a partir dos meus ingredientes")
    print("4- Finalizar Programa")
    print("5- Excluir receita ou ingrediente")
    print("6- Tabela Nutricional")

    resposta = int(input("Insira a opção: "))
    print("-----------------------------------")

    if resposta < 1 or resposta > 6:
        print("Opção inválida!")
        
    elif resposta == 4:
        print("Programa Finalizado!")
        break

    elif resposta == 1:

        for receita in receitas:
            print(receita["nome"])

        print(" ")
        print("Deseja adicionar uma nova receita?")
        print("1- SIM; 2- NÃO")

        opcao_nova_receita = int(input("Insira a opção: "))

        if opcao_nova_receita < 1 or opcao_nova_receita > 2:
            print("Opção Inválida!")

        elif opcao_nova_receita == 1:
            novo_nome = input(
                "Insira o nome da receita: "
            )
            novo_tempo = input(
                "Insira o tempo de preparo da receita: "
            )
            novo_preparo = input(
                "Descreva o preparo da receita: "
            )
            quant_novo_ingrediente = int(
                input(
                    "Quantos ingredientes haverão na sua receita? "
                )
            )

            novos_ingredientes = []

            print("Escreva SAIR para cancelar")
            for i in range(quant_novo_ingrediente):
                add_novo_ingrediente = input(
                    "Insira o ingrediente: "
                )
                if add_novo_ingrediente == "SAIR":
                    print("Programa Finalizado")
                    break
                novos_ingredientes.append(
                    add_novo_ingrediente.lower()
                )

            nova_receita = {
                "nome": novo_nome.lower(),
                "tempo": int(novo_tempo),
                "preparo": novo_preparo.lower(),
                "ingredientes": novos_ingredientes
            }

            receitas.append(nova_receita)

            with open(
                "receitas.json",
                "w",
                encoding="utf-8"
            ) as arquivo:
                json.dump(
                    receitas,
                    arquivo,
                    indent=4,
                    ensure_ascii=False
                )
            print("Receita adicionada!")
        
        else:
            print("Escolha uma receita para acessar")
            nome_pesquisa = input("Digite o nome da receita: ")
            
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
                
                novo_nome_ingrediente = input(
                    "Insira o nome do ingrediente: "
                )
                nova_caloria = int(input(
                    "Insira a quantidade de calorias do ingrediente: "
                ))
                nova_categoria = input(
                    "Insira a categoria do ingrediente: "
                )

                novo_ingrediente = {
                    "nome": novo_nome_ingrediente.lower(),
                    "caloria": int(nova_caloria),
                    "categoria": nova_categoria.lower(),
                }
                
                ingredientes.append(novo_ingrediente)

                with open(
                    "ingredientes.json",
                    "w",
                    encoding="utf-8"
                ) as arquivo:
                    json.dump(
                        ingredientes,
                        arquivo,
                        indent=3,
                        ensure_ascii=False
                    )
                print("Ingrediente adicionado!")
        
    elif resposta == 3:
        quant_ingrediente = int(input("Quantos ingredientes você deseja pesquisar? "))
        pesquisa_ingrediente = []
        print("Escreva SAIR para cancelar")
        for i in range (0, quant_ingrediente):
            ingrediente_add = input("Insira o ingrediente: ")
            if ingrediente_add == "SAIR":
                break
            pesquisa_ingrediente.append(ingrediente_add.lower())
            for receita in receitas:
                if all(
                    ingrediente.lower() in pesquisa_ingrediente
                    for ingrediente in receita["ingredientes"]
                ):
                    print("Receita Compatível:")
                    print(receita["nome"])

    elif resposta == 5:
        print("O que deseja excluir?")
        print("1- Última Receita")
        print("2- Último Ingrediente")
        opcao_excluir = int(input("Insira a opção: "))

        if opcao_excluir < 1 or opcao_excluir > 2:
            print("Opção Inválida")
        
        elif opcao_excluir == 1:
            receitas.pop()
            with open(
            "receitas.json",
            "w",
            encoding="utf-8"
            ) as arquivo:
                json.dump(
                    receitas,
                    arquivo,
                    indent=4,
                    ensure_ascii=False
                )
            print("Receita removida!")
                
        else:
            ingredientes.pop()
            with open(
            "ingredientes.json",
            "w",
            encoding="utf-8"
            ) as arquivo:
                json.dump(
                    ingredientes,
                    arquivo,
                    indent=3,
                    ensure_ascii=False
                )
            print("Ingrediente removido!")
            
    else: 
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