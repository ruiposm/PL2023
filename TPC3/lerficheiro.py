# abrindo o arquivo
with open("processos.txt", "r") as arquivo:
    # criando um dicionário para armazenar as informações
    processos = {}

    for linha in arquivo:
        linha = linha.strip()
        linha = linha.replace("::",",")
        if linha:
            partes = linha.split(",")
            if len(partes) >= 6:
    
                processo = {
                    "pasta": partes[0],
                    "data": partes[1],
                    "nome": partes[2],
                    "pai": partes[3],
                    "mae": partes[4],
                    "obs": partes[5]
                }
        
        # adicionando o processo ao dicionário de processos
                processos[processo["nome"]] = processo

print(processos)
