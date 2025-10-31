from tkinter import *
import tkinter as tk
from tkinter import ttk
import livros_tk
import interfaces_io
import json
import monta_string
import avaliacao


# for i in range(0,3):
#     if i == 0:
#         tipo_arquivo = "livros.txt"
#     if i == 1:
#         tipo_arquivo = "leitores.txt"
#     if i == 2:
#         tipo_arquivo = "emprestimos.txt"
#     if i == 3:
#         tipo_arquivo = "avaliacao.txt"
        
#     interfaces_io.limpa_linha_em_branco(tipo_arquivo)
        


def relatorio_livros():
    janela_relatorio_livros = Tk()
    janela_relatorio_livros.title("Livros do Acervo")
    
    lista_linha_str = interfaces_io.le_arquivo('livro')
    
    rel_livro = ''
    
    for linha in lista_linha_str:
        dict_livro = json.loads(linha)
        print(dict_livro)
        print(dict_livro['Registro'])
        ficha_livro = monta_string.monta_string_livro(dict_livro)
        rel_livro += ficha_livro
    
    print(rel_livro)
        
        








def obter_selecao():

    #Captura seleção do combobox
    selecao = combobox.get()

    if selecao == 'Livros': relatorio_livros()

    if selecao == 'Leitores':print("Leitores")

    if selecao == 'Emprestimo': print("Emprestimo")

    if selecao == 'Opiniao Atendimento':
        print("Opiniao")

    if selecao == 'Voltar':
        exit()
    




janela_relatorio = Tk()
janela_relatorio.title("Relatórios")
#janela_relatorio.iconbitmap("books.ico")
janela_relatorio['bg']=('white') #PapayaWhip  //  https://www.homehost.com.br/blog/tutoriais/tabela-de-cores-html/
janela_relatorio.geometry('500x400+50+20')
Etiqueta1 = Label(janela_relatorio, height=3,width=50,fg = 'black', bg = 'white',text="Área de relatórios",relief='groove')
Etiqueta1.pack(pady=2)
Etiqueta2 = Label(janela_relatorio, height=2, width=40, text = 'Escolha o tipo de relatório que deseja')
Etiqueta2.pack()

#### Combobox ####

opcoes = ['Livros','Leitores','Emprestimo','Opiniao Atendimento','Voltar']
combobox = ttk.Combobox(janela_relatorio, values=opcoes, state="readonly")
combobox.set("Escolha uma opção") # Define o texto inicial
combobox.pack(pady=10)

# Criação do botão
botao = tk.Button(janela_relatorio, text="Obter Relatório", command=obter_selecao)
botao.pack(pady=10)





janela_relatorio.mainloop()