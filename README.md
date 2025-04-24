# clique-modular-unsat-proof

**Formal and Computational Proof of UNSAT Detection via Modular Weighted Sums**  
*A novel approach for NP-complete formula analysis using GPU, Big Data, and algebraic signatures.*

---

## Overview

This repository presents a **mathematical and computational framework** to detect **UNSAT Boolean formulas** through **modular weighted sums**.  
Our method introduces a residue-based signature that holds consistently for UNSAT instances across **orthogonal weight vectors** and **large moduli**.

The approach is designed for scalability and precision, combining:
- Modular arithmetic
- Weight orthogonality
- Clause vector encoding
- Massive computational testing (GPU + Big Data)

> **Main Conjecture:**  
> If a Boolean formula φ is UNSAT, then  
> **S(φ) ≡ 0 mod M** for a wide range of weight vectors and prime moduli M.

---

## Key Contributions

- **Novel Signature** for detecting Boolean unsatisfiability.
- Extensive validation using **PHP(m,n)** and **random 3-SAT UNSAT** instances.
- GPU-accelerated computation of modular residues.
- Mathematical formalization in LaTeX and implementation in Python.
- Public repository with all results, graphs, CNF inputs, and datasets.

---

## Project Files

| File | Description |
|------|-------------|
| `docs/index.html` | Scientific web presentation |
| `assets/projeto_final_numerado.pdf` | Full PDF with proofs and results |
| `assets/residuos_resultado.csv` | Table of computed modular residues |
| `assets/pesos_utilizados.txt` | Weights used for each experiment |
| `assets/calcular_residuos.py` | Python script for residue computation |
| `assets/formula.cnf` | Example CNF used in validation |
| `images/` | Graphs generated during evaluation |

---

## Key Results

- **UNSAT formulas** consistently yield **S(φ) ≡ 0** across all weight families and moduli.
- **SAT formulas** show random and diverse S(φ) mod M values.
- Graphs and tables confirm a robust separation between SAT and UNSAT behavior.

---

## Live Scientific Page

Access the full scientific site here:  
**[https://jamesclick.github.io/clique-modular-unsat-proof](https://jamesclick.github.io/clique-modular-unsat-proof)**

Includes:
- Mathematical foundations
- Experimental graphs
- Modular formula signature
- Downloadable datasets and code
- Final PDF paper

---

## Contact & Author

**Jamesson Richard Campos Santos da Graça**  
*Independent Researcher (JamesClick)*  
GitHub: [@JamesClick](https://github.com/JamesClick)

If you wish to endorse this work for arXiv submission or collaborate:  
please visit the website or contact the author directly.

---

## License

This project is open-source and freely available for academic and research purposes.

---

> “Simplicity is the ultimate sophistication.” — *Leonardo da Vinci*
