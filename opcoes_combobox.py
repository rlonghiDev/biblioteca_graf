import interfaces_io


opcoes = []

def carrega_opcoes(tipo_arquivo):
    
    arquivo_para_ler = interfaces_io.nome_arquivo(tipo_arquivo)
    
    #Busca informações do arquvivo de livros
    linhas_do_arquivo = interfaces_io.le_arquivo(tipo_arquivo)

    for linha in linhas_do_arquivo:
        posicao_inicial = linha.find(':')
        posicao_inicial += 1
        posicao_final = linha.find(',')
        
        
        titulo = linha[posicao_inicial:posicao_final]
        titulo = titulo.replace('"','')
        titulo = titulo.strip()
        
        #print(titulo,'\n',type(titulo),'\n\n')
        
        posicao1_registro = linha.find('Registro')
        posicao2_registro = linha.find('}')
        
        registro = ''
        final_da_string = linha[posicao1_registro:posicao2_registro]
        
        for i in final_da_string:
            if i.isdigit():
                registro += i
        
        
        opcao = registro + ' - ' + titulo
        
        opcoes.append(opcao)
        
    return opcoes



    
    
