from tkinter import *
import tkinter as tk
from tkinter import ttk
import relatorio_tk_livro



def obter_selecao():

    #Captura seleção do combobox
    selecao = combobox.get()

    if selecao == 'Livros': relatorio_tk_livro.fichas_de_livros()

    if selecao == 'Leitores':print("Leitores")

    if selecao == 'Emprestimo': print("Emprestimo")

    if selecao == 'Opiniao Atendimento':
        print("Opiniao")

    if selecao == 'Voltar':
        janela_relatorio.destroy()
    




janela_relatorio = Tk()
janela_relatorio.title("Relatórios")
#janela_relatorio.iconbitmap("books.ico")
janela_relatorio['bg']=('white')
#janela_relatorio.geometry('500x400+50+20')
Etiqueta1 = Label(janela_relatorio, height=3,width=50,fg = 'black', bg = 'white',text="Área de relatórios",relief='groove')
Etiqueta1.grid(row=0,column=0)

##Em branco
Label(text="", width=10,bg='white').grid(row=1, column=0)

Etiqueta2 = Label(janela_relatorio, height=2, width=40, text = 'Escolha o tipo de relatório que deseja')
Etiqueta2.grid(row=2,column=0)

##Em branco
Label(text="", width=10,bg='white').grid(row=3, column=0)

#### Combobox ####

opcoes = ['Livros','Leitores','Emprestimo','Opiniao Atendimento','Voltar']
combobox = ttk.Combobox(janela_relatorio, values=opcoes, state="readonly")
combobox.set("Escolha uma opção") # Define o texto inicial
combobox.grid(row=4,column=0)

##Em branco
Label(text="", width=10,bg='white').grid(row=5, column=0)
    
# Criação do botão
botao = tk.Button(janela_relatorio, text="Ok", command=obter_selecao)
botao.grid(row=6,column=0)

#Em branco
Label(text="", width=10,bg='white').grid(row=7, column=0)



janela_relatorio.mainloop()