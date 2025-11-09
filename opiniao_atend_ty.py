from tkinter import *
import tkinter as tk
from tkinter import ttk
import json
import interfaces_io
import mensagem_aviso_tk
import opcoes_combobox
import avaliacao

janela_atend = Tk()
janela_atend.title("Avaliação")
janela_atend['bg']=('white') 
Etiqueta1 = Label(janela_atend, height=3,width=50, fg = 'black', bg = 'white', text="Opinião sobre o Atendimento",relief='groove')
Etiqueta1.grid(row=0,column=0)
Etiqueta2 = Label(janela_atend, height=2, width=40, text = 'Verifique a nota e veja os comentários')
Etiqueta2.grid(row=1,column=0)


janela_atend.mainloop()

