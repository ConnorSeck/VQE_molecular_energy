import numpy as np
from qiskit_nature.second_q.drivers import PySCFDriver
from qiskit_nature.second_q.mappers import JordanWignerMapper
from qiskit_nature.units import DistanceUnit
from scipy.sparse import csc_matrix
from scipy.sparse.linalg import eigsh

def h2_qubit_hamiltonian(R):
    geometry = f"H 0 0 0; H 0 0 {R}"
    driver = PySCFDriver(
        atom=geometry,
        basis="sto3g",
        charge=0,
        spin=0,
        unit=DistanceUnit.ANGSTROM,
    )
    problem = driver.run()
    fermionic_op = problem.hamiltonian.second_q_op()
    qubit_op = JordanWignerMapper().map(fermionic_op)
    return qubit_op, problem

def exact_energy(qubit_op, problem):
    # Convert SparsePauliOp → dense matrix
    H = qubit_op.to_matrix()

    # Exact diagonalization
    eigvals = np.linalg.eigvalsh(H)
    energy = np.min(eigvals).real

    # Add nuclear repulsion
    energy += problem.nuclear_repulsion_energy

    return energy
def exact_energy_sparse(qubit_op, problem):

    # Convert to sparse matrix
    H = csc_matrix(qubit_op.to_matrix())
    
    E0 = eigsh(H, k=1, which='SA', return_eigenvectors=False)[0].real
    
    E0 += problem.nuclear_repulsion_energy
    return E0

def LiH_qubit_hamiltonian(R):
    geometry = f"Li 0 0 0; H 0 0 {R}"

    driver = PySCFDriver(
        atom=geometry,
        basis="sto3g",
        charge=0,
        spin=0,
        unit=DistanceUnit.ANGSTROM,
    )

    problem = driver.run()

    fermionic_op = problem.hamiltonian.second_q_op()

    mapper = JordanWignerMapper()
    qubit_op = mapper.map(fermionic_op)

    return qubit_op, problem



    # Convert to sparse matrix
    H = csc_matrix(qubit_op.to_matrix())
    
    E0 = eigsh(H, k=1, which='SA', return_eigenvectors=False)[0].real
    
    E0 += problem.nuclear_repulsion_energy
    return E0

def HeH_qubit_hamiltonian(R):
    geometry = f"He 0 0 0; H 0 0 {R}"

    driver = PySCFDriver(
        atom=geometry,
        basis="sto3g",
        charge=1,
        spin=0,
        unit=DistanceUnit.ANGSTROM,
    )

    problem = driver.run()

    fermionic_op = problem.hamiltonian.second_q_op()

    mapper = JordanWignerMapper()
    qubit_op = mapper.map(fermionic_op)

    return qubit_op, problem



