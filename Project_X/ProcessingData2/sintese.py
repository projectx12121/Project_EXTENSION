import pandas as pd
import pandasql as psql

def df(filepath):

    # Lê o arquivo CSV e carrega os dados no DataFrame 'df'
    return pd.read_csv(filepath)

""" 
# Salário Médio por Bairro:
* Identifica bairros com maior poder aquisitivo, 
que podem ser mais propensos a gastar com serviços de petshop.
"""
def salario_medio_bairro(df):

    query = ("SELECT Bairro, "
             "AVG(Salario) AS Salario_Medio "
             "FROM df "
             "GROUP BY Bairro "
             "ORDER BY Salario_Medio DESC")

    result_df = psql.sqldf(query, locals())
    result_df['Salario_Medio'] = result_df['Salario_Medio'].astype(float).round(2)
    #sal_med = result_df['Salario_Medio'].iloc[0]

    # Exibe os valores
    print(f"\n# Salario Medio por Bairro ")
    print(result_df)

    # Salva o resultado em um arquivo CSV dentro da pasta 'Report'
    result_df.to_csv("Report/salario_medio_bairro.csv", index=False)
    return

"""
# Número de Clientes por Bairro:
* Bairros com mais clientes podem indicar uma maior demanda para o serviço de petshop.
"""
def clientes_bairro(df):

    query = ("SELECT "
             "Bairro, "
             "COUNT(*) AS Numero_Clientes "
             "FROM df "
             "GROUP BY Bairro "
             "ORDER BY Numero_Clientes DESC")

    result_df = psql.sqldf(query, locals())

    # Exibe os valores
    print(f"\n# Numero de Clientes por Bairro")
    print(result_df)

    # Salva o resultado em um arquivo CSV dentro da pasta 'Report'
    result_df.to_csv("Report/clientes_bairro.csv", index=False)
    return

"""
# Distribuição de Raças de Cachorro por Bairro: 
* Mostra quais raças são mais comuns em diferentes bairros, 
ajudando a ajustar o estoque e serviços da petshop.
"""
def raca_bairro(df):

    query = ("SELECT Bairro, "
             "Raca, "
             "COUNT(*) AS Quantidade "
             "FROM df "
             "GROUP BY Bairro, Raca "
             "ORDER BY Bairro, Quantidade DESC")

    result_df = psql.sqldf(query, locals())

    # Exibe os valores
    print(f"\n# Distribuicao de Raças de Cachorro por Bairro")
    print(result_df)

    # Salva o resultado em um arquivo CSV dentro da pasta 'Report'
    result_df.to_csv("Report/raca_bairro.csv", index=False)
    return

""" 
# Distribuição de Profissões dos Clientes por Bairro:
* Profissões podem indicar a faixa de renda e potencial interesse em serviços de petshop.
"""
def profissoes_cliente(df):

    query = ("SELECT Bairro,"
             "Profissao, "
             "COUNT(*) AS Quantidade "
             "FROM df "
             "GROUP BY Bairro, Profissao "
             "ORDER BY Bairro, Quantidade DESC")

    result_df = psql.sqldf(query, locals())

    # Exibe os valores
    print(f"\n# Distribuicao de Profissoes dos Clientes por Bairro")
    print(result_df)

    # Salva o resultado em um arquivo CSV dentro da pasta 'Report'
    result_df.to_csv("Report/profissoes_cliente.csv", index=False)
    return

""" 
# Faixa Etária dos Clientes por Bairro:
* Ajuda a entender a faixa etária média dos clientes em cada bairro.
"""
def idade_cliente(df):

    query = ("SELECT Bairro, "
             "AVG(Idade) AS Idade_Media, "
             "MIN(Idade) AS Idade_Minima, "
             "MAX(Idade) AS Idade_Maxima "
             "FROM df "
             "GROUP BY Bairro "
             "ORDER BY Idade_Media DESC")

    result_df = psql.sqldf(query, locals())

    # Converte as colunas para inteiros
    result_df['Idade_Media'] = result_df['Idade_Media'].astype(int)

    # Exibe os valores
    print(f"\n# Faixa Etaria dos Clientes por Bairro")
    print(result_df)

    # Salva o resultado em um arquivo CSV dentro da pasta 'Report'
    result_df.to_csv("Report/idade_cliente.csv", index=False)
    return

"""
# Salário Médio e Quantidade de Clientes por Bairro:
* Identifica bairros com maior potencial financeiro e número de clientes.
"""
def salMedio_clientes(df):

    query = ("SELECT Bairro, "
             "AVG(Salario) AS Salario_Medio, "
             "COUNT(*) AS Numero_Clientes "
             "FROM df "
             "GROUP BY Bairro "
             "ORDER BY Salario_Medio DESC, Numero_Clientes DESC")

    result_df = psql.sqldf(query, locals())
    result_df['Salario_Medio'] = result_df['Salario_Medio'].astype(float).round(2)

    # Exibe os valores
    print(f"\n# Salário Médio e Quantidade de Clientes por Bairro")
    print(result_df)

    # Salva o resultado em um arquivo CSV dentro da pasta 'Report'
    result_df.to_csv("Report/salMedio_clientes.csv", index=False)  # Salva o DataFrame em um arquivo CSV
    return

"""
# Quantidade de Clientes por Faixa Salarial:
* Analisa a distribuição dos clientes por faixa salarial. 
"""
def clientes_faixaSalarial(df):

    query = ("SELECT "
             "CASE "
             "WHEN Salario BETWEEN 1350 AND 3000 THEN '1350-3000' "
             "WHEN Salario BETWEEN 3001 AND 5000 THEN '3001-5000' "
             "WHEN Salario BETWEEN 5001 AND 7000 THEN '5001-7000' "
             "WHEN Salario BETWEEN 7001 AND 10000 THEN '7001-10000' "
             "ELSE 'Acima de 10000' END AS Faixa_Salarial, "
             "COUNT(*) AS Numero_Clientes "
             "FROM df "
             "GROUP BY Faixa_Salarial "
             "ORDER BY Numero_Clientes DESC")

    result_df = psql.sqldf(query, locals())

    # Exibe os valores
    print(f"\n# Quantidade de Clientes por Faixa Salarial")
    print(result_df)

    # Salva o resultado em um arquivo CSV dentro da pasta 'Report'
    result_df.to_csv("Report/clientes_faixaSalarial.csv", index=False)
    return

"""
# Clientes com Raça de Cachorro Popular:
* Identifica clientes com as raças de cachorro mais populares, 
o que pode ajudar no foco da oferta de produtos e serviços.
"""
def clientes_raca(df):

    query = ("SELECT Cliente, "
             "Raca "
             "FROM df "
             "WHERE Raca IN ("
             "SELECT Raca "
             "FROM df GROUP BY Raca "
             "ORDER BY COUNT(*) DESC LIMIT 5)")

    result_df = psql.sqldf(query, locals())

    # Exibe os valores
    print(f"\n# Clientes com Raca de Cachorro Popular")
    print(result_df)

    # Salva o resultado em um arquivo CSV dentro da pasta 'Report'
    result_df.to_csv("Report/clientes_raca.csv", index=False)
    return

"""
# Correlação entre Salário e Idade: 
* Analisa como a faixa salarial pode influenciar a idade dos clientes, 
ajudando a ajustar o marketing.
"""
def salario_idade(df):

    query = ("SELECT AVG(Salario) AS Salario_Medio, "
             "AVG(Idade) AS Idade_Media "
             "FROM df "
             "GROUP BY Salario, Idade "
             "ORDER BY Salario_Medio DESC")

    result_df = psql.sqldf(query, locals())
    result_df['Idade_Media'] = result_df['Idade_Media'].astype(int)
    result_df['Salario_Medio'] = result_df['Salario_Medio'].astype(float).round(2)

    # Exibe os valores
    print(f"\n# Correlação entre Salário e Idade")
    print(result_df)

    # Salva o resultado em um arquivo CSV dentro da pasta 'Report'
    result_df.to_csv("Report/salario_idade.csv", index=False)
    return

"""
# Número de Clientes por Sexo e Bairro:
* Identifica a distribuição de clientes por sexo em diferentes bairros, 
o que pode influenciar a estratégia de marketing e serviços.
"""
def sexo_bairro(df):

    query = ("SELECT "
             "Bairro, "
             "Sexo, "
             "COUNT(*) AS Numero_Clientes "
             "FROM df "
             "GROUP BY Bairro, Sexo "
             "ORDER BY Bairro, Numero_Clientes DESC")

    result_df = psql.sqldf(query, locals())

    # Exibe os valores
    print(f"\n# Correlação entre Salário e Idade")
    print(result_df)

    # Salva o resultado em um arquivo CSV dentro da pasta 'Report'
    result_df.to_csv("Report/salario_idade.csv", index=False)  # Salva o DataFrame em um arquivo CSV
    return

def main(filepath):

    # Carrega o DataFrame a partir do arquivo CSV
    frame = df(filepath)

    salario_medio_bairro(frame)
    clientes_bairro(frame)
    raca_bairro(frame)
    profissoes_cliente(frame)
    idade_cliente(frame)
    salMedio_clientes(frame)
    clientes_faixaSalarial(frame)
    clientes_raca(frame)
    salario_idade(frame)
    sexo_bairro(frame)

if __name__ == '__main__':

    # Substitua pelo caminho do seu arquivo CSV
    main(filepath="")