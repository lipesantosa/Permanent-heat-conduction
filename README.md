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
\frac{\partial T}{\partial t} + (\mathbf{u}\cdot \nabla)T - \kappa \Delta T = g
$$

onde:  
- $\mathbf{u} = (u_1,u_2)$ é o campo de velocidades,  
- $p$ é a pressão,  
- $T$ é a temperatura,  
- $\nu$ é a viscosidade cinemática,  
- $\kappa$ é a difusividade térmica,  
- $\mathbf{f}$ é um termo de força externa (e.g., gravidade),  
- $g$ é uma fonte de calor volumétrica.

---

## ⚙️ Formulação Variacional (FEM)

Sejam $V_h, Q_h, W_h$ os espaços de elementos finitos P1 para velocidade, pressão e temperatura, respectivamente.  
A formulação fraca consiste em encontrar $(\mathbf{u}_h, p_h, T_h) \in V_h \times Q_h \times W_h$ tais que:

1. **Momento:**

$$
\int_\Omega \left( \frac{\partial \mathbf{u}_h}{\partial t}\cdot \mathbf{v}_h + (\mathbf{u}_h\cdot \nabla)\mathbf{u}_h \cdot \mathbf{v}_h+ \nu \nabla \mathbf{u}_h : \nabla \mathbf{v}_h - p_h \, \nabla \cdot \mathbf{v}_h \right) \, dx = \int_\Omega \mathbf{f}\cdot \mathbf{v}_h \, dx
$$

2. **Incompressibilidade:**

$$
\int_\Omega q_h \, \nabla \cdot \mathbf{u}_h \, dx = 0
$$

3. **Energia:**

$$
\int_\Omega \left( \frac{\partial T_h}{\partial t}\, \theta_h  + (\mathbf{u}_h\cdot \nabla T_h)\theta_h  + \kappa \nabla T_h \cdot \nabla \theta_h \right) \, dx= \int_\Omega g \, \theta_h \, dx
$$

para todo $(\mathbf{v}_h, q_h, \theta_h) \in V_h \times Q_h \times W_h$.

---

## 🔧 Discretização Numérica

- **Espaços de aproximação:**  
  - Velocidade: P1 (linear contínuo)  
  - Pressão: P1 (linear contínuo)  
  - Temperatura: P1 (linear contínuo)  

- **Método temporal:** esquema implícito ou semi-implícito (Euler Backward).  
- **Estabilização:** opcionalmente, pode ser incluída estabilização **Petrov-Galerkin/GLS** para lidar com o par $P1-P1$ e termos advectivos dominantes.  

---

## 📂 Estrutura do Repositório

