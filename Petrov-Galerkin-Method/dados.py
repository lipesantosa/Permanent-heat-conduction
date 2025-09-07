import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def plot_and_analyze_errors(filepath):



    filepath = "D:/Documentos/Permanent-heat-conduction/Petrov-Galerkin-Method/tabela_erros.csv"

    try:
        df = pd.read_csv(filepath)
    except FileNotFoundError:
        print(f"Erro: O arquivo '{filepath}' não foi encontrado.")
        return

    # Certifica-se de que os dados são numéricos e remove linhas com valores NaN
    df = df.apply(pd.to_numeric, errors='coerce').dropna()

    # Define as colunas de erro e as ordens de convergência
    error_cols = ['L2u', 'H1u', 'L2p', 'H1p', 'L2T', 'H1T']

    print("Análise de Erro e Ordem de Convergência:\n")
    print("-" * 50)

    # Cria a figura e os eixos para o plot
    fig, ax = plt.subplots(figsize=(10, 8))

    # Calcula e plota os erros para cada coluna
    for col in error_cols:
        if col in df.columns and 'h' in df.columns:
            # Obtém os dados de erro e tamanho da malha
            h_values = df['h'].values
            error_values = df[col].values

            # Remove os valores com erro zero para evitar problemas no log
            valid_indices = error_values > 0
            h_valid = h_values[valid_indices]
            error_valid = error_values[valid_indices]

            if len(h_valid) < 2:
                print(f"Atenção: A coluna '{col}' não tem dados suficientes para plotar e calcular a ordem de convergência.")
                continue

            # Plota os dados em escala log-log
            ax.loglog(h_valid, error_valid, 'o-', label=f'Erro {col}')

            # Calcula a ordem de convergência (inclinação da linha log-log)
            # Usa os últimos dois pontos para uma estimativa mais representativa
            if len(h_valid) >= 2:
                last_two_h = h_valid[-2:]
                last_two_errors = error_valid[-2:]
                
                # A ordem é a inclinação da reta no gráfico log-log
                order = np.log(last_two_errors[0] / last_two_errors[1]) / np.log(last_two_h[0] / last_two_h[1])
                print(f"Erro {col}: A ordem de convergência (inclinação) é de aproximadamente {order:.2f}")

                # Adiciona o valor da ordem de convergência no gráfico
                ax.text(h_valid[-1], error_valid[-1], f' Ordem: {order:.2f}', fontsize=10, verticalalignment='bottom', horizontalalignment='right')

    # Configurações do gráfico
    ax.set_title('Gráfico de Erro vs. Tamanho da Malha (Log-Log)', fontsize=16)
    ax.set_xlabel('Tamanho da Malha (h)', fontsize=12)
    ax.set_ylabel('Erro', fontsize=12)
    ax.grid(True, which="both", ls="--")
    ax.legend()
    plt.tight_layout()
    plt.show()

    print("\nResumo da Análise:")
    print("-" * 50)

# Executa a função com o arquivo fornecido pelo usuário
if __name__ == "__main__":
    plot_and_analyze_errors('tabela_erros.csv')
