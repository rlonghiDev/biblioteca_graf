import json

def nome_arquivo(tipo_arquivo):

    if tipo_arquivo == 'livro':
        arquivo_para_abrir = "livros.txt"
    if tipo_arquivo == 'leitor':
        arquivo_para_abrir = "leitores.txt"
    if tipo_arquivo == 'emprestimo':
        arquivo_para_abrir = "emprestimos.txt"
    if tipo_arquivo == 'avaliacao':
        arquivo_para_abrir = "avaliacao.txt"

    return arquivo_para_abrir



def le_arquivo(tipo_arquivo):
    
    try:
        arquivo_para_abrir = nome_arquivo(tipo_arquivo)

        with open(arquivo_para_abrir,"rt") as arq:
            linha = arq.readlines()

        arq.close()

        return linha

    except Exception as e:
        
        print("Erro na leitura do arquivo:",e)
        
        return



def escreve_em_arquivo(tipo_arquivo,conteudo_para_escrever,forma_escrita):

    try:
    
        arquivo_para_escrever = nome_arquivo(tipo_arquivo)
        
        with open(arquivo_para_escrever, forma_escrita) as arq:
            arq.write(conteudo_para_escrever)
        arq.close()
        
        return 
    
    except Exception as e:
        print("Erro na escrita do arquivo:",e)



def procura_ultimo_registro(tipo_procura):
        
        linha = le_arquivo(tipo_procura)    
        
        if linha:
            registro = linha[-1].strip()
        else:
            registro = '1'

        posicao = registro.find('Registro')
        tamanho = len(registro)
        

        reg = '0'
        trecho_final = registro[posicao:tamanho]
        for i in trecho_final:
            if i.isdigit():
                reg += i

        valor = int(reg) + 1 #Incrementa valor para a próxima entrada
        return valor


def limpa_linha_em_branco(arquivo):
        
    linhas = le_arquivo(arquivo)

    linhas_com_conteudo = []
    conteudo = ""
    
    for linha in linhas:
        
        if linha.strip():
            linhas_com_conteudo.append(linha)
            
    for linha in linhas_com_conteudo:
        conteudo += str(linha)

    escreve_em_arquivo(arquivo,conteudo,'w')


