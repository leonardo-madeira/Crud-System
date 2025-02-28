from tkinter import *
import tkinter
from PIL import Image, ImageTk

class Tela_concluido(tkinter.Frame):
  def __init__(self, master):
    super().__init__(master)

    self.columnconfigure(0, weight=1)
    self.columnconfigure(1, weight=1)

    row0 = Label(self, text="")
    row0.grid(row=0, column=0, columnspan=2, pady=10)

    texto1 = Label(self, text="Concluído!",
                          font=("Verdana", 16, "bold"),
                          fg="black")

    texto1.grid(row=1, column=0, columnspan=2, pady=10)

    imagem = Image.open(r"images\done.png")
    imagem = imagem.resize((100, 100))

    self.imagem_tk = ImageTk.PhotoImage(imagem)

    label_imagem = Label(self, image=self.imagem_tk)

    label_imagem.grid(row=2, column=0, columnspan=2, pady=10)

    botao_voltar = Button(self, text="Voltar", 
                          font=("Bahnschrift Condensed", 18, "bold"), 
                          command= lambda: master.mostrar_tela(master.tela1),
                          fg="black", 
                          bg="white",
                          bd=2,
                          relief="solid",
                          highlightbackground="black",
                          )
    
    botao_voltar.grid(row=3, column=0, pady=20, columnspan=2)
