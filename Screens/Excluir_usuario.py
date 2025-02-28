from tkinter import *
import tkinter
import DBfunctions as funcoes

class Excluir_usuario(tkinter.Frame):
  def __init__(self, master):
    super().__init__(master)

    self.columnconfigure(0, weight=1)
    self.columnconfigure(1, weight=1)

    texto1 = Label(self, text="Dados do Usuário que serão EXCLUIDOS",
                          font=("Verdana", 16, "bold"),
                          fg="black")

    texto1.grid(row=0, column=0, columnspan=2, pady=10)

    self.label_dados = Label(self, text="", font=("Arial", 14), fg="black")
    self.label_dados.grid(row=2, column=0, columnspan=2, pady=10)

    ############### BOTAO ENVIAR #############

    botao_enviar = Button(self, text="Excluir", 
                          font=("Bahnschrift Condensed", 18, "bold"), 
                          command= lambda: self.excluir_dados(),                          
                          fg="white", 
                          bg="red",
                          bd=2,
                          relief="solid",
                          highlightbackground="black",
                          )
    
    botao_enviar.grid(row=3, column=1, pady=20, padx=10, sticky="e", columnspan=1)

    ############### BOTAO VOLTAR #############

    botao_voltar = Button(self, text="Voltar", 
                          font=("Bahnschrift Condensed", 18, "bold"), 
                          command= lambda: self.master.mostrar_tela(self.master.tela1),
                          fg="black", 
                          bg="white",
                          bd=2,
                          relief="solid",
                          highlightbackground="black",
                          )
    
    botao_voltar.grid(row=3, column=0, pady=20, padx=10, sticky="w", columnspan=1)

  def exibir_dados(self, lista):

    self.lista = lista
    keysList = ["Nome", "CPF", "Email", "Telefone", "Endereço"]
    texto_keys = "\n".join([f"{keysList[x]}: {lista[x]}" for x in range(len(lista))])
    self.label_dados.config(text=texto_keys)

  def excluir_dados(self):
    nome = self.lista[0]
    cpf = self.lista[1]
    email = self.lista[2]
    telefone = self.lista[3]
    endereco = self.lista[4]

    funcoes.excluir(nome, cpf, email, telefone, endereco)
    self.master.mostrar_tela(self.master.tela2)
