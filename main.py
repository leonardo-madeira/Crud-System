from tkinter import *
import tkinter
import DBfunctions as funcoes

from Screens.Tela1 import Tela1
from Screens.Tela_concluido import Tela_concluido
from Screens.Cadastro import Cadastro
from Screens.Consultar import Consultar
from Screens.Usuario_naoEncontrado import Usuario_naoEncontrado
from Screens.Usuario_encontrado import Usuario_encontrado
from Screens.Atualizar import Atualizar
from Screens.Atualizar_usuario import Atualizar_usuario
from Screens.Excluir import Excluir
from Screens.Excluir_usuario import Excluir_usuario

class App(tkinter.Tk):
  
  def __init__(self):
    super().__init__()
    self.title("CRUD SYSTEM")
    self.geometry("600x600")

    self.tela1 = Tela1(self)
    self.tela2 = Tela_concluido(self)
    self.tela3 = Cadastro(self)
    self.tela4 = Consultar(self)
    self.tela5 = Usuario_naoEncontrado(self)
    self.tela6 = Usuario_encontrado(self)
    self.tela7 = Atualizar(self)
    self.tela8 = Atualizar_usuario(self)
    self.tela9 = Excluir(self)
    self.tela10 = Excluir_usuario(self)


    self.tela1.pack(expand=True, fill="both")
  
  def mostrar_tela(self, tela):

        self.tela1.pack_forget()
        self.tela2.pack_forget()
        self.tela3.pack_forget()
        self.tela4.pack_forget()
        self.tela5.pack_forget()
        self.tela6.pack_forget()
        self.tela7.pack_forget()
        self.tela8.pack_forget()
        self.tela9.pack_forget()
        self.tela10.pack_forget()

        tela.pack(expand=True, fill="both")

if __name__ == "__main__":
  app = App()
  app.mainloop()