# MyRecipe
Aplicativo de receitas culinárias usando Python

# Como Usar
1- Com as extensões "Pylance" e "Python", ambas da Microsoft, execute o arquivo "interface.py" através do botão de play "run python file". Certifique-se também de ter instalado o Python 3.x;

2- Ao executar o programa, uma tela da biblioteca Tkinter é aberta, através dela, o usuário é capaz de escolher dentre 6 opções inseridas em um menu:

    2.1 - A primeira opção, "Receitas Registradas", permite ao usuário adicionar uma nova receita, incluindo um nome, o tempo de preparo, o modo de preparo e os ingredientes necessários. Caso não seja do interesse do usuário incluir uma nova receita, é possível apenas acessar uma receita já adicionada ao arquivo receitas.json, obtendo acesso às informações inseridas na receita acessada;

    2.2 - A segunda opção, "Ingredientes Registrados", funciona semelhante à primeira opção de receitas, porém aqui o usuário é capaz de obter informação dos ingredientes registrados em ingredientes.json, bem como adicionar novos ingredientes. Cada ingrediente possui um nome, uma categoria, e uma quantidade de calorias, importante para a comparação posterior na tabela nutricional;

    2.3 - A terceira opção, "Receita a partir de Ingredientes", é de longe a mais importante, tendo em vista que o objetivo do projeto é combater o desperdício de alimentos. O usuário é capaz de inserir os ingredientes disponíveis, e a partir deles, encontrar uma receita compatível já registrada em receitas.json;
    
    2.4 - A quarta opção, "Excluir receita ou ingrediente", permite ao usuário excluir uma última receita ou ingrediente inseridos em seus respectivos arquivos .json. Caso por engano o usuário tenha inserido alguma informação equívoca ao adicionar a respectiva receita ou ingrediente. Ou caso seja da vontade do usuário remover o último item das listas, usando o comando pop();

    2.5 - A quinta opção, "Tabela nutricional", ocupa o espaço de matriz da aplicação, onde o usuário obtém informações nutricionais, de forma organizada, sobre os ingredientes já registrados em ingredientes.json. A tabela nutricional conta com: o nome do ingrediente; a categoria; e o valor calórico. Assim, além de evitar o desperdício, o usuário também pode recorrer à ingredientes mais saudáveis;

    2.6 - A sexta e última opção, "Finalizar Programa", é autoexplicativa e apenas encerra a execução do programa.