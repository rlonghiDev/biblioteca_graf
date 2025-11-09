import time
import interfaces_io

## Recebe a avaliação e escreve no arquivo
def avaliacao(tipo,Registro,nota):
    # tipo 0 se for atendimento
    # tipo 1 se for livro

    ##Prepara os dados e escreve no arquivo 

    lista_para_escrever = str(tipo) + ',' + str(Registro) + ',' + str(nota) + '\n'
    
    interfaces_io.escreve_em_arquivo('avaliacao',lista_para_escrever,'a')
    #tipo_arquivo - Chamada do arquivo que receberá o conteúdo (destino);
    #conteudo_para_escrever - o conteudo que será inserido no arquivo
    #forma_escrita - 'a' para acrescentar e 'w' para substituir todo o conteúdo do arquivo de destino




def informa_media_avaliacao(tipo,Registro):
    
    # tipo => 0 se for sobre atendimento (Enviar int)
    # tipo => 1 se for sobre livro

    ## Registro => 0 se for sobre atendimento (Enviar int)
    ## Registro diferente de 0 para entregar a avaliação correspondente ao livro, Registro indica qual é o livro 
    
    interfaces_io.limpa_linha_em_branco('avaliacao')

    soma_notas_atendimento = 0
    soma_notas_livro = 0
    media_atendimento = 0
    media_livro = 0
    c1 = 0
    c2 = 0

    #Chama a funcaõ da leitura, envia tipo do arquivo e recebe na variaval ava
    ava = interfaces_io.le_arquivo('avaliacao')
    
    lista_int = []
    

    for linha in ava:
        linha = linha.replace('\n','')
        linha = linha.replace(" ","")
        linha = linha.strip()
        lista = linha.split(',')
        
        # Altera 
        for i in lista:
            i = i.strip()
            i = i.replace(" ","")
            i = int(i)
            lista_int.append(i)
            

        #identifica avaliação de atendimento
        if lista_int[0] == 0:
            soma_notas_atendimento += lista_int[2]
            c1 += 1

        #Identifica avaliação de livro

        if lista_int[0] == 1:
            if lista_int[1] == Registro:
                soma_notas_livro += lista_int[2]
                c2 += 1

        lista_int.clear()


    if tipo == 0:
        if soma_notas_atendimento > 0:
            media_atendimento = (soma_notas_atendimento / c1)
            media_atendimento = round(media_atendimento,2)
            return media_atendimento

    if tipo == 1:
        if soma_notas_livro > 0:
            media_livro = (soma_notas_livro/c2)
            media_livro = round(media_livro)
            return media_livro


# nota = informa_media_avaliacao(1,1)
# print(nota)

# def menu_avaliação_atendimento():
#     print("""
#           Olá !
#           Sua avaliação é muito importante para nós.
#           Digite abaixo sua opinião/avaliação sendo:
#           1 - Totalmente insatisfeito
#           5 - Atendimento espetacular
          
#           Se você deseja saber como anda nosso atedimento ...
#           Digite 6
#           """)
    
#     nota_atendimento = int(input("Digite aqui a sua nota\n"))
    
        
#     if nota_atendimento in range(1,6):
#         avaliacao(0,0,nota_atendimento)
#         return 'sucesso'
    
#     if nota_atendimento not in range(1,7):
#         print("Valor inválido, tente novamente")
#         time.sleep(3)
#         return 'erro'
    
#     if nota_atendimento == 6:
        
#         nota_media_atendimento = informa_media_avaliacao(0,0)
#         return nota_media_atendimento
    
    
    