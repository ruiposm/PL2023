# abrindo o arquivo
with open("processos.txt", "r") as arquivo:
    # criando um dicionário para armazenar as informações
    processos = {}

    for linha in arquivo:
        linha = linha.strip()
        linha = linha.replace("::", ",")
        if linha:
            partes = linha.split(",")
            if len(partes) >= 6:
                
             #criando um dicionário para armazenar as informações do processo atual
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

frequencia_por_ano = {}

# percorrendo o dicionário de processos e incrementando a contagem do ano correspondente
for processo in processos.values():
    ano = processo["data"].split("-")[2] 
    if ano in frequencia_por_ano:
        frequencia_por_ano[ano] += 1
    else:
        frequencia_por_ano[ano] = 1

for ano, frequencia in frequencia_por_ano.items():
    print(f"Ano {ano}: {frequencia} processos")