import avaliacao
import interfaces_io
import json

def monta_string_livro(dict):
        linha1 = '#' * 44
        espacamento = '#' + ' ' * 42 + '#'
        str21 = 'Título: ' # String [linha2] [posição1]
        str22 = dict['titulo'] # String [linha2] [posição1]
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


def busca_info(Registro, tipo, chamada):
    
        
        arq = interfaces_io.le_arquivo(tipo)
        
        for linha in arq:
                
            #Transforma a linha string em dicionario    
            dicionario = json.loads(linha)
    
            
            procura = str(dicionario['Registro'])
            procura = procura.strip()
            Registro = str(Registro)
            Registro = Registro.strip()
            
            if procura == Registro and chamada == 1:
                nome = dicionario
                break
            
            if procura == Registro and chamada == 0 and tipo == 'livro':
                nome = dicionario["titulo"]
                break
            
            if procura == Registro and chamada == 0 and tipo == 'leitor':
                nome = dicionario["nome"]
                break
                
            else:
                nome = "Nao localizado"            
    

        return nome


def monta_string_emprestimo(dict):
    linha1 = '#' * 44
    espacamento = '#' + ' ' * 42 + '#'
    titulo = 'EMPRESTIMO DE LIVRO'
    linha1a = '#' + titulo.center(42) + '#'
    str21 = 'Leitor: ' # String [linha2] [posição1]
    str22 = busca_info(int(dict['leitor']),"leitor",0)
    linha2 = '#' + str21.rjust(21) + str22.ljust(21) + '#'
    str31 = 'livro: '
    str32 = busca_info(int(dict['livro']),"livro",0)
    linha3 = '#' + str31.rjust(21) + str32.ljust(21) + '#'
    str41 = 'Emprestado em: '
    str42 = str(dict["data"])
    linha4 = '#' + str41.rjust(21) + str42.ljust(21) + '#'
    str51 = 'Registro: '
    str52 = str(dict['Registro'])
    linha5 = '#' + str51.rjust(21) + str52.ljust(21) + '#'

    ficha = (linha1 +'\n'+ espacamento + '\n' + linha1a + '\n' + linha2 + '\n' + linha3 + '\n' + linha4 + '\n' + linha5 + '\n' + espacamento + '\n' + linha1 + '\n')
    
    return ficha



   
        