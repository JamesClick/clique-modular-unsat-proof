# Residue Dataset Documentation - Modular Signature Method

This dataset contains modular residue results computed from Boolean formulas using the Modular Signature Method for UNSAT detection. These files support the experimental results presented in the article:  
**"Modular Signatures for UNSAT Detection: Experimental Validation and Theoretical Perspectives"**

---

## Purpose

The goal of this dataset is to provide transparent, reproducible, and structured access to the experimental results generated from applying weighted modular arithmetic to well-known unsatisfiable CNF formulas.

---

## Files Included

### `Modular_Signatures_Extended.csv`

This file contains raw residue results for a range of benchmark formulas, including:

- **PHP(n, n–1)** instances such as `PHP(3,2)`, `PHP(4,3)`, `PHP(5,4)`, and `PHP(6,5)`
- **Random 3-SAT (UNSAT)** formulas with 20 variables
- **Tseitin formulas**
- **XOR-SAT examples**

---

## Column Description

| Column Name       | Description                                                                 |
|-------------------|-----------------------------------------------------------------------------|
| `Formula`         | Identifier of the CNF formula (e.g., `php65_unsat.cnf`)                     |
| `WeightScheme`    | Type of weight applied (e.g., `Sequential`, `Exponential`, `Hash`)         |
| `Modulus`         | Prime number used as modulus M (e.g., 97, 101, 103)                         |
| `ResidueVector`   | Vector of residues per clause under the chosen weights and modulus         |
| `TotalResidue`    | Final aggregated modular sum S(φ;w,M); should be 0 for UNSAT cases         |
| `Satisfiability`  | Ground-truth classification of the formula (e.g., `UNSAT`, `SAT`)          |

---

## Format & Encoding

- UTF-8 comma-separated values (.csv)
- Header included
- Plain text, readable by any data analysis tool (Python, R, Excel, etc.)

---

## How to Interpret

If `TotalResidue = 0` for all weight schemes and prime moduli across a formula, this supports the **Modular UNSAT Conjecture**, suggesting the formula is unsatisfiable.

Conversely, `TotalResidue ≠ 0` may indicate satisfiability or edge cases under further investigation.

---

## Reproducibility Note

Each result in this CSV was generated from CNF files provided in the project ZIP, using modular residue computation algorithms described in the paper and implemented in the provided source code.

We encourage researchers to validate, extend or challenge these results using their own solvers, weights or prime moduli.

---

