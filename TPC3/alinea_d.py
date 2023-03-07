import json

with open("processos.txt", "r") as f:
    linhas = f.readlines()[:20]

dicio = []

for linha in linhas:
    linha = linha.strip().replace("::", ",")
    partes = linha.split(",")
    dic = {
        "pasta": partes[0],
        "data": partes[1],
        "nome": partes[2],
        "pai": partes[3],
        "mae": partes[4],
        "obs": partes[5]
    }
    dicio.append(dic)

with open("registros.json", "w") as f:
    json.dump(dicio, f, indent=4)
