

def apaga_leitor(registro):
    
    with open("leitores.txt","r") as leitores:
        linhas = leitores.readlines()
        
        leitores.close()
        
    for indice,linha in enumerate (linhas):
        print("Linha: ",linha, type(linha))
        pedaco_final = linha[-17:-1]
        
        print(pedaco_final.find(registro))
        
        if pedaco_final.find(registro) > -1:
            index_para_apagar = indice
            print(index_para_apagar)
            linhas.pop(index_para_apagar)
            break
        
        if pedaco_final.find(registro) <= -1:
            print("Registro de Leitor não localizado")
    
    
    with open("leitores.txt","wt") as leitores:
        leitores.writelines(linhas)
    leitores.close()

apaga_leitor('2')
        
        



# import relatorios

# def informa_media_avaliacao(tipo,Registro):
   
#     # tipo => 0 se for sobre atendimento 
#     # tipo => 1 se for sobre livro

#     ## Registro => 0 se for sobre atendimento 
#     ## Registro diferente de 0 para entregar a avaliação correspondente ao livro, Registro indica qual é o livro 
     
#     relatorios.limpa_linha_em_branco('avaliacao')

#     soma_notas_atendimento = 0
#     soma_notas_livro = 0
#     media_atendimento = 0
#     media_livro = 0
#     c1 = 0
#     c2 = 0

#     with open("avaliacao.txt", "r") as ava:
            

#         lista_int = []
            

#         for linha in ava:
#             linha = linha.replace('\n','')
#             linha = linha.replace(" ","")
#             linha = linha.strip()
#             lista = linha.split(',')
            
#             # Altera 
#             for i in lista:
#                 i = i.strip()
#                 i = i.replace(" ","")
#                 i = int(i)
#                 lista_int.append(i)

#             #identifica avaliação de atendimento
#             if lista_int[0] == 0:
#                 soma_notas_atendimento += lista_int[2]
#                 c1 += 1

#             #Identifica avaliação de livro

#             if lista_int[0] == 1:
#                 if lista_int[1] == Registro:
#                     soma_notas_livro += lista_int[2]
#                     c2 += 1

#             lista_int.clear()
#     ava.close()

#     if tipo == 0:
#         if soma_notas_atendimento > 0:
#             media_atendimento = (soma_notas_atendimento / c1)
#             print("Atendimento: ",round(media_atendimento,1))
#             return round(media_atendimento,1)

#     if tipo == 1:
#         if soma_notas_livro > 0:
#             media_livro = (soma_notas_livro/c2)
#             print("Livro: ",round(media_livro,1))
#             return round(media_livro,1)



                

            
            
    
    

# nota =  informa_media_avaliacao(0,0)
# print(nota)








# def avaliacao(tipo,Registro,nota):

#     ##Prepara os dados e escreve no arquivo 

#     lista_para_escrever = []
#     lista_para_escrever.append(tipo)
#     lista_para_escrever.append(int(Registro))
#     lista_para_escrever.append(int(nota))
#     lista_para_escrever = str(lista_para_escrever) + '\n'

#     with open("avaliacao.txt","at") as ava:

#       ava.write(lista_para_escrever)
    
#     ava.close()  



 































# import relatorios

# relatorios.relatorio_livros()
    
# def apaga_registro(registro_a_excluir):
    
#     registro_a_excluir = str(registro_a_excluir) #volta para string
#     Registro = "Registro: " + registro_a_excluir


#     with open ("livros.txt","r") as arq:
#         lista_de_linhas = arq.readlines()
        
#         arq.close() #Fecha arquivo
        
#         for indice,linha in enumerate(lista_de_linhas):
            
#             linha = linha.replace('"','')
#             linha = linha.replace("'","")
            
            
#             if Registro in linha:
#                 indice_para_excluir = indice
        
        
#         if type(indice_para_excluir) is int:
#             lista_de_linhas.pop(indice_para_excluir)
#             print("Livro apagado com sucesso")
            
#         else:
#             print("O Livro não foi localizado")
        
#     with open("livros.txt","w") as arq: #Abre arquivo modo escrita
            
#         for linha in lista_de_linhas:
#             linha.strip() # Tira eventuais espaços em branco no inicio ou final 
#             #linha = linha + '\n' #Coloca a próxima inserção na linha abaixo
#             arq.write(linha)
        
#         arq.close()
    


    
# ## Pergunta qual excluir

# registro_a_excluir = input("Digite o número do registro do livro a ser excluído\n")

# relatorios.limpa_linha_em_branco('livro')

# with open("livros.txt","r") as arq:
    
#     for linha in arq:
#         dicionario = eval(linha)
        
#         print("Registro a excluir: ", registro_a_excluir)
#         print(dicionario)
#         print(registro_a_excluir in dicionario)
#         print(type(dicionario))
        
#         registro_a_excluir = int(registro_a_excluir)
        
#         if dicionario['Registro'] == registro_a_excluir:
            
#             ficha = relatorios.monta_string_livro(dicionario)
            
#             print(ficha)

# #Fecha arquivo
# arq.close()

# acao = input("\nDeseja realmente apagar ? s/n\n")
# acao.lower()


# if acao == 's':
#     apaga_registro(registro_a_excluir)
    
# if acao == 'n':
#     exit(0)






    
    
# ## Apaga o registro
# Registro = "Registro: " + registro_a_excluir


# with open ("livros.txt","r") as arq:
#     lista_de_linhas = arq.readlines()
    
#     arq.close() #Fecha arquivo
    
#     for indice,linha in enumerate(lista_de_linhas):
        
#         linha = linha.replace('"','')
#         linha = linha.replace("'","")
        
        
#         if Registro in linha:
#             indice_para_excluir = indice
    
    
#     if type(indice_para_excluir) is int:
#         lista_de_linhas.pop(indice_para_excluir)
#         print("Livro apagado com sucesso")
        
#     else:
#         print("O Livro não foi localizado")
    
# with open("livros.txt","w") as arq: #Abre arquivo modo escrita
        
#     for linha in lista_de_linhas:
#         linha.strip() # Tira eventuais espaços em branco no inicio ou final 
#         #linha = linha + '\n' #Coloca a próxima inserção na linha abaixo
#         arq.write(linha)
    
#     arq.close()
    













# import datetime

# def busca_info(Registro, tipo):
    
#     arquivo_para_ler = ''  
    
#     if tipo == 'leitor':
#         arquivo_para_ler = "leitores.txt"
        
#     if tipo == 'livro':
#         arquivo_para_ler = "livros.txt"
        
#     if tipo == 'emprestimo':
#         arquivo_para_ler = "emprestimos.txt"
        
#     with open(arquivo_para_ler,"r") as arq:
        
#         for linha in arq:
#             dicionario = eval(linha)
        
#             procura = str(dicionario['Registro'])
#             procura = procura.strip()
#             Registro = Registro.strip()
            
#             if procura == Registro:
#                 nome = dicionario
#                 break
                
#             else:
#                 nome = "Nao localizado"
    
#     arq.close()#Fecha arquivo            
    
    
#     print("O que foi captado:",nome)

# Registro = '9'
# tipo = 'emprestimo'

# busca_info(Registro, tipo)










# Registro = '"Registro": 2'
# indice_para_apagar = ''

# with open("emprestimos.txt","r") as arq: #Abre arquivo no modo leitura
#     lista_de_linhas = arq.readlines()
    
#     arq.close() #Fecha arquivo
    
#     for indice,linha in enumerate(lista_de_linhas):
#         if Registro in linha:
#             indice_para_apagar = indice
        
#     print(type(indice_para_apagar))        
#     ##Remove emprestimo localizado se o registro foi localizado
#     if type(indice_para_apagar) is int:
#         lista_de_linhas.pop(indice_para_apagar)
#         print("Empréstimo encerrado com sucesso")
#     else:
#         print("Empréstimo não foi localizado")
    
# with open("emprestimos.txt","w") as arq: #Abre arquivo modo escrita
        
#     for linha in lista_de_linhas:
#         linha.strip() # Tira eventuais espaços em branco no inicio ou final 
#         #linha = linha + '\n' #Coloca a próxima inserção na linha abaixo
#         arq.write(linha)
    
#     arq.close()
    
        
        
    
    
    
    
    
            







# import json

# def confirma_cadastro(tipo_confirmacao):
    
#     if tipo_confirmacao == 'livro':
#         arquivo_a_ser_lido = 'livros.txt'
    
#     if tipo_confirmacao == 'leitor':
#         arquivo_a_ser_lido = 'leitores.txt'
        
#     if tipo_confirmacao == 'emprestimo':
#         arquivo_a_ser_lido = 'emprestimos.txt'
    
    
    
    
#     with open(arquivo_a_ser_lido,"r") as arq:
#         linha = arq.readlines()

#         arq.close()
    
#     registro = linha[-1].strip()
    
#     return json.loads(registro) 



####### Formatação de Data #####
# from datetime import date
            
# hoje_BD = date.today()
# hoje_BD = str(hoje_BD)
# print(hoje_BD)
# ano = hoje_BD[0:4]
# mes = hoje_BD[5:7]
# dia = hoje_BD[8:10]
# print(f"{dia}/{mes}/{ano}")





## Relatório Livro ##

# def monta_string(dict):
#     linha1 = '#' * 50
#     espacamento = '#' + ' ' * 48 + '#'
#     str21 = 'Título: ' # String [linha2] [posição1]
#     str22 = dict['nome'] # String [linha2] [posição1]
#     linha2 = '#' + str21.rjust(24) + str22.ljust(24) + '#'
#     str31 = 'Autor: '
#     str32 = dict['autor']
#     linha3 = '#' + str31.rjust(24) + str32.ljust(24) + '#'
#     str41 = 'Disponível: '
#     str42 = str(dict['Qde_disp'])
#     linha4 = '#' + str41.rjust(24) + str42.ljust(24) + '#'
#     str51 = 'Registro: '
#     str52 = str(dict['Registro'])
#     linha5 = '#' + str51.rjust(24) + str52.ljust(24) + '#'

#     ficha = (linha1 +'\n'+ espacamento + '\n' + linha2 + '\n' + linha3 + '\n' + linha4 + '\n' + linha5 + '\n' + espacamento + '\n' + linha1 + '\n')
#     return ficha


# with open("livros.txt","r") as arq:
    
#     for linha in arq:
#         dicionario = eval(linha)
#         ficha = monta_string(dicionario)
            
#         print(ficha)
            
        



        
# #tabulate

# arq.close()


# string_customizada = "nome:Charlie,idade:35,cidade:Nova York"
# # Divide a string em pares chave:valor e depois em chave e valor
# meu_dicionario = {chave.strip(): valor.strip() for item in string_customizada.split(',') for chave, valor in [item.split(':')]}

# print(meu_dicionario)
# print(type(meu_dicionario))






# import datetime

# nome = input("Digite o nome do Leitor")
# escola = input("Informe qual escola está matriculado")
# turma = input("Informe o curso que o leitor está inscrito")
# ano_cadastro = datetime.date.today().year
# registro_leitor = ''

# leitor ={}
# leitor['nome']=nome
# leitor['escola']=escola
# leitor['turma'] = turma
# leitor['ano']=ano_cadastro
# leitor['Registro'] = registro_leitor

# leitor_str = str(leitor) + '\n'

# with open("leitores.txt","at") as arq:
#      arq.write(leitor_str)

# arq.close()








# with open("livros.txt","r") as arq:
#     linha = arq.readlines()

# arq.close()

# if linha:
#     registro = linha[-1].strip()
# else:
#     registro = 'falhou'
#     print(registro)


# print(type(registro))

# posicao = registro.find('Registro')
# tamanho = len(registro)

# reg = '0'
# trecho_inteiro = registro[posicao:tamanho]
# for i in trecho_inteiro:
#     if i.isdigit():
#         reg += i


# valor = int(reg) + 1


# print("Registro:", valor)

