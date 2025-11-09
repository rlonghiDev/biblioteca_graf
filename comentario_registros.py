from tkinter import *
import tkinter as tk
import interfaces_io
import mensagem_aviso_tk


def comentario_recebe(Registro = 0):
    janela_comment = Tk()
    janela_comment.title("Avaliação")
    janela_comment['bg']=('white') 
    Etiqueta1 = Label(janela_comment, height=3,width=50, fg = 'black', bg = 'white', text="Opinião sobre o Atendimento",relief='groove')
    Etiqueta1.grid(row=0,column=0,columnspan=2)
    Etiqueta2 = Label(janela_comment, height=2, width=40, text = 'Deixe seu comentário abaixo')
    Etiqueta2.grid(row=1,column=0,columnspan=2)
    
    ##Em branco
    Label(janela_comment,text="", width=10,bg='white').grid(row=2, column=0,columnspan=2)
    
    ##
    def atualizar_contagem(event):
        """
        Função chamada a cada tecla pressionada para atualizar a contagem.
        """
        # Obtém o texto completo do widget Text, excluindo o caractere de nova linha extra que o widget adiciona.
        # O índice '1.0' significa linha 1, caractere 0 (início).
        # O índice 'end-1c' significa o final, menos 1 caractere (o '\n' oculto).
        texto = campo_texto.get("1.0", "end-1c")
        
        # Usa a função len() do Python para contar os caracteres na string.
        quantidade = 201 - len(texto)
        
        # Atualiza o texto do Label com a nova contagem
        label_contagem.config(text=f"Caracteres: {quantidade}")
        
        limite = 200
        
        if len(texto) > limite:
            # Se o comprimento exceder o limite, apaga os caracteres excedentes.
            # Começa a apagar do índice do limite até o final ("end").
            event.widget.delete(f"1.{limite}", "end")
        

    
    ##
    #Entrada de texto
    campo_texto = tk.Text(janela_comment,wrap=tk.WORD, width=50,height=5,borderwidth=5)
    campo_texto.grid(row=3,column=0,columnspan=2)
    
    # Vincula o evento de liberação de tecla (<KeyRelease>) à função de contagem
    # Isso garante que a contagem seja atualizada após cada caractere ser inserido ou removido.
    campo_texto.bind("<KeyRelease>", atualizar_contagem)

    ##Em branco
    Label(janela_comment,text="", width=10,bg='white').grid(row=4, column=0,columnspan=2)

    # Widget Label para exibir a contagem
    label_contagem = tk.Label(janela_comment, text="Caracteres: 200")
    label_contagem.grid(row=5,column=1)
    
    label_aviso = tk.Label(janela_comment,text="Limite máximo 200 caracteres")
    label_aviso.grid(row=5,column=0)
    
    ##Em branco
    Label(janela_comment,text="", width=10,bg='white').grid(row=6, column=0,columnspan=2,rowspan=2)
    
    def fecha_janela():
        janela_comment.destroy()
        
    botao_termina = tk.Button(janela_comment,text="Termina",command=fecha_janela)
    botao_termina.grid(row=8,column=0)
    
    def captura_comentario():
        conteudo_comentario = campo_texto.get('1.0',tk.END)
        return conteudo_comentario
        
    Registro = str(Registro)
    
    def grava_comentario():
        
        comentario = captura_comentario()
        conteudo = Registro + ',' + comentario + '\n'
        
        resultado = interfaces_io.escreve_em_arquivo('comentario',conteudo,'a')
        interfaces_io.limpa_linha_em_branco('comentario')
        mensagem_aviso_tk.popup_aviso(resultado)
        
    
    
    botao_grava = tk.Button(janela_comment,text="Grava",command=grava_comentario)
    botao_grava.grid(row=8,column=1)
    
    ##Em branco
    Label(janela_comment,text="", width=10,bg='white').grid(row=9, column=0,columnspan=2,rowspan=2)
    
    
    

    janela_comment.mainloop()
    