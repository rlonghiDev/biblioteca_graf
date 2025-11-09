from tkinter import *
import tkinter as tk
from tkinter import ttk
import livros_tk
import leitores_tk
import emprestimo_tk
import relatorio_tk
import comentario_registros


def obter_selecao():

    #Captura seleção do combobox
    selecao = combobox.get()

    if selecao == 'Livros':livros_tk.janela_livros()

    if selecao == 'Leitores':leitores_tk.janela_leitores()

    if selecao == 'Emprestimo':emprestimo_tk.janela_emprestimos()
    
    if selecao == 'Relatorios':relatorio_tk.escolher_relatorio()
        
    if selecao == 'Opiniao Atendimento':comentario_registros.comentario_recebe()

    if selecao == 'Sair':
        exit()
    

janela = Tk()
janela.title("Biblioteca")
#janela.iconbitmap("books.ico")
janela['bg']=('white') #PapayaWhip  //  https://www.homehost.com.br/blog/tutoriais/tabela-de-cores-html/
#janela.geometry('500x300+50+20')
Etiqueta1 = Label(janela, height=3,width=50,fg = 'black', bg = 'white',text="Sistema de Gerencimento da Biblioteca",relief='groove')
Etiqueta1.grid(row=0,column=0)

##Em branco
Label(text="", width=10,bg='white').grid(row=1, column=0)

Etiqueta2 = Label(janela, height=2, width=40, text = 'Escolha a função desejada abaixo')
Etiqueta2.grid(row=3,column=0)

##Em branco
Label(text="", width=10,bg='white').grid(row=4, column=0)


#### Combobox ####

opcoes = ['Livros','Leitores','Emprestimo','Relatorios','Opiniao Atendimento','Sair']
combobox = ttk.Combobox(janela, values=opcoes, state="readonly",height=10,width=15)
combobox.set("Escolha uma opção") # Define o texto inicial
combobox.grid(row=5,column=0)

##Em branco
Label(text="", width=10,bg='white').grid(row=6, column=0)

# Criação do botão
botao = tk.Button(janela, text="Escolha", command=obter_selecao)
botao.grid(row=7,column=0)

##Em branco
Label(text="", width=10,bg='white').grid(row=8, column=0)

janela.mainloop()