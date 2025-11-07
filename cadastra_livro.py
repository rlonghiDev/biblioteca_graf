import ultimo_registro
import confirma
import relatorios
import avaliacao
import json

def cadastrar_livro():

    #Produra o último registro de livro para partir determinar próximo registro.
    num_registro = ultimo_registro.procura_ultimo_registro("livro")

    #Recebe os dados do livro 
    nome = input("Digite o nome do livro\n")
    autor = input("Digite o nome do autor\n")
    qde_disp = int(input("Digite a quantidade disponível do livro\n"))
    qde_uso = 0
    nota = int(input("Digite a sua avaliação do livro de 0 a 5\n"))
    avaliacao.avaliacao(1,num_registro,nota)
    
    ## Coloca as informações no dicionário ##
    livro_dicionario = {}
    livro_dicionario["nome"] = nome
    livro_dicionario["autor"] = autor
    livro_dicionario["Qde_disp"] = qde_disp
    livro_dicionario["Qde_uso"] = qde_uso
    livro_dicionario["rating"] = avaliacao.informa_media_avaliacao(1,num_registro)
    livro_dicionario["Registro"] = num_registro

    livro_str = json.dumps(livro_dicionario) + "\n"

    with open ("livros.txt", "at") as arq:
        arq.write(livro_str)
    
    arq.close()
    
    
    
#relatorios.relatorio_livros()
    
def apaga_registro(registro_a_excluir):
    
    registro_a_excluir = str(registro_a_excluir) #volta para string
    Registro = "Registro: " + registro_a_excluir


    with open ("livros.txt","r") as arq:
        lista_de_linhas = arq.readlines()
        
        arq.close() #Fecha arquivo
        
        for indice,linha in enumerate(lista_de_linhas):
            
            linha = linha.replace('"','')
            linha = linha.replace("'","")
            
            
            if Registro in linha:
                indice_para_excluir = indice
        
        
        if type(indice_para_excluir) is int:
            lista_de_linhas.pop(indice_para_excluir)
            print("Livro apagado com sucesso")
            
        else:
            print("O Livro não foi localizado")
        
    with open("livros.txt","w") as arq: #Abre arquivo modo escrita
            
        for linha in lista_de_linhas:
            linha.strip() # Tira eventuais espaços em branco no inicio ou final 
            #linha = linha + '\n' #Coloca a próxima inserção na linha abaixo
            arq.write(linha)
        
        arq.close()
    


    
## Pergunta qual excluir

def proc_apaga_registro():
    
    relatorios.relatorio_livros()

    registro_a_excluir = input("Digite o número do registro do livro a ser excluído\n")

    relatorios.limpa_linha_em_branco('livro')

    with open("livros.txt","r") as arq:
        
        for linha in arq:
            dicionario = eval(linha)
            
            registro_a_excluir = int(registro_a_excluir)
            
            if dicionario['Registro'] == registro_a_excluir:
                
                ficha = relatorios.monta_string_livro(dicionario)
                
                print(ficha)

    #Fecha arquivo
    arq.close()

    acao = input("\nDeseja realmente apagar ? s/n\n")
    acao.lower()


    if acao == 's':
        apaga_registro(registro_a_excluir)
        
    if acao == 'n':
        return

        
    
    
def menu_livro():
    while True:
        print("""
              
            Bem vindo ao Menu de opções possíveis com livros:

            1 - Cadastrar um livro 
            2 - Apagar o cadastro de um livro
            3 - Volta as opções anteriores
            
            """)
        
        escolha_do_usuario = input("O que você deseja fazer ?\n")

        if escolha_do_usuario == "3":
            break

        if escolha_do_usuario == "1":
            cadastrar_livro()
            ficha_livro = confirma.confirma_cadastro("livro")
            confirmacao_livro = relatorios.monta_string_livro(ficha_livro)
            print(confirmacao_livro)
            
        if escolha_do_usuario == '2':
            proc_apaga_registro()
            
            
        


