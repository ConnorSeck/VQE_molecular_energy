import importlib
import pytest

def test_import_package():
    pkg = importlib.import_module("vqe_molecular_energy")
    assert hasattr(pkg, "__version__")

def test_example_energy_if_present():
    molecules = importlib.import_module("vqe_molecular_energy.molecules")
    if hasattr(molecules, "example_hamiltonian") and hasattr(molecules, "energy_expectation"):
        h = molecules.example_hamiltonian()
        psi = [1.0, 0.0]
        E = molecules.energy_expectation(psi, h)
        assert pytest.approx(E, rel=1e-9) == 1.0
    else:
        pytest.skip("No example functions in molecules module; update test to match your API")
        