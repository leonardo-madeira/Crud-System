from tkinter import *
import tkinter

class Tela1(tkinter.Frame):
  def __init__(self, master):
    super().__init__(master)
    self.columnconfigure(0, weight=1)
    self.columnconfigure(1, weight=1)

    texto1 = Label(self, text="Qual ação você gostaria de realizar?",
                          font=("Verdana", 16, "bold"),
                          fg="black")

    texto1.pack(pady=10)

    texto1.grid(row=0, column=0, padx=0, columnspan=2, pady=10)

    botao_cadastrar = tkinter.Button(self,
                            text="Cadastrar",
                            font=("Bahnschrift Condensed", 18, "bold"),
                            fg="black", 
                            bg="white",
                            bd=2,
                            relief="solid",
                            highlightbackground="black",
                            command=lambda: master.mostrar_tela(master.tela3))


    botao_cadastrar.grid(row=1, column=0, padx=10, pady=5, sticky="ew")

    botao_consultar = Button(self, 
                            text="Consultar",
                            font=("Bahnschrift Condensed", 18, "bold"),
                            fg="black", 
                            bg="white",
                            bd=2,
                            relief="solid",
                            highlightbackground="black",
                            command=lambda: master.mostrar_tela(master.tela4))

    botao_consultar.grid(row=1, column=1, padx=10, pady=5, sticky="ew")

    botao_atualizar = Button(self, 
                            text="Atualizar",
                            font=("Bahnschrift Condensed", 18, "bold"),
                            fg="black", 
                            bg="white",
                            bd=2,
                            relief="solid",
                            highlightbackground="black",
                            command= lambda: master.mostrar_tela(master.tela7))

    botao_atualizar.grid(row=2, column=0, padx=10, pady=5, sticky="ew")

    botao_excluir = Button(self,
                          text="Excluir",
                          font=("Bahnschrift Condensed", 18, "bold"),
                            fg="black", 
                            bg="white",
                            bd=2,
                            relief="solid",
                            highlightbackground="black",
                            command= lambda: master.mostrar_tela(master.tela9))

    botao_excluir.grid(row=2, column=1, padx=10, pady=5, sticky="ew")
