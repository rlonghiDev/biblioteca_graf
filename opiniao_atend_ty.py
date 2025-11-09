from tkinter import *
import tkinter as tk
from tkinter import ttk
import avaliacao
import comentario_registros

janela_atend = Tk()
janela_atend.title("Avaliação")
janela_atend['bg']=('white') 
Etiqueta1 = Label(janela_atend, height=3,width=50, fg = 'black', bg = 'white', text="Opinião sobre o Atendimento",relief='groove')
Etiqueta1.grid(row=0,column=0,columnspan=2)
Etiqueta2 = Label(janela_atend, height=2, width=40, text = 'Verifique a nota e veja os comentários')
Etiqueta2.grid(row=1,column=0,columnspan=2)

 ##Em branco
Label(janela_atend,text="", width=10,bg='white').grid(row=2, column=0,columnspan=2)



nota_var = tk.StringVar()
nota_var.set("10")

nota = avaliacao.informa_media_avaliacao(0,0)
nota_str = 'NOTA: '
nota_str += str(nota)

def configura_nota():
    nota_var.set(nota_str)
    

#Nota
label_nota = tk.Label(janela_atend, textvariable=nota_var, width=10,bg='white').grid(row=3, column=0,columnspan=2)
configura_nota()


##Em branco
Label(janela_atend,text="", width=10,bg='white').grid(row=4, column=0)

## Ver comentarios (implementar)




#Botao de encerramento + escrever comentário
def fechar_janela():
    janela_atend.destroy()
    
def chama_comentar():
    comentario_registros.comentario_recebe()

botao_fechar = tk.Button(janela_atend, text="Fechar", command=fechar_janela)
botao_fechar.grid(row=5,column=0)

botao_comentario = tk.Button(janela_atend,text="Comente", command=chama_comentar)
botao_comentario.grid(row=5,column=1)

##Em branco
Label(janela_atend,text="", width=10,bg='white').grid(row=6, column=0, columnspan=2)

janela_atend.mainloop()

