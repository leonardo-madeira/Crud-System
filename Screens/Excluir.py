from tkinter import *
import tkinter
import DBfunctions as funcoes

class Excluir(tkinter.Frame):
  def __init__(self, master):
    super().__init__(master)

    self.columnconfigure(0, weight=1)
    self.columnconfigure(1, weight=1)

    texto1 = Label(self, text="Digite o nome, cpf, telefone, email ou endereço \ndo usuário para EXCLUSÃO.",
                          font=("Verdana", 13, "bold"),
                          fg="black")                    
    
    texto1.grid(row=0, column=0, columnspan=2, pady=10)

    self.consulta = Entry(self, width=30, font="Arial 20", bd=2, relief="solid", highlightbackground="black")
    self.consulta.grid(row=1, column=0, pady=5, columnspan=2)

    ############### BOTAO ENVIAR #############
    botao_enviar = Button(self, text="Enviar", 
                          font=("Bahnschrift Condensed", 18, "bold"), 
                          command= lambda: self.consultar_dados(),                          
                          fg="black", 
                          bg="white",
                          bd=2,
                          relief="solid",
                          highlightbackground="black",
                          )
  
    
    botao_enviar.grid(row=3, column=1, pady=20, padx=10, sticky="e", columnspan=1)


    ############### BOTAO VOLTAR #############
    botao_voltar = Button(self, text="Voltar", 
                          font=("Bahnschrift Condensed", 18, "bold"), 
                          command= lambda: master.mostrar_tela(master.tela1),
                          fg="black", 
                          bg="white",
                          bd=2,
                          relief="solid",
                          highlightbackground="black",
                          )
    
    botao_voltar.grid(row=3, column=0, pady=20, padx=10, sticky="w", columnspan=1)

  def consultar_dados(self):
    resposta = self.consulta.get()
    self.consulta.delete(0, tkinter.END)
    self.lista = funcoes.consultar(resposta)

    if self.lista:
      self.master.tela10.exibir_dados(self.lista)
      self.master.mostrar_tela(self.master.tela10)
    else:
      self.master.mostrar_tela(self.master.tela5)