# Numerical Simulation of Convective-Diffusive Heat Transport by an Incompressible Viscous Flow

In this work we present a numerical study of heat transport through a moving fluid, in which convection and diffusion processes are considered. The transport is carried out by a newtonian, laminar, irrotational, incompressible and transient flow of a fluid based on the Navier-Stokes equations and the Convection-Diffusion equation. This study provides a basis for more theoretical investigations involving stability, existence of weak solutions and extensions to newtonian fluids.

## Square Cavity
### Domain
Square cavity with velocity boundary condition Γ_1 = (1,0) on the top (lid) of the cavity, and Γ_2 = (0,0) on the rest of the walls.


# Simulação de Transporte de Calor por Convecção-Difusão com FreeFEM

Este projeto implementa, no FreeFEM, a resolução da equação de convecção-difusão de temperatura acoplada com o sistema de Navier-Stokes. O modelo simula o transporte de calor em um fluido incompressível com escoamento bidimensional, considerando o efeito da velocidade no transporte da temperatura e possível dependência da viscosidade com a temperatura.

---

## 🔬 Modelo Matemático

### Sistema de Navier-Stokes (incompressível)
\[
\begin{aligned}
\rho \left( \frac{\partial \mathbf{u}}{\partial t} + \mathbf{u} \cdot \nabla \mathbf{u} \right) - \nabla \cdot (\mu(T) \nabla \mathbf{u}) + \nabla p &= \mathbf{f} \\
\nabla \cdot \mathbf{u} &= 0
\end{aligned}
\]

### Equação de Convecção-Difusão para a Temperatura
\[
\frac{\partial T}{\partial t} + \mathbf{u} \cdot \nabla T - \nabla \cdot (\kappa \nabla T) = Q
\]

Onde:
- \( \mathbf{u} \): campo de velocidade
- \( p \): pressão
- \( T \): temperatura
- \( \mu(T) \): viscosidade (possivelmente variável com a temperatura)
- \( \kappa \): difusividade térmica
- \( Q \): fonte de calor
- \( \rho \): densidade (constante)

---

## 🛠️ Implementação

### Características:
- **Espaço de aproximação:** P2 para velocidade, P1 para pressão, P1 para temperatura.
- **Método numérico:** Galerkin com estabilização se necessário (upwind ou SUPG).
- **Tempo:** Esquema implícito de Euler (ou semi-implícito).
- **Acoplamento:** Newton ou Oseen (linearizado).
- **Adaptação de malha:** via `adaptmesh` para refinar onde gradientes de temperatura ou velocidade são intensos.

---

## 📁 Estrutura dos Arquivos

- `navier-stokes-temp.edp` – Código principal do problema acoplado Navier-Stokes + temperatura.
- `malha.edp` – Geração da malha (ou carregamento de malha `.msh` externa).
- `README.md` – Este arquivo.

---

## ⚙️ Parâmetros do Código

Os principais parâmetros físicos e numéricos são definidos no início do código:

```cpp
real Re = 100;        // Número de Reynolds
real Pr = 0.71;       // Número de Prandtl
real dt = 0.01;       // Passo de tempo
int nT = 100;         // Número de passos de tempo
real mu0 = 1.0;       // Viscosidade base
real T0 = 0.0;        // Temperatura de referência
