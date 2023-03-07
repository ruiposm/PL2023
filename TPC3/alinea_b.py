from datetime import datetime

with open("processos.txt", "r") as arquivo:
    first_name_freq = {}
    last_name_freq = {}
    for i in range(16, 22):
        first_name_freq[f"Século {i}"] = {}
        last_name_freq[f"Século {i}"] = {}

    for linha in arquivo:
        linha = linha.strip()
        linha = linha.replace("::", ",")

        if linha:
            partes = linha.split(",")
            if len(partes) >= 6:
                data = datetime.strptime(partes[1], '%Y-%m-%d')
                nome = partes[2]
                partes_nome = nome.split()
                primeiro_nome = partes_nome[0]
                ultimo_nome = partes_nome[-1]
                # calcular o seculo
                seculo = f"Século {((data.year - 1) // 100) + 1}"
                if primeiro_nome in first_name_freq[seculo]:
                    first_name_freq[seculo][primeiro_nome] += 1
                else:
                    first_name_freq[seculo][primeiro_nome] = 1
                if ultimo_nome in last_name_freq[seculo]:
                    last_name_freq[seculo][ultimo_nome] += 1
                else:
                    last_name_freq[seculo][ultimo_nome] = 1

# 5 nomes próprios e apelidos mais usados
for seculo in first_name_freq.keys():
    print(f"Primeiros nomes mais usados no {seculo}:")
    top_first_names = sorted(first_name_freq[seculo], key=first_name_freq[seculo].get, reverse=True)[:5]
    for nome in top_first_names:
        print(f"- {nome} ({first_name_freq[seculo][nome]} vezes)")
    print(f"Últimos nomes mais usados no {seculo}:")
    top_last_names = sorted(last_name_freq[seculo], key=last_name_freq[seculo].get, reverse=True)[:5]
    for nome in top_last_names:
        print(f"- {nome} ({last_name_freq[seculo][nome]} vezes)")
