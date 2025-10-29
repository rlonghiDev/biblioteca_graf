from tkinter import *
import tkinter as tk
from tkinter import ttk


def obter_selecao():

    #Captura seleção do combobox
    selecao = combobox.get()

    if selecao == 'Livros':
        print("Livros")

    if selecao == 'Leitores':
        print("Leitores")

    if selecao == 'Emprestimo':
        print("Emprestimo")

    if selecao == 'Opiniao Atendimento':
        print("Opiniao")

    if selecao == 'Sair':
        exit()
    




janela = Tk()
janela.title("Biblioteca")
#janela.iconbitmap("books.ico")
janela['bg']=('white') #PapayaWhip  //  https://www.homehost.com.br/blog/tutoriais/tabela-de-cores-html/
janela.geometry('500x400+50+20')
Etiqueta1 = Label(janela, height=3,width=50,text="Sistema de gerencimento da Biblioteca",bg = 'white')
Etiqueta1.pack()
Etiqueta2 = Label(janela, height=2, width=40, fg = 'black', bg = 'white', text = 'Escolha a função desejada abaixo',relief='groove')
Etiqueta2.pack()
#### Combobox ####

opcoes = ['Livros','Leitores','Emprestimo','Opiniao Atendimento','Sair']
combobox = ttk.Combobox(janela, values=opcoes, state="readonly")
combobox.set("Escolha uma opção") # Define o texto inicial
combobox.pack(pady=10)

# Criação do botão
botao = tk.Button(janela, text="Escolha", command=obter_selecao)
botao.pack(pady=10)








janela.mainloop()