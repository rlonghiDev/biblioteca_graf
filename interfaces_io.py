import mensagem_aviso_tk


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
        
        #limpa_linha_em_branco(tipo_arquivo)

        with open(arquivo_para_abrir,"r") as arq:
            linhas = arq.readlines()

        arq.close()
        
        return linhas #Todas as linhas do arquivo

    except Exception as e:
        
        aviso = ("Erro na leitura do arquivo:",e)
        mensagem_aviso_tk.popup_aviso(aviso)
        
        return



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





def escreve_em_arquivo(tipo_arquivo,conteudo_para_escrever,forma_escrita):
    #tipo_arquivo - Chamada do arquivo que receberá o conteúdo (destino);
    #conteudo_para_escrever - o conteudo que será inserido no arquivo
    #forma_escrita - 'a' para acrescentar e 'w' para substituir todo o conteúdo do arquivo de destino

    try:
    
        arquivo_para_escrever = nome_arquivo(tipo_arquivo)
        
        with open(arquivo_para_escrever, forma_escrita) as arq:
            arq.write(conteudo_para_escrever)
        arq.close()
        
        return 'sucesso'
    
    except Exception as e:
        aviso_mensagem = ("Erro na escrita do arquivo:",e)
        mensagem_aviso_tk.popup_aviso(aviso_mensagem)
        return 'erro'


def procura_ultimo_registro(tipo_procura):
        
    limpa_linha_em_branco(tipo_procura)
    
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







