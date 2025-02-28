from tkinter import *
import tkinter

class Usuario_encontrado(tkinter.Frame):
  def __init__(self, master):
    super().__init__(master)

    self.columnconfigure(0, weight=1)
    self.columnconfigure(1, weight=1)

    texto1 = Label(self, text="Dados do Usuário",
                          font=("Verdana", 16, "bold"),
                          fg="black")

    texto1.grid(row=0, column=0, columnspan=2, pady=10)

    self.label_dados = Label(self, text="", font=("Arial", 14), fg="black")
    self.label_dados.grid(row=2, column=0, columnspan=2, pady=10)

    botao_voltar = Button(self, text="Voltar", 
                          font=("Bahnschrift Condensed", 18, "bold"), 
                          command= lambda: self.master.mostrar_tela(self.master.tela1),
                          fg="black", 
                          bg="white",
                          bd=2,
                          relief="solid",
                          highlightbackground="black",
                          )
    
    botao_voltar.grid(row=3, column=0, pady=20, columnspan=2)

  def exibir_dados(self, lista):

    self.lista = lista
    keysList = ["Nome", "CPF", "Email", "Telefone", "Endereço"]
    texto_keys = "\n".join([f"{keysList[x]}: {lista[x]}" for x in range(len(lista))])
    self.label_dados.config(text=texto_keys)
