"""Small smoke test so you can run `python -m vqe_molecular_energy`."""

from . import molecules

def main():
    try:
        # If your moved molecules.py has real functions, this will exercise them.
        if hasattr(molecules, "example_hamiltonian") and hasattr(molecules, "energy_expectation"):
            h = molecules.example_hamiltonian()
            psi = [1.0, 0.0]
            E = molecules.energy_expectation(psi, h)
            print(f"Example energy: {E}")
        else:
            print("Package imported successfully, but no example functions found in molecules.")
    except Exception as e:
        print("Package import succeeded but running example failed:", e)

if __name__ == "__main__":
    main()