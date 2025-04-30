**Scientific Website:** [https://jamesclick.github.io/clique-modular-unsat-proof](https://jamesclick.github.io/clique-modular-unsat-proof)
# Formalization and Experimental Validation of the Modular Signature Method for UNSAT Detection

## Introduction

The detection of unsatisfiability (UNSAT) in Boolean formulas is a cornerstone problem in theoretical computer science, with critical implications in complexity theory, SAT solving, and logic programming. Traditional methods for UNSAT detection often rely on extensive combinatorial search or resolution techniques, which can be computationally expensive for large instances.

This project introduces a novel modular algebraic approach, where Boolean formulas are mapped into modular arithmetic structures. By assigning integer weights to variables and computing modular residues, we propose a potential "signature" for identifying UNSAT instances in a more algebraic and scalable way.

---

## Methodology

Given a CNF (Conjunctive Normal Form) Boolean formula φ, we define a weighted sum S(φ; w, M) under integer weight assignments w and modulus M:

- Assign integer weights to literals based on different strategies (sequential, exponential, or hash-based).
- For each clause, compute the weighted sum of its literals modulo a prime M.
- Aggregate the clause residues to obtain the modular signature S(φ).

The **conjecture** underlying this method is:  
> **If φ is UNSAT, then S(φ; w, M) ≡ 0 for all sufficiently large primes M and appropriately structured weight schemes w.**

This version of the project focuses on **experimental validation** of this conjecture across multiple benchmark families.

---

## Experimental Results

Extensive empirical testing was conducted on classical benchmarks:

- **Pigeonhole Principle (PHP) instances**: PHP(3,2), PHP(4,3), PHP(5,4), PHP(6,5)
- **Random 3-SAT UNSAT instance**: 20 variables, custom generated
- **Tseitin formulas**: Structural UNSAT formulas
- **XOR-SAT instances**: Algebraic UNSAT examples

For each instance, we applied three weight schemes (Sequential, Exponential, Hash-based) and tested multiple prime moduli (97, 101, 103).  
The results showed consistent zero residues (S(φ) ≡ 0) across all UNSAT instances tested, reinforcing the potential of modular signatures as a detection method.

---

## Limitations

While the experimental results are encouraging, this work is still a first step. Several limitations are recognized:

- **Absence of a General Proof**: No formal theorem yet guarantees that S(φ) = 0 for all UNSAT formulas universally.
- **Pathological Cases**: Certain highly symmetric or artificial formulas might evade detection.
- **Weight and Modulus Optimization**: No theoretical criteria for selecting optimal weight schemes and modulus sizes yet.
- **Scalability**: The current computational cost (O(n·k) per configuration) may impact performance on very large instances.

These limitations are declared transparently to guide future work and community feedback.

---

## Future Work

The next stages of this research aim to:

- Formalize mathematical proofs establishing necessary and sufficient conditions for modular UNSAT detection.
- Analyze robustness against pathological CNF structures.
- Develop criteria for optimized weight assignment and modulus selection.
- Parallelize computations (e.g., GPU acceleration) to enhance scalability.
- Extend the method to richer logical systems beyond CNF (e.g., QBF, pseudo-Boolean constraints).
- Combine modular signatures with classic SAT solvers to guide heuristic pruning.

---

## Materials Available

The repository and accompanying website provide:

- **Scientific Article (PDF)**: Full description of the method, experiments, results, and perspectives.
- **Complete Project Package (ZIP)**: Source codes, datasets, and preliminary notes.
- **Extended Residue Dataset (CSV)**: Detailed residues computed for each instance × weight scheme × modulus.
- **Video Presentation (MP4)**: Overview of the methodology and project motivation.

All materials are openly accessible for inspection, reproduction of experiments, and future collaboration.

---

## Acknowledgments

We thank all collaborators and professors who provided valuable feedback during the project development. Special thanks to the reviewers who emphasized the importance of empirical validation and honest acknowledgment of current limitations.

---

## About the Author

Jamesson Richard Campos Santos da Graça (JamesClick) is an independent researcher passionate about theoretical computer science, combinatorics, and computational logic.  
This work represents his first major contribution toward the modular analysis of satisfiability problems.

---
