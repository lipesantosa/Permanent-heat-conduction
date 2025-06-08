# Numerical Simulation of Convective-Diffusive Heat Transport by an Incompressible Viscous Flow

In this work we present a numerical study of heat transport through a moving fluid, in which convection and diffusion processes are considered. The transport is carried out by a newtonian, laminar, irrotational, incompressible and transient flow of a fluid based on the Navier-Stokes equations and the Convection-Diffusion equation. This study provides a basis for more theoretical investigations involving stability, existence of weak solutions and extensions to newtonian fluids.

---

## Square Cavity
### Domain
Square cavity with velocity boundary condition Γ_1 = (1,0) on the top (lid) of the cavity, and Γ_2 = (0,0) on the rest of the walls.

---

## Mathematical Model
### Incompressible Navier-Stokes System
\[
\begin{aligned}
\rho \left( \frac{\partial \mathbf{u}}{\partial t} + \mathbf{u} \cdot \nabla \mathbf{u} \right) - \nabla \cdot (\mu(T) \nabla \mathbf{u}) + \nabla p &= \mathbf{f} \\
\nabla \cdot \mathbf{u} &= 0
\end{aligned}
\]

### Convection-Diffusion Equation for Temperature
\[
\frac{\partial T}{\partial t} + \mathbf{u} \cdot \nabla T - \nabla \cdot (\kappa \nabla T) = Q
\]

Where:
- \( \mathbf{u} \): velocity field
- \( p \): pressure
- \( T \): temperature
- \( \mu(T) \): viscosity (constant)
- \( \kappa \): thermal diffusivity
- \( Q \): heat source
- \( \rho \): density (constante)

---

## Implementation
- **Approximation space:** P2 for velocity, P1 for pressure, P1 for temperature.
- **Numerical Method:** Galerkin with inf-sup condition by Taylor-Hood elements.
- **Time:** Semi-discrete formulation of time.

---
