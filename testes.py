import tkinter as tk

def atualizar_contagem(event):
    """
    Função chamada a cada tecla pressionada para atualizar a contagem.
    """
    # Obtém o texto completo do widget Text, excluindo o caractere de nova linha extra que o widget adiciona.
    # O índice '1.0' significa linha 1, caractere 0 (início).
    # O índice 'end-1c' significa o final, menos 1 caractere (o '\n' oculto).
    texto = campo_texto.get("1.0", "end-1c")
    
    # Usa a função len() do Python para contar os caracteres na string.
    quantidade = len(texto)
    
    # Atualiza o texto do Label com a nova contagem
    label_contagem.config(text=f"Caracteres: {quantidade}")

# Configuração da janela principal
root = tk.Tk()
root.title("Contador de Caracteres")
root.geometry("400x300")

# Widget Label para exibir a contagem
label_contagem = tk.Label(root, text="Caracteres: 0")
label_contagem.pack(pady=10)

# Widget Text para entrada de texto
campo_texto = tk.Text(root, wrap=tk.WORD, width=40, height=10)
campo_texto.pack(padx=10, pady=10)

# Vincula o evento de liberação de tecla (<KeyRelease>) à função de contagem
# Isso garante que a contagem seja atualizada após cada caractere ser inserido ou removido.
campo_texto.bind("<KeyRelease>", atualizar_contagem)

# Loop principal da aplicação
root.mainloop()


