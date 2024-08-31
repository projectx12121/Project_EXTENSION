from ProcessingData2 import grafico, sintese

def main():

    dadosTratados = "Database/dadosTratados.csv"

    sintese.main(dadosTratados)
    grafico.main(dadosTratados)

if __name__ == '__main__':
    main()

"""
Perfil Econômico:
Com o objetivo que seja a abertura de uma filial que dependa de uma clientela com maior poder aquisitivo,
recomenda-se priorizar bairros onde os salários médios sejam mais elevados e onde a distribuição salarial
favoreça rendimentos altos.

Demografia e Raça de Cães:
Se o empreendimento estiver relacionado a produtos ou serviços destinados a cães,
é aconselhável selecionar bairros com alta concentração das raças de cães que correspondem ao público-alvo
do negócio, indicando um mercado potencialmente interessado nos serviços oferecidos.

Dados Profissionais: No caso de a filial fornecer produtos ou serviços voltados para profissionais
de alta renda ou setores específicos, é recomendável escolher bairros com uma elevada concentração
desses profissionais, a fim de maximizar o alcance e a eficácia da filial.
"""