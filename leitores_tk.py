from tkinter import *
import tkinter as tk
from tkinter import ttk
import json
import interfaces_io
import mensagem_aviso_tk
import opcoes_combobox
import datetime

def janela_leitores():
    
    def obter_selecao():

        #Captura seleção do combobox
        selecao = combobox.get()

        if selecao == 'Acrescentar':
            cadastro_tk()
            

        if selecao == 'Retirar':
            apaga_leitor_tk()


        if selecao == 'Voltar':
            janela_leitores.destroy()
        




    janela_leitores = Tk()
    janela_leitores.title("Leitores")
    janela_leitores['bg']=('white') 
    #janela_leitores.geometry('600x650+50+20')
    
    Etiqueta1 = Label(janela_leitores, height=3,width=50,fg = 'black', bg = 'white',text="Gerenciamento de Leitores",relief='groove')
    Etiqueta1.grid(row=0,column=0)
    
    Etiqueta2 = Label(janela_leitores, height=2, width=40, text = 'Escolha a função desejada abaixo')
    Etiqueta2.grid(row=1,column=0)
    
    ##Em branco
    Label(janela_leitores,text="", width=10,bg='white').grid(row=2, column=0)
    
    #### Combobox ####

    opcoes = ['Acrescentar','Retirar','Voltar']
    combobox = ttk.Combobox(janela_leitores, values=opcoes, state="readonly")
    combobox.set("Escolha uma opção") # Define o texto inicial
    combobox.grid(row=3, column=0)
    
    
    ##Em branco
    Label(janela_leitores,text="", width=10,bg='white').grid(row=4, column=0)

    # Criação do botão
    botao = tk.Button(janela_leitores, text="Escolha", command=obter_selecao)
    botao.grid(row=5, column=0)
    
     ##Em branco ###
    Label(janela_leitores,text="", width=10,bg='white').grid(row=6, column=0)
    

    def cadastro_tk():
        
        
        def pegar_texto():
            nome = campo_entrada1.get()
            escola = campo_entrada2.get()
            turma = campo_entrada3.get()
            ano = datetime.date.today().year
            registro = interfaces_io.procura_ultimo_registro('leitor')


            cad_leitor = {}
            cad_leitor['nome'] = nome
            cad_leitor['escola'] = escola
            cad_leitor['turma'] = turma
            cad_leitor['ano'] = ano
            cad_leitor['Registro'] = registro

            linha_str = json.dumps(cad_leitor)
            linha_str = "\n" + linha_str

            resultado = interfaces_io.escreve_em_arquivo('leitor',linha_str,'a')
            
            aviso = ('Processo de gravação do arquivo:',resultado)
            mensagem_aviso_tk.popup_aviso(aviso)
            
            
            #Limpa campos texto
            campo_entrada1.delete(0,tk.END)
            campo_entrada2.delete(0,tk.END)
            campo_entrada3.delete(0,tk.END)
            
            
        global frame_esquerdo
        frame_esquerdo = Frame(janela_leitores,bg='white')
        frame_esquerdo.grid(row=7,column=0)
        
        
        label_instr1 = Label(frame_esquerdo,text="Informe o nome do Leitor:",bg='white')
        label_instr1.grid(row=8,column=0)

        campo_entrada1 = Entry(frame_esquerdo,width = 35,bg='LightGray')
        campo_entrada1.grid(row=8,column=1)
        
        
        label_instr2 = Label(frame_esquerdo,text="Informe a escola:",bg='white')
        label_instr2.grid(row=9,column=0)

        campo_entrada2 = Entry(frame_esquerdo,width = 35,bg='LightGray')
        campo_entrada2.grid(row=9,column=1)
        
        
        label_instr3 = Label(frame_esquerdo,text="Informe a turma:",bg='white')
        label_instr3.grid(row=10,column=0)


        campo_entrada3 = Entry(frame_esquerdo,width = 35,bg='LightGray')
        campo_entrada3.grid(row=10,column=1)

        ##Em branco ###
        Label(frame_esquerdo,text="", width=10,bg='white').grid(row=11, column=0)
        
        botao_cadastrar_leitor = Button(frame_esquerdo, text = "Cadastrar", command=pegar_texto,bg='LightGray')
        botao_cadastrar_leitor.grid(row=12,column=1)

        
        ##Em branco ###
        Label(janela_leitores,text="", width=10,bg='white').grid(row=13, column=0)
        
   
    #Limpa a janela pra receber a nova função   
    def limpa_frame():
        # for widget in frame_esquerdo.winfo_children():
        #     widget.destroy()
        frame_esquerdo.destroy()
        
        
            

        
    def apaga_leitor_tk():
        
        limpa_frame()
        
        def obter_selecao_apaga():

            #Captura seleção do combobox
            
            selecao = combobox_apaga.get()

            posicao_hifen = selecao.find('-')
            inicio_string = selecao[:posicao_hifen]
            registro_para_apagar = ''
            
            for i in inicio_string:
                if i.isdigit():
                    registro_para_apagar += i
                    

            linhas_do_arquivo = interfaces_io.le_arquivo('leitor')
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
            
            retorno = interfaces_io.escreve_em_arquivo('leitor',linhas_do_arquivo_str,'w')
            
            if retorno == 'sucesso':
                mensagem_aviso_tk.popup_aviso('Leitor apagado com sucesso')
            
            if retorno == 'erro':
                mensagem_aviso_tk.popup_aviso('Falha ao apagar o leitor, tente novamente')
            
            
        opcoes = opcoes_combobox.carrega_opcoes('leitor')
        
        frame_esquerdo = Frame(janela_leitores,bg='white')
        frame_esquerdo.grid(row=7,column=0)
        
        combobox_apaga = ttk.Combobox(frame_esquerdo, values=opcoes, state="readonly")
        combobox_apaga.set("Escolha o leitor") # Define o texto inicial
        combobox_apaga.grid(row=7,column=0)
        
        ##Em branco ###
        Label(frame_esquerdo,text="", width=10,bg='white').grid(row=8, column=0)
        
        botao_apaga = tk.Button(frame_esquerdo, text="Apagar", command=obter_selecao_apaga)
        botao_apaga.grid(row=9,column=0)
        
        



    janela_leitores.mainloop()
    
#janela_leitores()