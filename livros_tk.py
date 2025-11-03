from tkinter import *
import tkinter as tk
from tkinter import ttk
import json
import interfaces_io
import mensagem_aviso_tk
import opcoes_combobox
import avaliacao



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
    #janela_livros.geometry('600x650+50+20')
    Etiqueta1 = Label(janela_livros, height=3,width=50,fg = 'black', bg = 'white',text="Gerenciamento do Acervo de Livros",relief='groove')
    Etiqueta1.grid(row=0,column=0)
    Etiqueta2 = Label(janela_livros, height=2, width=40, text = 'Escolha a função desejada abaixo')
    Etiqueta2.grid(row=1,column=0)
   
   
    ##Em branco
    Label(text="", width=10,bg='white').grid(row=2, column=0)
               
    #### Combobox ####
    opcoes = ['Acrescentar','Retirar','Voltar']
    combobox = ttk.Combobox(janela_livros, values=opcoes, state="readonly")
    combobox.set("Escolha uma opção") # Define o texto inicial
    combobox.grid(row=3,column=0)

    ##Em branco
    Label(text="", width=10,bg='white').grid(row=4, column=0)
               
    
    
    # Criação do botão
    botao = tk.Button(janela_livros, text="Escolha", command=obter_selecao)
    botao.grid(row=5,column=0)
    

    def cadastro_tk():
        
        
        def pegar_texto():
            titulo = campo_entrada1.get()
            autor = campo_entrada2.get()
            qde_disp = campo_entrada3.get()
            qde_uso = campo_entrada4.get()
            registro = interfaces_io.procura_ultimo_registro('livro')
            nota1 = campo_entrada5.get()
            avaliacao.avaliacao(1,registro,nota1)
            nota = avaliacao.informa_media_avaliacao(1,registro)
            


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
            
            
        global frame_cadastra
        frame_cadastra=Frame(janela_livros,bg='white')
        frame_cadastra.grid(row=6,column=0)
        
        label_instr1 = Label(frame_cadastra,text="Informe o título do Livro:",bg='white',justify=RIGHT)
        label_instr1.grid(row=6,column=0)

        campo_entrada1 = Entry(frame_cadastra,width = 35,bg='LightGray')
        campo_entrada1.grid(row=6,column=1)
        
        ##
    
        label_instr2 = Label(frame_cadastra,text="Informe o autor:",bg='white',justify=RIGHT)
        label_instr2.grid(row=7,column=0)

        campo_entrada2 = Entry(frame_cadastra,width = 35,bg='LightGray')
        campo_entrada2.grid(row=7,column=1)
        
        
        ##
        
        
        label_instr3 = Label(frame_cadastra,text="Disponíveis:",bg='white',justify='right')
        label_instr3.grid(row=8,column=0)

        campo_entrada3 = Entry(frame_cadastra,width = 35,bg='LightGray')
        campo_entrada3.grid(row=8,column=1)
        
        
        ##        
        
        label_instr4 = Label(frame_cadastra,text="Em uso:",bg='white',justify=tk.RIGHT)
        label_instr4.grid(row=9,column=0)

        campo_entrada4 = Entry(frame_cadastra,width = 35,bg='LightGray')
        campo_entrada4.grid(row=9,column=1)

        ##
        
        label_instr5 = Label(frame_cadastra,text="Nota (de 1 a 5):",bg='white')
        label_instr5.grid(row=10,column=0)

        campo_entrada5 = Entry(frame_cadastra,width = 35,bg='LightGray')
        campo_entrada5.grid(row=10,column=1)

        ##Em branco
        Label(frame_cadastra,text="", width=10,bg='white').grid(row=11, column=0)
        ##
        botao_cadastrar_livro = Button(frame_cadastra, text = "Cadastrar", command=pegar_texto,bg='LightGray')
        botao_cadastrar_livro.grid(row=11,column=1)
        
        ##Em branco
        Label(frame_cadastra,text="", width=10,bg='white').grid(row=12, column=0)
        
    def apaga_frame_cadastra():
        frame_cadastra.destroy()
    
   
   
   
    def apaga_livro_tk():
        
        apaga_frame_cadastra()
        
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
            
        
        
        
        global frame_apaga
        frame_apaga = Frame(janela_livros,bg='white')
        frame_apaga.grid(row=6,column=0)
        
        ##Em branco
        Label(frame_apaga,text="", width=10,bg='white').grid(row=6, column=0)
        
        
        
        opcoes = opcoes_combobox.carrega_opcoes('livro')
        combobox_apaga = ttk.Combobox(frame_apaga, values=opcoes, state="readonly")
        combobox_apaga.set("Escolha o livro") # Define o texto inicial
        combobox_apaga.grid(row=7,column=0)
        
        ##Em branco
        Label(text="", width=10,bg='white').grid(row=8, column=0)
        
        ##Botão
        botao_apaga = tk.Button(frame_apaga, text="Apagar", command=obter_selecao_apaga)
        botao_apaga.grid(row=9,column=0)
        
        
        ##Em branco
        Label(frame_apaga,text="", width=10,bg='white').grid(row=10, column=0)


    janela_livros.mainloop()

janela_livros()