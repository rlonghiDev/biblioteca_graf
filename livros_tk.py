from tkinter import *
import tkinter as tk
from tkinter import ttk
import json
import interfaces_io
import mensagem_aviso_tk
import opcoes_combobox



def janela_livros():
    
    def obter_selecao():

        #Captura seleção do combobox
        selecao = combobox.get()

        if selecao == 'Acrescentar':
            cadastro_tk()
            

        if selecao == 'Retirar':
            apaga_livro_tk()


        if selecao == 'Voltar':
            janela_livros.destroy()
        




    janela_livros = Tk()
    janela_livros.title("Livros")
    janela_livros['bg']=('white') 
    janela_livros.geometry('600x650+50+20')
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
            
            aviso = ('Processo de gravação do arquivo:',resultado)
            mensagem_aviso_tk.popup_aviso(aviso)
            
            
            #Limpa campos texto
            campo_entrada1.delete(0,tk.END)
            campo_entrada2.delete(0,tk.END)
            campo_entrada3.delete(0,tk.END)
            campo_entrada4.delete(0,tk.END)
            campo_entrada5.delete(0,tk.END)
            

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
        
        
        
    def apaga_livro_tk():
        
        def obter_selecao_apaga():

            #Captura seleção do combobox
            
            selecao = combobox_apaga.get()

            posicao_hifen = selecao.find('-')
            inicio_string = selecao[:posicao_hifen]
            registro_para_apagar = ''
            
            for i in inicio_string:
                if i.isdigit():
                    registro_para_apagar += i
                    

            linhas_do_arquivo = interfaces_io.le_arquivo('livro')
            registro_na_linha = ''
            
            for indice,linha in enumerate(linhas_do_arquivo):
                posicao_registro = linha.find('Registro')
                final_string = linha[posicao_registro:]
                for i in final_string:
                    if i.isdigit():
                        registro_na_linha += i
                
                if registro_para_apagar == registro_na_linha:
                    indice_para_apagar = indice
                else:
                    registro_na_linha = ''
                
                
                    
            del linhas_do_arquivo[indice_para_apagar]
            
            linhas_do_arquivo_str = ''
            
            for l in linhas_do_arquivo:
                linhas_do_arquivo_str += l
            
            retorno = interfaces_io.escreve_em_arquivo('livro',linhas_do_arquivo_str,'w')
            
            if retorno == 'sucesso':
                mensagem_aviso_tk.popup_aviso('Livro apagado com sucesso')
            
            if retorno == 'erro':
                mensagem_aviso_tk.popup_aviso('Falha ao apagar o livro, tente novamente')
            
            
        opcoes = opcoes_combobox.carrega_opcoes('livro')
        
        frame_esquerdo = Frame(janela_livros,bg='white')
        frame_esquerdo.pack(anchor="w",padx=200,pady=25)
        
        combobox_apaga = ttk.Combobox(frame_esquerdo, values=opcoes, state="readonly")
        combobox_apaga.set("Escolha o livro") # Define o texto inicial
        combobox_apaga.pack(pady=10)
        
        
        botao_apaga = tk.Button(frame_esquerdo, text="Apagar", command=obter_selecao_apaga)
        botao_apaga.pack(pady=10)
        
        



    janela_livros.mainloop()
    
