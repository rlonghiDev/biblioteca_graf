import tkinter as tk
from tkinter import messagebox


def popup_aviso(mensagem):
    
    janela_popup = tk.Tk()
    janela_popup.withdraw()#oculta janela principal
    
    messagebox.showwarning("Aviso",mensagem)
    
    def fecha_popup():
        janela_popup.destroy()
    
    botao = tk.Button(janela_popup, text="Fechar", command=fecha_popup)
    botao.pack(pady=10)