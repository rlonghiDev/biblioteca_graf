import datetime
import ultimo_registro
import relatorios
import avaliacao

def realiza_emprestimo(registro_leitor,registro_livro):
                
    with open("leitores.txt","r") as arq:
        global ficha_leitor
        global ficha_livro
        ficha_livro = {}
        ficha_leitor = {}

        for linha in arq:
            dicionario = eval(linha)
            if registro_leitor == dicionario['Registro']:
                ficha_leitor = dicionario
    
    arq.close()#Fecha arquivo

    with open("livros.txt", "r") as books:

        for linha in books:
            dict_books = eval(linha)
            if registro_livro == dict_books["Registro"]:
                ficha_livro = dict_books
    
    books.close()

    if ficha_leitor != None and ficha_livro != None:
        dict_emprestimo = {}
        dict_emprestimo['leitor'] = registro_leitor
        dict_emprestimo['livro'] = registro_livro
        dict_emprestimo['data'] = datetime.date.today()
        dict_emprestimo['Registro'] = ultimo_registro.procura_ultimo_registro('emprestimo')

    else:
        print("Erro, verifique os códigos de registro informados e tente novamente")
        exit(0)

    emprestimo_str = str(dict_emprestimo) + '\n'


    with open("emprestimos.txt","at") as arq:
        arq.write(emprestimo_str)

    arq.close()
    


def apaga_linha(Registro):
    
    Registro = "Registro: " + str(Registro)
    indice_para_apagar = ''

    with open("emprestimos.txt","r") as arq: #Abre arquivo no modo leitura
        lista_de_linhas = arq.readlines()
        
        arq.close() #Fecha arquivo
        
        for indice,linha in enumerate(lista_de_linhas):
            
            linha = linha.replace('"','')
            linha = linha.replace("'","")
            
            
            if Registro in linha:
                indice_para_apagar = indice
            
            
            
        ##Remove emprestimo se o registro foi localizado
        if type(indice_para_apagar) is int:
            lista_de_linhas.pop(indice_para_apagar)
            print("Empréstimo encerrado com sucesso")
            
        else:
            print("Empréstimo não foi localizado")
        
    with open("emprestimos.txt","w") as arq: #Abre arquivo modo escrita
            
        for linha in lista_de_linhas:
            linha.strip() # Tira eventuais espaços em branco no inicio ou final 
            #linha = linha + '\n' #Coloca a próxima inserção na linha abaixo
            arq.write(linha)
        
        arq.close()





def apaga_emprestimo():
    relatorios.relatorio_emprestimo()
    Registro = input("Digite o número do empréstimo que será encerrado\n")
    registro_emprestimo = relatorios.busca_info(Registro,"emprestimo",1)
    registro_livro = registro_emprestimo["livro"]
    ficha_emprestimo = relatorios.monta_string_emprestimo(registro_emprestimo)
    
    
    print(ficha_emprestimo)
    
       
    if ficha_emprestimo != "Nao localizado":
        confirma = input("Confirma encerramento desse empréstimo ? s/n ")
    else:
        print("Emprestimo Não localizado\n")
        confirma = 'n'
    
    if confirma == 's':
        nota = int(input("Dê sua avaliação de 1 a 5 para o livro"))
        avaliacao.avaliacao(1,registro_livro,nota)
        apaga_linha(Registro)
    
    if confirma == 'n':
        return
    
    