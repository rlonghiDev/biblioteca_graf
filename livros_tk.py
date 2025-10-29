from tkinter import *
import tkinter as tk
from tkinter import ttk



def janela_livros():
    
    def obter_selecao():

        #Captura seleção do combobox
        selecao = combobox.get()

        if selecao == 'Acrescentar':
            print("Acrescentar")
            cadastro_tk()
            

        if selecao == 'Retirar':
            print("Leitores")


        if selecao == 'Voltar':
            janela_livros.destroy()
        




    janela_livros = Tk()
    janela_livros.title("Livros")
    janela_livros['bg']=('white') 
    janela_livros.geometry('600x600+50+20')
    Etiqueta1 = Label(janela_livros, height=3,width=50,fg = 'black', bg = 'white',text="Gerenciamento do Acervo de Livros",relief='groove')
    Etiqueta1.pack(pady=2)
    Etiqueta2 = Label(janela_livros, height=2, width=40, text = 'Escolha a função desejada abaixo')
    Etiqueta2.pack()
    #### Combobox ####

    opcoes = ['Acrescentar','Retirar','Voltar']
    combobox = ttk.Combobox(janela_livros, values=opcoes, state="readonly")
    combobox.set("Escolha uma opção") # Define o texto inicial
    combobox.pack(pady=10)

    # Criação do botão
    botao = tk.Button(janela_livros, text="Escolha", command=obter_selecao)
    botao.pack(pady=10)
    

    def cadastro_tk():
        
        
        def pegar_texto():
            texto1 = campo_entrada1.get()
            texto2 = campo_entrada2.get()
            texto3 = campo_entrada3.get()
            texto4 = campo_entrada4.get()
            texto5 = campo_entrada5.get()
            texto6 = campo_entrada6.get()
            
            
            
            print(texto1)
            print(texto2)
            print(texto3)
            print(texto4)
            print(texto5)
            print(texto6)
            

        frame_esquerdo = Frame(janela_livros,bg='white')
        frame_esquerdo.pack(anchor="w",padx=5,pady=5)
        
        
        label_instr1 = Label(frame_esquerdo,text="Informe o título do Livro:",bg='white')
        #label_instr1.pack(side=LEFT)
        label_instr1.pack(anchor="w",padx=5,pady=5)

        campo_entrada1 = Entry(frame_esquerdo,width = 35,bg='LightGray')
        #campo_entrada1.pack(side=LEFT)
        campo_entrada1.pack(anchor="w",padx=5,pady=5)
        
        
        
        
        frame_esquerdo2 = Frame(janela_livros,bg='white')
        frame_esquerdo2.pack(anchor="w",padx=5,pady=5)
        
        
        label_instr2 = Label(frame_esquerdo2,text="Informe o autor:",bg='white')
        label_instr2.pack(anchor="w",padx=5,pady=5)

        campo_entrada2 = Entry(frame_esquerdo2,width = 35,bg='LightGray')
        campo_entrada2.pack(side=LEFT)
        
        
        
        frame_esquerdo3 = Frame(janela_livros,bg='white')
        frame_esquerdo3.pack(anchor="w",padx=5,pady=5)
        
        
        label_instr3 = Label(frame_esquerdo3,text="Informe o autor:",bg='white')
        label_instr3.pack(anchor="w",padx=5,pady=5)

        campo_entrada3 = Entry(frame_esquerdo3,width = 35,bg='LightGray')
        campo_entrada3.pack(side=LEFT)
        
        
        
        

        botao_cadastrar_livro = Button(janela_livros, text = "Cadastrar", command=pegar_texto,bg='LightGray')
        botao_cadastrar_livro.pack(pady=20)
        
    

    janela_livros.mainloop()