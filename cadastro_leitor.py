import datetime
import ultimo_registro
import confirma
import relatorios
import json


def cadastrar_leitor():
    nome = input("Digite o nome do Leitor\n")
    escola = input("Informe qual escola está matriculado\n")
    turma = input("Informe o curso que o leitor está inscrito\n")
    ano_cadastro = datetime.date.today().year

    #Produra o último registro de livro para partir determinar próximo registro.
    registro_leitor = ultimo_registro.procura_ultimo_registro("leitor")

    leitor = {}
    leitor["nome"]=nome
    leitor["escola"]=escola
    leitor["turma"] = turma
    leitor["ano"]=ano_cadastro
    leitor["Registro"] = registro_leitor

    leitor_str = json.dumps(leitor) + "\n"

    with open("leitores.txt","at") as arq:
        arq.write(leitor_str)

    arq.close()
    

def apaga_leitor(registro):
    
    with open("leitores.txt","r") as leitores:
        linhas = leitores.readlines()
        
        leitores.close()
        
    for indice,linha in enumerate (linhas):
        pedaco_final = linha[-17:-1]
    
        
        if pedaco_final.find(registro) > -1:
            index_para_apagar = indice
            linhas.pop(index_para_apagar)
            return 'sucesso'
            
        
        if pedaco_final.find(registro) <= -1:
            return 'erro'
    
    
    with open("leitores.txt","wt") as leitores:
        leitores.writelines(linhas)
    leitores.close()

        
        
    
    
    
def menu_leitor():
    while True:
        print("""
            
            1 - Cadastro de novo Leitor
            2 - Apaga leitor do cadastro
            3 - Volta para as opções anteriores
            
            """)
        escolha = input("Digite a opção desejada\n")
        
        if escolha == '3':
            break
            
        if escolha == '1':
            cadastrar_leitor()
            ficha_leitor = confirma.confirma_cadastro("leitor")
            confirmacao_leitor = relatorios.monta_string_leitor(ficha_leitor)
            print(confirmacao_leitor)
            
        if escolha == '2':
            print(relatorios.relatorio_leitores())
            
            registro_leitor = input("Digite o número do registro do leitor a ser apagado")
            status = apaga_leitor(registro_leitor)
            
            if status =="sucesso":
                print("Cadastro de Leitor apagado com sucesso")
                
            if status == "erro":
                print("O registro não foi localizado, tente novamente")
            
