import avaliacao

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


# def monta_string_leitor(dict_leitor):
        