# VQE for Molecular Ground-State Energies

**Module:** QC803 – Quantum Computing  
**Project:** Variational Quantum Eigensolver (VQE) – Molecular Energy Curves  
**Student:** Connor Seckerson
**Date:** January 2026

---

## 📖 Project Overview

This project implements the Variational Quantum Eigensolver (VQE) to compute
ground-state energy curves of small molecules as a function of bond length.
We focus primarily on the hydrogen molecule (H₂) in the STO-3G basis.

The goals are:
- Compute reference (exact) ground-state energies classically
- Implement VQE with different ansätze and depths
- Compare classical optimizers
- Analyze convergence, variance, and noise effects
- Estimate equilibrium bond length and energy

---

## 🧪 Methods

- **Hamiltonian generation:** Qiskit Nature + PySCF
- **Reference energies:** Exact diagonalization
- **VQE ansatz:** Parameterized RX/RZ layers with entanglement
- **Optimizers:** COBYLA, SPSA, SLSQP
- **Noise models:** Depolarizing and readout error
- **Backend:** Qiskit Aer (statevector and shot-based)

---

## 📂 Repository Structure

```text
src/            Core Python modules
notebooks/      Jupyter notebooks for experiments
data/           Reference and VQE-generated data
results/        Figures and tables used in the report
environment/    Environment setup files
report/         Final PDF report
