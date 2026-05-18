import tkinter as tk

janela = tk.Tk()
janela.title("My Recipe")
janela.geometry("1200x720")

texto = tk.Label(janela, text="Bem-vindo ao My Recipe")
texto.pack()

janela.mainloop()