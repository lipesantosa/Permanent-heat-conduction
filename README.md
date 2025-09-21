# Simulação de Transporte de Calor com Elementos Finitos (P1-P1)

Este repositório contém uma implementação em **FreeFEM++** do problema de **transporte de calor** em um fluido em movimento, resolvido via **Método dos Elementos Finitos (FEM)** utilizando discretização **P1-P1** (linear para velocidade/temperatura e linear para pressão).

---

## 📖 Formulação Matemática

O problema considerado é o transporte de calor em um fluido incompressível, modelado pelo sistema acoplado de **Navier–Stokes** com a **equação de energia**.

### Equações Governantes

1. **Conservação da massa (incompressibilidade):**

$$
\nabla \cdot \mathbf{u} = 0
$$

2. **Equações de Navier–Stokes (momentum):**

$$
\frac{\partial \mathbf{u}}{\partial t} + (\mathbf{u}\cdot \nabla)\mathbf{u} - \nu \Delta \mathbf{u} + \nabla p = \mathbf{f}
$$

3. **Equação de energia (transporte de calor):**

$$
\frac{\partial T}{\partial t} + (\mathbf{u}\cdot \nabla)T - \kappa \Delta T = f_T
$$

onde:  
- $\mathbf{u} = (u_1,u_2)$ é o campo de velocidades,  
- $p$ é a pressão,  
- $T$ é a temperatura,  
- $\nu$ é a viscosidade cinemática,  
- $\kappa$ é a difusividade térmica,  
- $\mathbf{f}$ é um termo de força externa (e.g., gravidade),  
- $f_T$ é uma fonte de calor volumétrica.

---

## ⚙️ Formulação Variacional (FEM)



