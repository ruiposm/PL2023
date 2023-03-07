import re

def contar_relacoes():
    # abre o arquivo
    with open("processos.txt", "r") as f:
        # lê o conteúdo do arquivo
        conteudo = f.read()
        # utiliza expressões regulares para buscar as ocorrências dos tipos de relação
        regex = r"(irmao|sobrinho materno|sobrinho paterno|tio paterno|tio materno|primo materno|primo paterno|avo materno|avo paterno|neto materno|neto paterno)"
        ocorrencias = re.findall(regex, conteudo, re.IGNORECASE)
        # conta a frequência de cada tipo de relação
        frequencias = {}
        for ocorrencia in ocorrencias:
            if ocorrencia in frequencias:
                frequencias[ocorrencia] += 1
            else:
                frequencias[ocorrencia] = 1
        # retorna o dicionário de frequências
        return frequencias

# chama a função e imprime o resultado
print(contar_relacoes())
