# VQE Molecular Energy

This repository contains a study of molecular ground-state energies
using the Variational Quantum Eigensolver (VQE) implemented with
Qiskit and Qiskit Nature.

The project focuses on small molecular systems and includes
exact diagonalization benchmarks as well as noisy simulations.

## Project Structure

- `src/vqe_molecular_energy/`  
  Core reusable code for molecular Hamiltonians and exact solvers.

- `notebooks/`  
  Jupyter notebooks containing numerical experiments and analysis.

- `tests/`  
  Basic unit tests for core functionality.

## Methods

- Second-quantized molecular Hamiltonians (Qiskit Nature)
- Jordan–Wigner fermion-to-qubit mapping
- Exact diagonalization (dense and sparse)
- Variational Quantum Eigensolver (VQE)
- Noise models using Qiskit Aer

## Installation

Create a virtual environment and install the project:

```bash
pip install -e .

