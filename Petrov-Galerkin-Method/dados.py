import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress

# Nome do arquivo CSV gerado pelo FreeFem++
csv_file = 'D:/Documentos/Permanent-heat-conduction/Petrov-Galerkin-Method/tabela_erros.csv'

try:
    # Carregar os dados do CSV
    df = pd.read_csv(csv_file)

    # Exibir as primeiras linhas do DataFrame para verificar
    print("Dados carregados do CSV:")
    print(df.head())
    print("\n")

    # Colunas de erro que queremos analisar
    # Adicionadas 'L2T' e 'H1T'
    error_columns = ['L2u', 'H1u', 'L2p', 'H1p', 'L2T', 'H1T'] 

    # Criar uma figura para os subplots
    # Ajustado para 2 linhas e 3 colunas para acomodar 6 gráficos
    plt.figure(figsize=(18, 12)) 

    # Iterar sobre cada coluna de erro para gerar o gráfico e calcular a ordem
    for i, error_col in enumerate(error_columns):
        # Filtrar linhas onde o erro não é NaN (para a primeira linha, onde a ordem é NaN)
        # E garantir que os valores de erro e h sejam positivos para o log
        valid_data = df[(df[error_col].notna()) & (df[error_col] > 0) & (df['h'] > 0)]

        if valid_data.empty:
            print(f"Não há dados válidos para a coluna '{error_col}' para plotar e calcular a ordem de convergência.")
            continue

        # Calcular log(h) e log(Erro)
        log_h = np.log(valid_data['h'])
        log_error = np.log(valid_data[error_col])

        # Criar um subplot para cada tipo de erro (2 linhas, 3 colunas)
        plt.subplot(2, 3, i + 1) 

        # Plotar os pontos (log(Erro) vs log(h))
        plt.scatter(log_h, log_error, label=f'Dados {error_col}', color='blue', marker='o')

        # Realizar regressão linear para encontrar a ordem de convergência (inclinação)
        # Ignorar a primeira linha se a ordem for 'NaN' ou 0 para o cálculo da regressão
        # A regressão linear será feita nos dados log-log
        slope, intercept, r_value, p_value, std_err = linregress(log_h, log_error)
        order_of_convergence = -slope # A ordem de convergência é geralmente o negativo da inclinação em log(Erro) vs log(h)

        # Plotar a linha de regressão
        plt.plot(log_h, intercept + slope * log_h, color='red', linestyle='--', label=f'Regressão (Ordem: {order_of_convergence:.2f})')

        # Adicionar rótulos e título
        plt.xlabel('log(h)')
        plt.ylabel(f'log({error_col})')
        plt.title(f'Convergência da Norma {error_col}')
        plt.legend()
        plt.grid(True)

        print(f"Ordem de Convergência para {error_col}: {order_of_convergence:.4f}")

    plt.tight_layout() # Ajusta o layout para evitar sobreposição
    plt.show()

except FileNotFoundError:
    print(f"Erro: O arquivo '{csv_file}' não foi encontrado. Certifique-se de que o CSV foi gerado e está no mesmo diretório do script Python.")
except Exception as e:
    print(f"Ocorreu um erro: {e}")

