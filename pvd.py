import os
from glob import glob

# Caminho onde estão seus arquivos .vtu
pasta = "D:/Documentos/Permanent-heat-conduction"
arquivos = sorted(glob(os.path.join(pasta, "resultsQ100_t*.vtu")))

# Nome do arquivo de saída .pvd
saida_pvd = os.path.join(pasta, "results_adimensionalQ_100.pvd")

# Geração do arquivo PVD
with open(saida_pvd, "w") as f:
    f.write('<VTKFile type="Collection" version="0.1" byte_order="LittleEndian">\n')
    f.write('  <Collection>\n')
    for arq in arquivos:
        nome = os.path.basename(arq)
        # Extrai o valor do tempo do nome do arquivo, ex: arquivo_t0.01.vtu
        tempo = nome.replace("resultsQ100_t", "").replace(".vtu", "")
        f.write(f'    <DataSet timestep="{tempo}" group="" part="0" file="{nome}"/>\n')
    f.write('  </Collection>\n')
    f.write('</VTKFile>\n')

print(f".pvd gerado com sucesso: {saida_pvd}")
