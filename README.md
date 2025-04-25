# Modular UNSAT Signature – JamesClick

This repository presents a novel approach for detecting unsatisfiable Boolean formulas using modular weighted sums applied to CNF clauses.

By assigning orthogonal weight vectors and evaluating their modular sum across multiple primes, the method consistently distinguishes satisfiable from unsatisfiable instances without relying on classical resolution.

---

## Highlights

- **Modular Algebraic Signature:** UNSAT formulas yield zero residues across all tested weight vectors.
- **Generalization:** Results validated over PHP, 3-SAT, XOR-SAT and Tseitin formulas.
- **Lightweight & Scalable:** Ideal for preprocessing or hybrid integration with SAT solvers.

---

## Reproducibility

To test the modular signature method locally:

1. **Clone the repository**
```bash
git clone https://github.com/JamesClick/clique-modular-unsat-proof
cd clique-modular-unsat-proof
