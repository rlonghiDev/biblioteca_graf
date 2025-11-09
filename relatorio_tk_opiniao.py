from tkinter import *
import tkinter as tk
from tkinter import ttk
import interfaces_io
import monta_string
import json


def fichas_de_comentarios():
    janela_comment = Tk()
    janela_comment.title("Comentários do Atendimento")
    janela_comment['bg']=('white') 
    #janela_comment.geometry('600x650+50+20')
    Etiqueta1 = Label(janela_comment, height=3,width=50,fg = 'black', bg = 'white',text="Comentarios dos usuários",relief='groove')
    Etiqueta1.grid(row=0,column=0,columnspan=2)

    ##Em branco
    Label(text="", width=10,bg='white').grid(row=1, column=0,columnspan=2)

    text_area = Text(janela_comment, height=20, width=10,wrap='word')
    text_area.grid(row=1,column=0,columnspan=2)
    
    

    def fichas_comments():
        fichas = ''
        ##Captura do arquivo de livros:
        comentarios = interfaces_io.le_arquivo('comentario')
        
        for comentario in comentarios:
            registro,conteudo = comentario.split(',')
            print("Registro: ",registro)
            print("Conteudo: ",conteudo)
            
            #Comentario sobre atendimento
            # if registro == '0': 
            #     return conteudo
            
    fichas_comments()
    
    janela_comment.mainloop()


fichas_de_comentarios()


                
        
        
            
        

    #text_area.insert('1.0',fichas_livros())
    