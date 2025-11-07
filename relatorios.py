import avaliacao


#### Limpa linha em branco #####

def limpa_linha_em_branco(arquivo):
    
    if arquivo == "leitor":
        arquivo_para_abrir = "leitores.txt"
    
    if arquivo == "livro":
        arquivo_para_abrir = "livros.txt"
        
    if arquivo == "emprestimo":
        arquivo_para_abrir = "emprestimos.txt"
        
    if arquivo == "avaliacao":
        arquivo_para_abrir = "avaliacao.txt"
        
    with open(arquivo_para_abrir, "r") as arq: #modo leitura
        linhas = arq.readlines()
    arq.close()
        
    linhas_com_conteudo = []
    
    for linha in linhas:
        if linha.strip():
            linhas_com_conteudo.append(linha)
            
    
    with open(arquivo_para_abrir,"w") as arq:
        for linha in linhas_com_conteudo:
            arq.write(linha)
    
    arq.close()
    

def monta_string_leitor(dict):
        linha1 = '#' * 44
        espacamento = '#' + ' ' * 42 + '#'
        str21 = 'Nome: ' # String [linha2] [posição1]
        str22 = dict['nome'] # String [linha2] [posição1]
        linha2 = '#' + str21.rjust(21) + str22.ljust(21) + '#'
        str31 = 'Escola: '
        str32 = dict['escola']
        linha3 = '#' + str31.rjust(21) + str32.ljust(21) + '#'
        str41 = 'Turma: '
        str42 = str(dict['turma'])
        linha4 = '#' + str41.rjust(21) + str42.ljust(21) + '#'
        str51 = 'Registro: '
        str52 = str(dict['Registro'])
        linha5 = '#' + str51.rjust(21) + str52.ljust(21) + '#'
        str61 = 'Ano: '
        str62 = str(dict['ano'])
        linha6 = '#' + str61.rjust(21) + str62.ljust(21) + '#'

        ficha = (linha1 +'\n'+ espacamento + '\n' + linha2 + '\n' + linha3 + '\n' + linha4 + '\n' + linha5 + '\n' + linha6 + '\n' + espacamento + '\n' + linha1 + '\n')
        return ficha


   
def relatorio_leitores():
    
    limpa_linha_em_branco('leitor') #Função para eliminar linhas em branco
    
    with open("leitores.txt","r") as arq:
        
        for linha in arq:
            dicionario = eval(linha)
            ficha = monta_string_leitor(dicionario)
                
            print(ficha)
        
        arq.close()#Fecha arquivo

##### Relatorio Livro #####

def monta_string_livro(dict):
        linha1 = '#' * 44
        espacamento = '#' + ' ' * 42 + '#'
        str21 = 'Título: ' # String [linha2] [posição1]
        str22 = dict['nome'] # String [linha2] [posição1]
        linha2 = '#' + str21.rjust(21) + str22.ljust(21) + '#'
        str31 = 'Autor: '
        str32 = dict['autor']
        linha3 = '#' + str31.rjust(21) + str32.ljust(21) + '#'
        str41 = 'Disponível: '
        str42 = str(dict['Qde_disp'])
        linha4 = '#' + str41.rjust(21) + str42.ljust(21) + '#'
        str51 = 'Registro: '
        str52 = str(dict['Registro'])
        linha5 = '#' + str51.rjust(21) + str52.ljust(21) + '#'
        str61 = 'Avaliação: '
        int62a = avaliacao.informa_media_avaliacao(1,dict['Registro'])
        int62a = int(int62a)
        str62 =   (int62a * '|*')
        str62a = str(str62)
        linha6 = '#' + str61.rjust(21) + str62a.ljust(21) + '#'

        ficha = (linha1 + '\n' + espacamento + '\n' + linha2 + '\n' + linha3 + '\n' + linha4 + '\n' + linha5 + '\n' + linha6 + '\n' +  espacamento + '\n' +  linha1 + '\n')
        
        return ficha


   
def relatorio_livros():
    
    limpa_linha_em_branco('livro')
    
    with open("livros.txt","r") as arq:
        
        for linha in arq:
            dicionario = eval(linha)
            ficha = monta_string_livro(dicionario)
                
            print(ficha)
        
    arq.close()#Fecha arquivo




##### Relatório de Empréstimo #####


def busca_info(Registro, tipo, chamada):
    
    arquivo_para_ler = ''  
    
    if tipo == 'leitor':
        arquivo_para_ler = "leitores.txt"
        
    if tipo == 'livro':
        arquivo_para_ler = "livros.txt"
        
    if tipo == 'emprestimo':
        arquivo_para_ler = "emprestimos.txt"
    
    with open(arquivo_para_ler,"r") as arq:
        
        for linha in arq:
            dicionario = eval(linha)
            
            procura = str(dicionario['Registro'])
            procura = procura.strip()
            Registro = str(Registro)
            Registro = Registro.strip()
            
            if procura == Registro and chamada == 1:
                nome = dicionario
                break
            
            if procura == Registro and chamada == 0:
                nome = dicionario["nome"]
                break
                
            else:
                nome = "Nao localizado"
    
    arq.close()#Fecha arquivo            
    

    return nome


    

#### String Emprestimo ####

def monta_string_emprestimo(dict):
    linha1 = '#' * 44
    espacamento = '#' + ' ' * 42 + '#'
    titulo = 'EMPRESTIMO DE LIVRO'
    linha1a = '#' + titulo.center(42) + '#'
    str21 = 'Leitor: ' # String [linha2] [posição1]
    str22 = busca_info(int(dict["leitor"]),"leitor",0)
    linha2 = '#' + str21.rjust(21) + str22.ljust(21) + '#'
    str31 = 'livro: '
    str32 = busca_info(int(dict["livro"]),"livro",0)
    linha3 = '#' + str31.rjust(21) + str32.ljust(21) + '#'
    str41 = 'Emprestado em: '
    str42 = str(dict["data"])
    linha4 = '#' + str41.rjust(21) + str42.ljust(21) + '#'
    str51 = 'Registro: '
    str52 = str(dict['Registro'])
    linha5 = '#' + str51.rjust(21) + str52.ljust(21) + '#'

    ficha = (linha1 +'\n'+ espacamento + '\n' + linha1a + '\n' + linha2 + '\n' + linha3 + '\n' + linha4 + '\n' + linha5 + '\n' + espacamento + '\n' + linha1 + '\n')
    
    return ficha


def relatorio_emprestimo():
    
    limpa_linha_em_branco('emprestimo')
    
    with open("emprestimos.txt","r") as arq:
        
        for linha in arq:
            dicionario = eval(linha)
            ficha = monta_string_emprestimo(dicionario)
                
            print(ficha)
        
    arq.close()#Fecha arquivo

    
    
    
    




