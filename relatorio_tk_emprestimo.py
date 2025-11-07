from tkinter import *
import tkinter as tk
from tkinter import ttk
import interfaces_io
import monta_string
import json


def fichas_de_emprestimos():
    janela_emprestimos = Tk()
    janela_emprestimos.title("Relatório Empréstimos")
    janela_emprestimos['bg']=('white') 
    #janela_emprestimos.geometry('600x650+50+20')
    Etiqueta1 = Label(janela_emprestimos, height=3,width=50,fg = 'black', bg = 'white',text="Lista de emprestimos no Acervo",relief='groove')
    Etiqueta1.grid(row=0,column=0)

    ##Em branco
    Label(text="", width=10,bg='white').grid(row=1, column=0)

    text_area = Text(janela_emprestimos, height=20, width=50,wrap='word')
    text_area.grid(row=1,column=0)
    
    

    def fichas_emprestimos():
        fichas = ''
        ##Captura do arquivo de emprestimos:
        emprestimos = interfaces_io.le_arquivo('emprestimo')
        
        for emprestimo in emprestimos:
            dict_emprestimo = emprestimo
            info_emprestimo = json.loads(dict_emprestimo)
            etiqueta_emprestimo = monta_string.monta_string_emprestimo(info_emprestimo)
            fichas += etiqueta_emprestimo
        
        return fichas
            
        

    text_area.insert('1.0',fichas_emprestimos())
    
fichas_de_emprestimos()