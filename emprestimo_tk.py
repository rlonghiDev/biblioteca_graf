from tkinter import *
import tkinter as tk
from tkinter import ttk
import mensagem_aviso_tk
import opcoes_combobox
import datetime
import json
import interfaces_io

def janela_emprestimos():
    
    def obter_selecao():

        #Captura seleção do combobox
        selecao = combobox.get()

        if selecao == 'Novo':
            novo_emprestimo_tk()
            

        # if selecao == 'Devolucao':
        #     encerra_emprestimo_tk()


        if selecao == 'Voltar':
            janela_emprestimos.destroy()
        
        
    ## Posicionamento grid ##
    
    janela_emprestimos = Tk()
    janela_emprestimos.title("Emprestimos")
    janela_emprestimos['bg']=('white') 
    
    #janela_emprestimos.geometry('600x650+50+20')
    Etiqueta1 = Label(janela_emprestimos, height=3,width=50,fg = 'black', bg = 'white',text="Gerenciamento de Emprestimos",relief='groove')
    Etiqueta1.grid(row=0,column=0)
    
    ##Em branco
    Label(text="", width=10,bg='white').grid(row=1, column=0)  
    
    Etiqueta2 = Label(janela_emprestimos, height=2, width=40, text = 'Escolha a função desejada abaixo')
    Etiqueta2.grid(row=2,column=0)
    
     ##Em branco
    Label(text="", width=10,bg='white').grid(row=3, column=0) 
    
    #### Combobox ####

    opcoes = ['Novo','Devolucao','Voltar']
    combobox = ttk.Combobox(janela_emprestimos, values=opcoes, state="readonly")
    combobox.set("Escolha uma opção") # Define o texto inicial
    combobox.grid(row=4,column=0)
    
     ##Em branco
    Label(text="", width=10,bg='white').grid(row=5, column=0) 

    # Criação do botão
    botao = tk.Button(janela_emprestimos, text="OK", command=obter_selecao)
    botao.grid(row=6,column=0)
    
     ##Em branco
    Label(text="", width=10,bg='white').grid(row=7, column=0)
    
    
    #Prepara e envia para ser escrito no arquivo
    def realiza_emprestimo(livro,leitor):
        
        dict_emprestimo = {}
        dict_emprestimo["leitor"] = leitor
        dict_emprestimo["livro"] = livro
        dict_emprestimo["data"] = str(datetime.date.today())
        dict_emprestimo["Registro"] = interfaces_io.procura_ultimo_registro('emprestimo')
        
        linha_emprestimo = json.dumps(dict_emprestimo)
        linha_emprestimo = '\n' + linha_emprestimo
        
        resultado = interfaces_io.escreve_em_arquivo('emprestimo',linha_emprestimo,'a')
        
        if resultado == 'sucesso':
            mensagem_aviso_tk.popup_aviso("Emprestimo registrado\ncom sucesso")
        else:
            mensagem_aviso_tk.popup_aviso("Falha ao registrar o emprestimo")
        
        
    

    def novo_emprestimo_tk():
        
        
        def pegar_selecoes_combobox():
            
            livro = combobox_livro.get()
            leitor = combobox_leitor.get()
            
            registro_book = livro[:5]
            
            registro_livro=''
            
            for i in registro_book:
                if i.isdigit():
                    registro_livro += i
                    
       
            registro_reader = leitor[:5]
            registro_leitor = ''
            
            for r in registro_reader:
                if r.isdigit():
                    registro_leitor += r
            
            
            if len(registro_livro) < 1 or len(registro_leitor) < 1:
                mensagem_aviso_tk.popup_aviso('Falha na seleção\nTente novamente')
                janela_emprestimos.destroy()
                
            
            realiza_emprestimo(registro_livro,registro_leitor)
            
            
         
        #Combobox livro
        
        opcoes_livro = []
        opcoes_livro = opcoes_combobox.carrega_opcoes('livro') 
        
        combobox_livro = ttk.Combobox(janela_emprestimos, values = opcoes_livro, state="readonly")
        combobox_livro.set("Escolha o livro") # Define o texto inicial
        combobox_livro.grid(row=8,column=0)
        #opcoes_livro.clear()
        
        ##Em branco
        Label(janela_emprestimos,text="", width=10,bg='white').grid(row=9, column=0) 
        
        #Combobox Leitor
        opcoes_leitor = []
        opcoes_leitor = opcoes_combobox.carrega_opcoes('leitor')
        
        combobox_leitor = ttk.Combobox(janela_emprestimos, values = opcoes_leitor, state="readonly")
        combobox_leitor.set("Escolha o leitor") # Define o texto inicial
        combobox_leitor.grid(row=10,column=0)
        
        ##Em branco
        Label(janela_emprestimos,text="", width=10,bg='white').grid(row=11, column=0) 
        
        botao_empresta = tk.Button(janela_emprestimos, text="Emprestar", command=pegar_selecoes_combobox)
        botao_empresta.grid(row=12,column=0)
        
        ##Em branco
        Label(janela_emprestimos,text="", width=10,bg='white').grid(row=13, column=0)
            
    
    
    
    
    




    janela_emprestimos.mainloop()


