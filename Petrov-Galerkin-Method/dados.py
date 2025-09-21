import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Substitua pelo seu caminho
csvfile = r"D:/Documentos/Permanent-heat-conduction/Petrov-Galerkin-Method/tabela_erros.csv"

df = pd.read_csv(csvfile)

# Colunas esperadas
error_cols = ['L2u', 'H1u', 'L2p', 'H1p', 'L2T', 'H1T']
if 'h' not in df.columns:
    raise RuntimeError("A coluna 'h' (tamanho de malha) não foi encontrada no CSV.")

# Ordena por h crescente (h pequeno = malha refinada)
df = df.sort_values('h').reset_index(drop=True)

# Prepara subplots
ncols = 2
nrows = int(np.ceil(len(error_cols)/ncols))
fig, axes = plt.subplots(nrows, ncols, figsize=(12, 10))
axes = axes.ravel()

results = {}

for i, col in enumerate(error_cols):
    ax = axes[i]
    if col not in df.columns:
        ax.set_visible(False)
        continue

    h = df['h'].to_numpy()
    err = df[col].to_numpy()

    # Filtra valores válidos
    mask = np.isfinite(err) & (err > 0)
    h = h[mask]
    err = err[mask]

    if len(h) < 2:
        ax.text(0.5, 0.5, f"Poucos dados em {col}", ha='center', va='center')
        continue

    # Ajuste log-log
    logh = np.log(h)
    logerr = np.log(err)
    coef = np.polyfit(logh, logerr, 1)
    slope = coef[0]

    # Reta de referência
    h_fit = np.linspace(h.max(), h.min(), 50)

    err_fit = np.exp(np.polyval(coef, np.log(h_fit)))

    # Plot
    ax.loglog(h, err, 'o-', label=f'Erro {col}')
    ax.loglog(h_fit, err_fit, '--', label=f'Fit slope = {slope:.2f}')
    ax.invert_xaxis()  # mostra refinamento à direita
    ax.set_xlabel('h')
    ax.set_ylabel('Erro')
    ax.set_title(f'{col}: ordem ≈ {slope:.2f}')
    ax.grid(True, which='both', ls='--')
    ax.legend()

    results[col] = slope

# Ajusta layout
plt.tight_layout()
plt.show()

# Imprime resumo no terminal
print("\nResumo das ordens de convergência (ajuste log-log):")
for col, slope in results.items():
    print(f"{col:>4}: {slope:.3f}")


csv = r"D:/Documentos/Permanent-heat-conduction/Petrov-Galerkin-Method/tabela_erros.csv"
df = pd.read_csv(csv).sort_values('h').reset_index(drop=True)
cols = ['L2u','H1u','L2p','H1p','L2T','H1T']
for col in cols:
    if col not in df.columns: continue
    h = df['h'].to_numpy(); err = df[col].to_numpy()
    mask = np.isfinite(err) & (err>0)
    h = h[mask]; err = err[mask]
    print("\n===", col, "===")
    for hi, ei in zip(h, err):
        print(f"h={hi:.6g}, err={ei:.6g}")
    if len(h)<2: continue
    # slopes locais
    slopes = [np.log(err[i-1]/err[i])/np.log(h[i-1]/h[i]) for i in range(1,len(h))]
    print("slopes locais:", np.array(slopes))
    # robust fit: remover outlier quando erro cresce > 10x
    mask_ok = np.ones_like(err, bool)
    for i in range(1,len(err)):
        if err[i] > 10*err[i-1]: mask_ok[i]=False
    coef = np.polyfit(np.log(h[mask_ok]), np.log(err[mask_ok]), 1)
    print("slope fit robust:", coef[0])