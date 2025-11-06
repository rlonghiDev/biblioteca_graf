from tkinter import *
import tkinter as tk
from tkinter import ttk
import interfaces_io
import monta_string
import json


def fichas_de_livros():
    janela_livros = Tk()
    janela_livros.title("Relatório Livros")
    janela_livros['bg']=('white') 
    #janela_livros.geometry('600x650+50+20')
    Etiqueta1 = Label(janela_livros, height=3,width=50,fg = 'black', bg = 'white',text="Lista de livros no Acervo",relief='groove')
    Etiqueta1.grid(row=0,column=0)

    ##Em branco
    Label(text="", width=10,bg='white').grid(row=1, column=0)

    text_area = Text(janela_livros, height=20, width=50,wrap='word')
    text_area.grid(row=1,column=0)
    
    

    def fichas_livros():
        fichas = ''
        ##Captura do arquivo de livros:
        livros = interfaces_io.le_arquivo('livro')
        
        for livro in livros:
            dict_livro = livro
            info_livro = json.loads(dict_livro)
            etiqueta_livro = monta_string.monta_string_livro(info_livro)
            fichas += etiqueta_livro
        
        return fichas
            
        

    text_area.insert('1.0',fichas_livros())
    
#fichas_de_livros()