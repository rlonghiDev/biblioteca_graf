import json

def confirma_cadastro(tipo_confirmacao):
    
    if tipo_confirmacao == 'livro':
        arquivo_a_ser_lido = 'livros.txt'
    
    if tipo_confirmacao == 'leitor':
        arquivo_a_ser_lido = 'leitores.txt'
        
    if tipo_confirmacao == 'emprestimo':
        arquivo_a_ser_lido = 'emprestimos.txt'
    
    
    
    
    with open(arquivo_a_ser_lido,"r") as arq:
        linha = arq.readlines()

        arq.close()
    
    registro = linha[-1].strip()
    
    return json.loads(registro) 
            