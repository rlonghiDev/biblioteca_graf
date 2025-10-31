from tkinter import *
import tkinter as tk
from tkinter import ttk
import json
import interfaces_io



def janela_livros():
    
    def obter_selecao():

        #Captura seleção do combobox
        selecao = combobox.get()

        if selecao == 'Acrescentar':
            cadastro_tk()
            

        if selecao == 'Retirar':
            print("Retirar")


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
            titulo = campo_entrada1.get()
            autor = campo_entrada2.get()
            qde_disp = campo_entrada3.get()
            qde_uso = campo_entrada4.get()
            nota = campo_entrada5.get()
            registro = interfaces_io.procura_ultimo_registro('livro')


            cad_livro = {}
            cad_livro['titulo'] = titulo
            cad_livro['autor'] = autor
            cad_livro['Qde_disp'] = qde_disp
            cad_livro['Qde_uso'] = qde_uso
            cad_livro['rating'] = nota
            cad_livro['Registro'] = registro

            linha_str = json.dumps(cad_livro)
            linha_str = "\n" + linha_str

            resultado = interfaces_io.escreve_em_arquivo('livro',linha_str,'a')
            print("Processo de gravação do arquivo:",resultado)



        frame_esquerdo = Frame(janela_livros,bg='white')
        frame_esquerdo.pack(anchor="w",padx=5,pady=5)
        
        
        label_instr1 = Label(frame_esquerdo,text="Informe o título do Livro:",bg='white')
        #label_instr1.pack(side=LEFT)
        label_instr1.pack(anchor="w",padx=5,pady=5)

        campo_entrada1 = Entry(frame_esquerdo,width = 35,bg='LightGray')
        #campo_entrada1.pack(side=LEFT)
        campo_entrada1.pack(anchor="w",padx=5,pady=5)
        
        ##
        frame_esquerdo2 = Frame(janela_livros,bg='white')
        frame_esquerdo2.pack(anchor="w",padx=5,pady=5)
        
        
        label_instr2 = Label(frame_esquerdo2,text="Informe o autor:",bg='white')
        label_instr2.pack(anchor="w",padx=5,pady=5)

        campo_entrada2 = Entry(frame_esquerdo2,width = 35,bg='LightGray')
        campo_entrada2.pack(side=LEFT)
        
        
        ##
        frame_esquerdo3 = Frame(janela_livros,bg='white')
        frame_esquerdo3.pack(anchor="w",padx=5,pady=5)
        
        
        label_instr3 = Label(frame_esquerdo3,text="Disponíveis:",bg='white')
        label_instr3.pack(anchor="w",padx=5,pady=5)

        campo_entrada3 = Entry(frame_esquerdo3,width = 35,bg='LightGray')
        campo_entrada3.pack(side=LEFT)
        
        
        ##
        frame_esquerdo4 = Frame(janela_livros,bg='white')
        frame_esquerdo4.pack(anchor="w",padx=5,pady=5)
        
        
        label_instr4 = Label(frame_esquerdo4,text="Em uso:",bg='white')
        label_instr4.pack(anchor="w",padx=5,pady=5)

        campo_entrada4 = Entry(frame_esquerdo4,width = 35,bg='LightGray')
        campo_entrada4.pack(side=LEFT)

        ##
        frame_esquerdo5 = Frame(janela_livros,bg='white')
        frame_esquerdo5.pack(anchor="w",padx=5,pady=5)
        
        
        label_instr5 = Label(frame_esquerdo5,text="Nota (de 1 a 5):",bg='white')
        label_instr5.pack(anchor="w",padx=5,pady=5)

        campo_entrada5 = Entry(frame_esquerdo5,width = 35,bg='LightGray')
        campo_entrada5.pack(side=LEFT)

        
        ##
        botao_cadastrar_livro = Button(janela_livros, text = "Cadastrar", command=pegar_texto,bg='LightGray')
        botao_cadastrar_livro.pack(pady=20)
        
    # def apaga_livro_tk():



    janela_livros.mainloop()