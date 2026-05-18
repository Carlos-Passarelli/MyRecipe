import json
import tkinter as tk
from tkinter import messagebox, simpledialog, ttk

# funções de carga e salvamento do json
def carregar_dados():
    global receitas, ingredientes
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


def salvar_receitas():
    with open("receitas.json", "w", encoding="utf-8") as arquivo:
        json.dump(receitas, arquivo, indent=4, ensure_ascii=False)


def salvar_ingredientes():
    with open("ingredientes.json", "w", encoding="utf-8") as arquivo:
        json.dump(ingredientes, arquivo, indent=3, ensure_ascii=False)


# adicionando itens
def adicionar_receita():
    nome = simpledialog.askstring("Nova Receita", "Insira o nome da receita:")
    if not nome:
        return

    tempo = simpledialog.askinteger(
        "Nova Receita", "Insira o tempo de preparo (minutos):"
    )
    if tempo is None:
        return

    preparo = simpledialog.askstring("Nova Receita", "Descreva o preparo:")
    if not preparo:
        return

    quant = simpledialog.askinteger(
        "Nova Receita", "Quantos ingredientes haverão na receita?"
    )
    if not quant:
        return

    novos_ingredientes = []
    for i in range(quant):
        ingrediente = simpledialog.askstring(
            "Ingrediente", f"Insira o ingrediente {i+1} (ou 'SAIR' para cancelar):"
        )
        if not ingrediente or ingrediente.upper() == "SAIR":
            messagebox.showinfo("Cancelado", "Cadastro de receita cancelado.")
            return
        novos_ingredientes.append(ingrediente.lower())

    nova_receita = {
        "nome": nome.lower(),
        "tempo": tempo,
        "preparo": preparo.lower(),
        "ingredientes": novos_ingredientes,
    }
    receitas.append(nova_receita)
    salvar_receitas()
    messagebox.showinfo("Sucesso", "Receita adicionada com sucesso!")


def adicionar_ingrediente():
    nome = simpledialog.askstring(
        "Novo Ingrediente", "Insira o nome do ingrediente:"
    )
    if not nome:
        return

    caloria = simpledialog.askinteger(
        "Novo Ingrediente", "Insira a quantidade de calorias:"
    )
    if caloria is None:
        return

    categoria = simpledialog.askstring(
        "Novo Ingrediente", "Insira a categoria:"
    )
    if not categoria:
        return

    novo_ingrediente = {
        "nome": nome.lower(),
        "caloria": caloria,
        "categoria": categoria.lower(),
    }
    ingredientes.append(novo_ingrediente)
    salvar_ingredientes()
    messagebox.showinfo("Sucesso", "Ingrediente adicionado com sucesso!")


# visualizações / busca
def listar_receitas():
    janela_rec = tk.Toplevel(root)
    janela_rec.title("Receitas Registradas")
    janela_rec.geometry("400x400")

    tk.Label(
        janela_rec, text="Clique em uma receita para ver os detalhes:"
    ).pack(pady=5)

    lista_box = tk.Listbox(janela_rec)
    lista_box.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)

    for r in receitas:
        lista_box.insert(tk.END, r["nome"].title())

    def ver_detalhes():
        selecionado = lista_box.curselection()
        if not selecionado:
            return
        index = selecionado[0]
        rec = receitas[index]

        detalhes = (
            f"Nome: {rec['nome'].title()}\n"
            f"Tempo: {rec['tempo']} min\n"
            f"Preparo: {rec['preparo']}\n\n"
            f"Ingredientes:\n" + "\n".join([f"- {i}" for i in rec["ingredientes"]])
        )
        messagebox.showinfo(f"Detalhes: {rec['nome'].title()}", detalhes)

    tk.Button(janela_rec, text="Ver Detalhes", command=ver_detalhes).pack(pady=5)
    tk.Button(
        janela_rec, text="+ Adicionar Receita", command=adicionar_receita
    ).pack(pady=5)


def listar_ingredientes():
    janela_ing = tk.Toplevel(root)
    janela_ing.title("Ingredientes Registrados")
    janela_ing.geometry("300x350")

    lista_box = tk.Listbox(janela_ing)
    lista_box.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

    for ing in ingredientes:
        lista_box.insert(tk.END, ing["nome"].title())

    tk.Button(
        janela_ing, text="+ Adicionar Ingrediente", command=adicionar_ingrediente
    ).pack(pady=5)


def buscar_por_ingredientes():
    quant = simpledialog.askinteger(
        "Buscar por Ingredientes", "Quantos ingredientes deseja pesquisar?"
    )
    if not quant:
        return

    pesquisa_ingrediente = []
    for i in range(quant):
        ing = simpledialog.askstring(
            "Buscar", f"Insira o ingrediente {i+1} (ou 'SAIR' para cancelar):"
        )
        if not ing or ing.upper() == "SAIR":
            return
        pesquisa_ingrediente.append(ing.lower())

    encontradas = []
    for receita in receitas:
        if all(
            ing.lower() in pesquisa_ingrediente
            for ing in receita["ingredientes"]
        ):
            encontradas.append(receita["nome"].title())

    if encontradas:
        resultado = "Receitas Compatíveis:\n" + "\n".join(encontradas)
    else:
        resultado = "Nenhuma receita compatível encontrada."

    messagebox.showinfo("Resultado da Busca", resultado)


# excluir
def excluir_item():
    janela_excluir = tk.Toplevel(root)
    janela_excluir.title("Excluir")
    janela_excluir.geometry("250x120")

    def excluir_receita():
        if receitas:
            removida = receitas.pop()
            salvar_receitas()
            messagebox.showinfo(
                "Removido", f"Última receita ({removida['nome']}) removida!"
            )
        else:
            messagebox.showwarning("Aviso", "Nenhuma receita para remover.")
        janela_excluir.destroy()

    def excluir_ingrediente():
        if ingredientes:
            removido = ingredientes.pop()
            salvar_ingredientes()
            messagebox.showinfo(
                "Removido",
                f"Último ingrediente ({removido['nome']}) removido!",
            )
        else:
            messagebox.showwarning("Aviso", "Nenhuma ingrediente para remover.")
        janela_excluir.destroy()

    tk.Button(
        janela_excluir, text="Excluir Última Receita", command=excluir_receita
    ).pack(fill=tk.X, padx=20, pady=10)
    tk.Button(
        janela_excluir,
        text="Excluir Último Ingrediente",
        command=excluir_ingrediente,
    ).pack(fill=tk.X, padx=20, pady=5)


# tabela nutricional
def exibir_tabela_nutricional():
    janela_tab = tk.Toplevel(root)
    janela_tab.title("Tabela Nutricional")
    janela_tab.geometry("500x300")

    # criando uma tabela visual
    colunas = ("ingrediente", "calorias", "categoria")
    tabela = ttk.Treeview(janela_tab, columns=colunas, show="headings")

    tabela.heading("ingrediente", text="Ingrediente")
    tabela.heading("calorias", text="Calorias")
    tabela.heading("categoria", text="Categoria")

    tabela.column("ingrediente", minwidth=150, width=150)
    tabela.column("calorias", minwidth=100, width=100)
    tabela.column("categoria", minwidth=150, width=150)

    for ing in ingredientes:
        tabela.insert(
            "",
            tk.END,
            values=(
                ing["nome"].title(),
                ing["caloria"],
                ing["categoria"].title(),
            ),
        )

    tabela.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)


# Configurando janela de menu
receitas = []
ingredientes = []
carregar_dados()

root = tk.Tk()
root.title("My Recipe")
root.geometry("350x400")
root.configure(bg="#A8A885")

label_titulo = tk.Label(
    root, text="Bem-vindo ao My Recipe", font=("Arial", 14, "bold")
)
label_titulo.pack(pady=15)

# botões do menu
btn_1 = tk.Button(
    root, text="Receitas Registradas", width=30, command=listar_receitas
)
btn_1.pack(pady=5)

btn_2 = tk.Button(
    root,
    text="Ingredientes Registrados",
    width=30,
    command=listar_ingredientes,
)
btn_2.pack(pady=5)

btn_3 = tk.Button(
    root,
    text="Receita a partir de Ingredientes",
    width=30,
    command=buscar_por_ingredientes,
)
btn_3.pack(pady=5)

btn_5 = tk.Button(
    root, text="Excluir Receita ou Ingrediente", width=30, command=excluir_item
)
btn_5.pack(pady=5)

btn_6 = tk.Button(
    root, text="Tabela Nutricional", width=30, command=exibir_tabela_nutricional
)
# Correção do nome da função associada ao botão 6
btn_6.configure(command=exibir_tabela_nutricional)
btn_6.pack(pady=5)

btn_4 = tk.Button(
    root, text="Finalizar Programa", width=30, fg="red", command=root.quit
)
btn_4.pack(pady=20)

root.mainloop()