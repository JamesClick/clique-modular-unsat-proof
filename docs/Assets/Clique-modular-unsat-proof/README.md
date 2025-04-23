# Modular UNSAT Proof – Computational Package

This package contains all necessary files to reproduce the results described in the project.

## Files

- `formula.cnf`: A known UNSAT 3-SAT formula used in the tests.
- `pesos_utilizados.txt`: List of weights used in the vector sum (hash and polynomial strategies).
- `residuos_resultado.csv`: Output of the modular residue sums for each weight/modulus.
- `calcular_residuos.py`: Python script to compute S(φ) mod M for CNF formulas.
- `graficos/*.png`: Graphs showing the difference between SAT and UNSAT cases.

## Usage

1. Run `calcular_residuos.py` to test a CNF formula with chosen weights and moduli.
2. Compare the outputs with `residuos_resultado.csv` for verification.
3. Use `formula.cnf` as your starting point or replace it with another known CNF formula.

For more information, visit the project website:  
[https://jamesclick.github.io/clique-modular-unsat-proof/](https://jamesclick.github.io/clique-modular-unsat-proof/)
