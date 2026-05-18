# References

> Formal citations for all works mentioned in *The Geometry of Meaning*.

---

## Geometric Algebra + Machine Learning

### GATr — Geometric Algebra Transformer

**Brehmer, J., de Haan, P., Behrends, S., and Cohen, T. (2023).**
Geometric Algebra Transformer.
*Advances in Neural Information Processing Systems (NeurIPS), 2023.*
arXiv:2305.18415 [cs.LG].

> Introduces the Geometric Algebra Transformer (GATr), a general-purpose architecture for geometric data using projective geometric algebra Cl(3,0,1). Achieves E(3) equivariance by construction. Applied to n-body modeling, mesh estimation, and robotic motion planning.

**Links:** [arXiv](https://arxiv.org/abs/2305.18415) · [GitHub](https://github.com/Qualcomm-AI-research/geometric-algebra-transformer)

---

### GAFL — Geometric Algebra Flow Matching

**Wagner, J., et al. (2024).**
Generating Highly Designable Proteins with Geometric Algebra Flow Matching.
*Advances in Neural Information Processing Systems (NeurIPS), 2024.*
arXiv:2411.05238 [cs.LG].

> Uses projective geometric algebra with flow matching on SE(3)^N for protein backbone generation. Geometric products enable higher-order message passing between residues.

**Links:** [arXiv](https://arxiv.org/abs/2411.05238) · [GitHub](https://github.com/hits-mli/gafl)

---

### L-GATr — Lorentz-Equivariant GATr

**Authors TBD (2024).**
Lorentz-Equivariant Geometric Algebra Transformers for High-Energy Physics.
*Advances in Neural Information Processing Systems (NeurIPS), 2024.*

> Extends GATr with Lorentz symmetry equivariance for high-energy physics applications.

**Links:** [NeurIPS](https://neurips.cc/virtual/2024/poster/94796)

---

### LaB-GATr

**Authors TBD (2024).**
LaB-GATr: Geometric Algebra Transformers for Large Biomedical Surface and Volume Data.
*International Conference on Medical Image Computing and Computer-Assisted Intervention (MICCAI), 2024.*

> Adapts GATr to large-scale 3D medical data with geometric tokenization.

---

## Geometric Algebra for Language & NLP

### FGA — Functional Geometric Algebra for NLP

**Pustejovsky, J. (2026).**
Toward a Functional Geometric Algebra for Natural Language Semantics.
arXiv:2604.25902 [cs.CL].

> Argues Geometric Algebra provides a mathematically superior foundation for natural language semantics compared to linear algebra. Proposes Functional Geometric Algebra (FGA) framework with typed, compositional semantics supporting inference and interpretability.

**Links:** [arXiv](https://arxiv.org/abs/2604.25902)

---

### CliffordNet

**Authors TBD (2026).**
CliffordNet: All You Need is Geometric Algebra.
arXiv:2601.06793 [cs.CV].

> Proposes the Clifford Algebra Network (CAN/CliffordNet), a vision backbone grounded purely in Geometric Algebra. Represents latent representations as multivectors evolving under the full spectrum of geometric operations.

**Links:** [arXiv](https://arxiv.org/abs/2601.06793)

---

## Language Modeling & Flow Matching

### S-FLM — Hyperspherical Flow Language Model

**Authors TBD (2026).**
Language Modeling with Hyperspherical Flows.
arXiv:2605.11125 [cs.CL].

> Introduces S-FLM, a latent flow language model on the hypersphere S^{d-1}. Generates sequences by rotating vectors along a velocity field learned with cross-entropy. Baseline for the gaflowlm project.

**Links:** [arXiv](https://arxiv.org/abs/2605.11125)

---

### Attractor Models (Solve the Loop)

**Fein-Ashley, J. and Rashidinejad, P. (2026).**
Solve the Loop: Attractor Models for Language and Reasoning.
arXiv:2605.12466 [cs.LG].

> Introduces Attractor Models using deep equilibrium (DEQ) fixed-point solvers for language modeling and reasoning. Decouples effective depth from memory. Base architecture for the gattrlm project.

**Links:** [arXiv](https://arxiv.org/abs/2605.12466) · [GitHub](https://github.com/attractor-models) · [Project Page](https://attractor-models.github.io)

---

## Word Embeddings & Semantics

### Word2Mvec

**Mani, A. (2024).**
Representing Words in a Geometric Algebra.
*Senior Thesis, Princeton University.*

> Investigates representing words as multivectors instead of vectors. Word2Mvec model slightly outperforms standard Word2Vec+FC baseline on word similarity and analogy tasks, suggesting benefits from geometric product interactions.

**Links:** [Princeton PACM](https://www.pacm.princeton.edu/sites/default/files/pacm_arjunmani_0.pdf)

---

## Foundational GA Texts

1. **Macdonald, A.** *Linear and Geometric Algebra.* CreateSpace, 2011.
   — The gentlest introduction to GA from linear algebra foundations.

2. **Dorst, L., Fontijne, D., and Mann, S.** *Geometric Algebra for Computer Science: An Object-Oriented Approach to Geometry.* Morgan Kaufmann, 2007.
   — Practical and intuitive, with applications to graphics and robotics.

3. **Hestenes, D. and Sobczyk, G.** *Clifford Algebra to Geometric Calculus: A Unified Language for Mathematics and Physics.* D. Reidel, 1984.
   — The original modern treatment. Mathematically rigorous.

---

## Project Repositories

| Project | Description | URL |
|---------|-------------|-----|
| **gaflowlm** | GA flow matching for language | [github.com/pebaryan/gaflowlm](https://github.com/pebaryan/gaflowlm) |
| **gattrlm** | Clifford attractor model | [github.com/pebaryan/gattrlm](https://github.com/pebaryan/gattrlm) |
| **gamuon** | GA reformulation of Muon optimizer | [github.com/pebaryan/gamuon](https://github.com/pebaryan/gamuon) |
| **galbook** | This book (manuscript, roadmap, reviews) | [github.com/pebaryan/galbook](https://github.com/pebaryan/galbook) |

---

*Last updated: May 2026. Years verified against arXiv submission dates and conference proceedings.*
