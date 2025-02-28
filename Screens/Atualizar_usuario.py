from tkinter import *
import tkinter
import DBfunctions as funcoes

class Atualizar_usuario(tkinter.Frame):
  def __init__(self, master):
    super().__init__(master)

    self.columnconfigure(0, weight=1)
    self.columnconfigure(1, weight=1)

    texto1 = Label(self, text="Cadastro",
                          font=("Verdana", 16, "bold"),
                          fg="black")                    
    
    texto1.grid(row=0, column=0, columnspan=2, pady=10)

    ################# NOME ################
    texto_nome = Label(self, text="Nome:", font=("Bahnschrift Condensed", 20, "bold"), fg="black")
    texto_nome.grid(row=1, column=0, sticky="e", padx=10, pady=10)

    self.nome = Entry(self, width=30, font="Arial 20", bd=2, relief="solid", highlightbackground="black")
    self.nome.grid(row=1, column=1, padx=10, pady=10, sticky="w")

    ################# CPF ################

    texto_cpf = Label(self, text="CPF:", font=("Bahnschrift Condensed", 20, "bold"), fg="black")
    texto_cpf.grid(row=2, column=0, sticky="e", padx=10, pady=10)

    self.cpf = Entry(self, width=30, font="Arial 20", bd=2, relief="solid", highlightbackground="black") 
    self.cpf.grid(row=2, column=1, padx=10, pady=10, sticky="w")

    ################# EMAIL ################

    texto_email = Label(self, text="Email:", font=("Bahnschrift Condensed", 20, "bold"), fg="black")
    texto_email.grid(row=3, column=0, sticky="e", padx=10, pady=10)

    self.email = Entry(self, width=30, font="Arial 20", bd=2, relief="solid", highlightbackground="black") 
    self.email.grid(row=3, column=1, padx=10, pady=10, sticky="w")

    ################# TELEFONE ################

    texto_telefone = Label(self, text="Telefone:", font=("Bahnschrift Condensed", 20, "bold"), fg="black")
    texto_telefone.grid(row=4, column=0, sticky="e", padx=10, pady=10)

    self.telefone = Entry(self, width=30, font="Arial 20", bd=2, relief="solid", highlightbackground="black") 
    self.telefone.grid(row=4, column=1, padx=10, pady=10, sticky="w")


    ################# ENDEREÇO ################

    texo_endereco = Label(self, text="Endereço:", font=("Bahnschrift Condensed", 20, "bold"), fg="black")
    texo_endereco.grid(row=5, column=0, sticky="e", padx=10, pady=10)

    self.endereco = Entry(self, width=30, font="Arial 20", bd=2, relief="solid", highlightbackground="black")
    self.endereco.grid(row=5, column=1, padx=10, pady=10, sticky="w")




  
    ############### BOTAO ENVIAR #############

    botao_enviar = Button(self, text="Enviar", 
                          font=("Bahnschrift Condensed", 18, "bold"), 
                          command= lambda: self.atualizar_dados(),                          
                          fg="black", 
                          bg="white",
                          bd=2,
                          relief="solid",
                          highlightbackground="black",
                          )
    
    botao_enviar.grid(row=6, column=1, pady=20, padx=10, sticky="e", columnspan=1)

    ############### BOTAO VOLTAR #############


    botao_voltar = Button(self, text="Voltar", 
                          font=("Bahnschrift Condensed", 18, "bold"), 
                          command= lambda: self.voltar(),
                          fg="black", 
                          bg="white",
                          bd=2,
                          relief="solid",
                          highlightbackground="black",
                          )
    
    botao_voltar.grid(row=6, column=0, pady=20, padx=10, sticky="w", columnspan=1)


  def recuperar_lista(self, lista):
    self.lista = lista
    self.preencher_campos()
    return self.lista
  
  def preencher_campos(self):
    if self.lista:
      self.nome.insert(0, self.lista[0])
      self.cpf.insert(0, self.lista[1])
      self.email.insert(0, self.lista[2])
      self.telefone.insert(0, self.lista[3])
      self.endereco.insert(0, self.lista[4])
  
  def atualizar_dados(self):
    nome_novo = self.nome.get()
    cpf_novo = self.cpf.get()
    email_novo = self.email.get()
    telefone_novo = self.telefone.get()
    endereco_novo = self.endereco.get()


    lista_antiga = self.lista.copy()

    nome_antigo = lista_antiga[0]
    cpf_antigo = lista_antiga[1]
    email_antigo = lista_antiga[2]
    telefone_antigo = lista_antiga[3]
    endereco_antigo = lista_antiga[4]

    funcoes.atualizar(nome_antigo, cpf_antigo, email_antigo, telefone_antigo, endereco_antigo, 
              nome_novo, cpf_novo, email_novo, telefone_novo, endereco_novo)
    
    self.nome.delete(0, tkinter.END)
    self.cpf.delete(0, tkinter.END)
    self.email.delete(0, tkinter.END)
    self.telefone.delete(0, tkinter.END)
    self.endereco.delete(0, tkinter.END)
    
    self.master.mostrar_tela(self.master.tela2)

  def voltar(self):
    self.nome.delete(0, tkinter.END)
    self.cpf.delete(0, tkinter.END)
    self.email.delete(0, tkinter.END)
    self.telefone.delete(0, tkinter.END)
    self.endereco.delete(0, tkinter.END)

    self.master.mostrar_tela(self.master.tela1)
