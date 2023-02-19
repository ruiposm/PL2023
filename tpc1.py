def ler_dados():
    # Inicializar lista vazia para os dados
    dados = []

    # Abrir o arquivo para leitura
    with open("myheart.csv", 'r') as f:
        # Ler a primeira linha do myheart e descartá-lo
        next(f)
        
        # Iterar pelas linhas restantes
        for linha in f:
            # Dividir a linha em campos usando a vírgula como separador
            campos = linha.strip().split(',')
            
            # Valores de cada campo
            idade = int(campos[0])
            sexo = campos[1]
            tensao = int(campos[2])
            colesterol = int(campos[3])
            batimento = int(campos[4])
            tem_doenca = int(campos[5])
            
            # Adicionar os valores a um dicionário
            dicionario = {'idade': idade, 'sexo': sexo, 'tensao': tensao, 'colesterol': colesterol, 'batimento': batimento, 'tem_doenca': tem_doenca}
            
            # Adicionar o dicionário à lista de dados
            dados.append(dicionario)

    # Retornar a lista de dados
    return dados


def distribuicao_doenca_por_sexo(dados):
    # Contar o número de homens e mulheres com e sem doença
    homens_com_doenca = 0
    homens_sem_doenca = 0
    mulheres_com_doenca = 0
    mulheres_sem_doenca = 0
    
    for dicionario in dados:
        if dicionario['sexo'] == 'M':
            if dicionario['tem_doenca'] == 1:
                homens_com_doenca += 1
            else:
                homens_sem_doenca += 1
        elif dicionario['sexo'] == 'F':
            if dicionario['tem_doenca'] == 1:
                mulheres_com_doenca += 1
            else:
                mulheres_sem_doenca += 1
    
    # Calcular as proporções correspondentes
    total_homens = homens_com_doenca + homens_sem_doenca
    total_mulheres = mulheres_com_doenca + mulheres_sem_doenca
    
    percentagem_homem_com_doenca = homens_com_doenca / total_homens
    percentagem_homem_sem_doenca = homens_sem_doenca / total_homens
    percentagem_mulher_com_doenca = mulheres_com_doenca / total_mulheres
    percentagem_mulher_sem_doenca = mulheres_sem_doenca / total_mulheres
    
    # Retornar um dicionário com as proporções
    return {'homens_com_doenca': percentagem_homem_com_doenca, 
            'homens_sem_doenca': percentagem_homem_sem_doenca, 
            'mulheres_com_doenca': percentagem_mulher_com_doenca, 
            'mulheres_sem_doenca': percentagem_mulher_sem_doenca}
    

def distribuicao_por_idade(dados):
    # Inicializar dicionário com contagem de pessoas por intervalo de idade
    contagem_idades = {'[30-34]': 0, '[35-39]': 0, '[40-44]': 0}
    
    # Inicializar dicionário com contagem de pessoas doentes por intervalo de idade
    contagem_doencas = {'[30-34]': 0, '[35-39]': 0, '[40-44]': 0}
    
    # Iterar sobre os dados
    for dicionario in dados:
        idade = dicionario['idade']
        tem_doenca = dicionario['tem_doenca']
        
        # Adicionar a contagem de pessoas ao intervalo de idade correspondente
        if idade >= 30 and idade <= 34:
            contagem_idades['[30-34]'] += 1
        elif idade >= 35 and idade <= 39:
            contagem_idades['[35-39]'] += 1
        elif idade >= 40 and idade <= 44:
            contagem_idades['[40-44]'] += 1
        
        # Adicionar a contagem de pessoas doentes ao intervalo de idade correspondente
        if idade >= 30 and idade <= 34 and tem_doenca == 1:
            contagem_doencas['[30-34]'] += 1
        elif idade >= 35 and idade <= 39 and tem_doenca == 1:
            contagem_doencas['[35-39]'] += 1
        elif idade >= 40 and idade <= 44 and tem_doenca == 1:
            contagem_doencas['[40-44]'] += 1
    
    # Calcular a percentagem de pessoas doentes em cada intervalo de idade
    percentagem_doencas = {}
    for intervalo in contagem_doencas:
        contagem = contagem_idades[intervalo]
        if contagem > 0:
            percentagem = contagem_doencas[intervalo] / contagem
        else:
            proporcao = 0.0
        percentagem_doencas[intervalo] = percentagem
    
    # Retornar o dicionário com as percentagens de doença por intervalo de idade
    return percentagem_doencas


def distribuicao_doencas_por_colesterol(dados):
    # Cria um dicionário para armazenar a contagem de doenças por nível de colesterol
    doencas_por_colesterol = {}
    
    # Determina o limite inferior e superior dos níveis de colesterol
    colesterol_min = min(dados['colesterol'])
    colesterol_max = max(dados['colesterol'])
    colesterol_int = 10
    
    # Cria os níveis de colesterol e inicializa as contagens de doenças em cada nível com zero
    for colesterol in range(colesterol_min, colesterol_max + colesterol_int, colesterol_int):
        doencas_por_colesterol[colesterol] = 0
    
    # Percorre os dados e incrementa as contagens de doenças nos níveis correspondentes de colesterol
    for i in range(len(dados['colesterol'])):
        colesterol = dados['colesterol'][i]
        doencas = dados['tem_doenca'][i]
        
        for c in range(colesterol_min, colesterol_max + colesterol_int, colesterol_int):
            if colesterol < c + colesterol_int:
                doencas_por_colesterol[c] += doencas
                break
    
    # Retorna o dicionário de contagens de doenças por nível de colesterol
    return doencas_por_colesterol

dados = ler_dados()

# Distribuição por idade
print('Distribuição por idade:')
print('--------------------------------')
print('| Intervalo de idade | Percentagem de doenças |')
print('--------------------------------')
for intervalo, percentagem in distribuicao_por_idade(dados).items():
    print(f"| {intervalo:18} | {percentagem:21.2%} |")
print('--------------------------------')

# Distribuição por Sexo
def imprimir_tabela_distribuicao_doencas_por_sexo(dados):
    distr = distribuicao_doenca_por_sexo(dados)
    
    print('Distribuição por Sexo:')
    print("+----------------+----------------+")
    print("| Sexo           | Contagem       |")
    print("+----------------+----------------+")
    for sexo, contagem in distr.items():
        print(f"| {sexo:20} | {contagem:20} |")
    print("+----------------+----------------+")
    
imprimir_tabela_distribuicao_doencas_por_sexo(dados)

