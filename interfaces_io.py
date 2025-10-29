def nome_arquivo(tipo_arquivo):

    if tipo_arquivo == 'livro':
        arquivo_para_abrir = "livros.txt"
    if tipo_arquivo == 'leitor':
        arquivo_para_abrir = "leitores.txt"
    if tipo_arquivo == 'emprestimo':
        arquivo_para_abrir = "emprestimos.txt"

    return arquivo_para_abrir



def le_arquivo(tipo_arquivo):

    arquivo_para_abrir = nome_arquivo(tipo_arquivo)

    with open(arquivo_para_abrir,"rt") as arq:
        linha = arq.readlines()

    arq.close()

    return linha



def escreve_em_arquivo(tipo_arquivo,conteudo_para_escrever):

    arquivo_para_escrever = nome_arquivo(tipo_arquivo)
    
    with open(arquivo_para_escrever,"w") as arq:
        arq.write(conteudo_para_escrever)
    arq.close()
    
    return



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

    print("Conteudo linhas",linhas)
    
    linhas_com_conteudo = []
    conteudo = ""
    
    for linha in linhas:
        if linha.strip():
            linhas_com_conteudo.append(linha)
            
        for linha in linhas_com_conteudo:
            conteudo += linha

    print("Conteudo a ser escrito",conteudo)

    escreve_em_arquivo(arquivo,conteudo)


limpa_linha_em_branco('emprestimo')
print(procura_ultimo_registro('emprestimo'))
