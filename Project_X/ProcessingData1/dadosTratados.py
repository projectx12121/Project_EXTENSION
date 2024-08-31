# Importa a biblioteca Pandas para manipulacao de dados
import pandas as pd

def df(filepath):

    # Le o arquivo CSV para um DataFrame (carrega os dados no DataFrame 'df')
    return pd.read_csv(filepath)

def sistema(df):

    # Informacoes do DataFrame: Contagem de entradas, tipos de dados e memoria ocupada
    print("\033[00;32m\n# Informacoes de sistema \033[00;00m")
    print(df.info())

def descricao(df):

    # Exibe o DataFrame original
    print(f"\033[00;32m\n# DataFrame - Dados Tratados \033[00;00m\n {df}")

    # Gerando estatisticas descritivas apenas para colunas numericas
    descricao = df.describe()

    # Exibindo estatisticas descritivas para colunas numericas
    print("\033[00;32m\n# Estatisticas Descritivas para Colunas Numericas \033[00;00m")

    for coluna in descricao.columns:

        print(f"\n---------- {coluna} ----------\n")
        print(f"# Total de valores (count): {descricao[coluna]['count']:.0f}")
        print(f"# Media (mean): {descricao[coluna]['mean']:.2f}")
        print(f"# Desvio padrao (std): {descricao[coluna]['std']:.2f}")
        print(f"# 1º Quartil (25%): {descricao[coluna]['25%']:.2f}")
        print(f"# 3º Quartil (75%): {descricao[coluna]['75%']:.2f}")
        print(f"# Mediana (50%): {descricao[coluna]['50%']:.2f}")
        print(f"# Valor maximo (max): {descricao[coluna]['max']:.2f}")
        print(f"# Valor minimo (min): {descricao[coluna]['min']:.2f}")

    # Gerando estatisticas descritivas para colunas categoricas (nao numericas)
    descricao_categoricas = df.describe(include=['object'])

    # Exibindo estatisticas descritivas para colunas categoricas
    if not descricao_categoricas.empty:

        print("\033[00;32m\n# Estatisticas Descritivas - Colunas Categoricas \033[00;00m")

        for coluna in descricao_categoricas.columns:

            print(f"\n---------- {coluna} ----------\n")
            print(f"# Total de valores (count): {descricao_categoricas[coluna]['count']:.0f}")
            print(f"# Valor mais frequente (top): {descricao_categoricas[coluna]['top']}")
            print(f"# Frequencia do valor mais frequente (freq): {descricao_categoricas[coluna]['freq']:.0f}\n")

def tratamento(df):

    # Seleciona as linhas que tem ao menos um valor nulo
    df_missing = df[df.isna().any(axis=1)]

    # Exibe as linhas com dados inconsistentes
    print("\033[00;31m\n# Tratamento: Dados inconsistentes \033[00;00m\n", df_missing)

    """ 
        Tratando dados inconsistentes 
    """
    # Utiliza o indice das linhas com valores nulos para remove-las
    df_no_nulls = df.drop(df_missing.index)

    # Remove todas as linhas que contenham o valor zero em qualquer campo (filtra as linhas que nao contem zeros em nenhum campo)
    df_no_zeros = df_no_nulls[(df_no_nulls != 0).all(axis=1)]

    # Exibe o DataFrame apos a remocao dos dados nulos e zeros (mostra o DataFrame limpo, sem valores nulos e zeros)
    print("\033[00;31m\n# DataFrame Apos Remover Valores Nulos e Zeros\033[00;00m")
    print(df_no_zeros)

    # Retorna o DataFrame limpo e tratado
    return df_no_zeros

def arquivoNovo(df_no_zeros):

    # Salva o DataFrame limpo em um novo arquivo CSV
    df_no_zeros.to_csv("DataBase/dadosTratados.csv", index=False)

    # Exibe uma mensagem de confirmacao
    print("\033[01;33m\n# Dados tratados salvos em 'DataBase\dadosTratados.csv'.\033[00;00m")

def main(filepath):

    # Chama as funcoes de tratamento de dados e exibicao de informacoes
    print(f"\n\033[01;32m{'=-=' * 10} INFORMACOES DADOS TRATADOS {'=-=' * 10}\033[01;00m")

    frame = tratamento(df(filepath))
    sistema(frame)
    descricao(frame)
    arquivoNovo(frame)

# Verifica se o script esta sendo executado diretamente e, em caso afirmativo, chama a funcao principal
if __name__ == '__main__':

    # Executa a funcao principal
    main(filepath="")