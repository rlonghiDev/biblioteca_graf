def procura_ultimo_registro(tipo_procura):
        
        if tipo_procura == 'livro':
            arquivo_para_abrir = "livros.txt"
        if tipo_procura == 'leitor':
            arquivo_para_abrir = "leitores.txt"
        if tipo_procura == 'emprestimo':
            arquivo_para_abrir = "emprestimos.txt"

        with open(arquivo_para_abrir,"r") as arq:
            linha = arq.readlines()

        arq.close()

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
