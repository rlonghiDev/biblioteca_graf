from tkinter import *
import tkinter as tk
from tkinter import ttk
import interfaces_io
import monta_string
import json


def fichas_de_leitores():
    janela_leitores = Tk()
    janela_leitores.title("Relatório Leitores")
    janela_leitores['bg']=('white') 
    #janela_leitores.geometry('600x650+50+20')
    Etiqueta1 = Label(janela_leitores, height=3,width=50,fg = 'black', bg = 'white',text="Lista de Leitores",relief='groove')
    Etiqueta1.grid(row=0,column=0)

    ##Em branco
    Label(text="", width=10,bg='white').grid(row=1, column=0)

    text_area = Text(janela_leitores, height=20, width=50,wrap='word')
    text_area.grid(row=2,column=0)
    
    

    def fichas_leitores():
        fichas = ''
        ##Captura do arquivo de livros:
        leitores = interfaces_io.le_arquivo('leitor')
        
        for leitor in leitores:
            dict_leitor = leitor
            info_leitor = json.loads(dict_leitor)
            etiqueta_leitor = monta_string.monta_string_leitor(info_leitor)
            fichas += etiqueta_leitor
        
        return fichas
            
        

    text_area.insert('1.0',fichas_leitores())
    
#fichas_de_leitores()