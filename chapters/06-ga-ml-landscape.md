## 6. Explorations: How Others Apply GA

Chapter 5 showed how attention works — and where it falls short. The output is a weighted sum: linear blending, not transformation. This limitation isn't unique to language. Across machine learning, researchers have encountered problems where standard vector operations don't capture the structure of the domain.

This chapter explores three of those problems and how Geometric Algebra provides a path forward. Each section follows the same arc: the problem, the GA opportunity, and the work that's been done.

---

### The Problem of 3D Symmetry

**The Problem:**

Many real-world tasks involve 3D geometric data — points, vectors, rotations, translations. A protein's structure, a robot's pose, a molecule's conformation: all are fundamentally geometric.

Standard neural networks treat this geometry as raw numbers. A point is three coordinates. A rotation is nine numbers in a 3×3 matrix. The network must learn from data that rotating the input should rotate the output — a constraint called **E(3) equivariance**.

This is inefficient. The network learns the symmetry from scratch, through data augmentation, when the symmetry is built into the problem. Worse, the representation obscures the geometry: nine numbers in a rotation matrix don't tell you the rotation plane or angle.

**The GA Opportunity:**

Geometric Algebra makes the symmetry *explicit*. In projective geometric algebra Cl(3,0,1):
- A point is a multivector with a specific grade structure
- A rotation is a rotor (cosine + sine × bivector) — the plane and angle are explicit
- A translation is *also* a rotor in the conformal model

The algebra respects E(3) by construction. Rotate the input multivector, and the output rotates the same way — no training required.

**Existing Work:**

**GATr** (Geometric Algebra Transformer, Qualcomm AI Research, NeurIPS 2023) applies this to 3D geometric reasoning. It replaces standard transformer layers with GA equivalents: multivector projections instead of vector projections, geometric products instead of dot products.

The 16-dimensional projective GA can represent points, lines, planes, spheres, rotations, and translations as first-class citizens. GATr achieves E(3) equivariance without data augmentation.

Results: consistent outperformance on N-body physics, robotics scenes, and medical imaging. The network doesn't waste capacity learning symmetry — it starts with it.

GATr was followed by **L-GATr** (Lorentz-equivariant for high-energy physics) and **LaB-GATr** (large biomedical data), showing the approach generalizes across domains.

**Why This Matters for Language:**

GATr wasn't designed for language. But it proves a principle: when you encode domain structure into the algebra, the architecture becomes more data-efficient. The question isn't whether GA helps 3D reasoning — it clearly does. The question is whether language has similar hidden structure waiting to be uncovered.

---

### The Problem of Structured Generation

**The Problem:**

Generating valid protein structures is hard. A protein backbone isn't just 3D coordinates — it's a sequence of amino acids, each with a specific orientation relative to its neighbors. The space of valid structures is tiny compared to the space of all possible coordinate tuples.

Standard diffusion models operate on raw coordinates. They learn the structure of valid proteins implicitly, through millions of examples. But they struggle to capture global constraints: bond angles, chirality, steric clashes. The result is generated structures that look protein-like locally but violate basic physical constraints globally.

**The GA Opportunity:**

Protein frames live in SE(3) — the group of rotations and translations. This is exactly what geometric algebra represents naturally. Instead of generating raw coordinates, generate *frames* as multivectors in Cl(3,0,1).

The geometric product enforces structure. Invalid combinations produce high-grade terms that can be penalized. Valid combinations stay within the algebraic subspace of physical configurations.

**Existing Work:**

**GAFL** (Geometric Algebra Flow Matching, HITS, NeurIPS 2024) applies this to protein backbone generation. It represents each amino acid frame as a multivector and uses the geometric product for message passing between residues.

The flow matching objective learns to interpolate from noise to valid structures — but "valid" is now defined algebraically, not just statistically. The model learns to flow toward configurations that respect the geometric constraints of protein structure.

Results: GAFL generates backbones with higher "designability" (fraction that fold into stable proteins) than coordinate-based methods. Other methods over-represent alpha helices; GAFL captures the full diversity of secondary structures.

**The Deeper Insight:**

GAFL showed that the geometric product captures richer interactions than standard vector operations. Coordinates add; multivectors *compose*. The difference is structure preservation — the algebra keeps track of relationships that raw numbers lose.

This is the same principle that matters for language: words don't just *align* (dot product), they *interact* (geometric product). GAFL proves this principle works at scale for structured generation.

---

### The Problem of Compositional Semantics

**The Problem:**

Language is compositional. The meaning of "red car" isn't the sum of "red" and "car" — it's an emergent property of their interaction. Current approaches handle this through attention: weighted sums of vector representations. But attention is linear. It blends; it doesn't transform.

Worse, standard embeddings conflate different kinds of information into a single vector:
- Grammatical category (noun, verb, adjective)
- Core semantic content (what the word denotes)
- Relational structure (how it connects to other words)

These get tangled together. When "king" transforms to "queen," the vector offset captures the correlation, but not the underlying geometric operation.

**The GA Opportunity:**

Multivectors naturally separate these aspects across grades:
- Scalar: category, intensity, register
- Vector: core semantic content
- Bivector: relational and transformational structure

The geometric product between two word-multivectors produces cross-grade terms that capture composition. "Red" (scalar intensity + vector color) composed with "car" (scalar object-ness + vector concept + bivector affordances) produces a bivector term representing the color-object relationship.

Attention becomes geometric: instead of dot products, use the scalar part of the geometric product. Instead of weighted sums, use the full geometric product between query and value.

**Existing Work:**

**FGA** (Functional Geometric Algebra, Pustejovsky, 2026) makes the case for GA as a foundation for natural language semantics. It's a 43-page argument that the operations we need for compositional semantics — type coercion, operator-level contrasts, semantic transformation — are geometric operations poorly expressed in linear algebra.

The paper shows that transformer attention contains implicit geometric operations that GA makes explicit. Worked examples include:
- Type coercion: "began the book" → began reading/writing, expressed as geometric transformations
- Operator contrasts: the difference between "hit" (contact) and "strike" (forceful contact) as grade projections
- Semantic transformation: negation, modality, and aspect as rotor operations

**CliffordNet** (2025) proposes Clifford algebras as a general framework for neural network design, with NLP applications.

**Word2Mvec** (Princeton, 2024): A senior thesis showing multivector representations with geometric products outperform Word2Vec on similarity and analogy tasks. The rotor representation captures analogies as shared transformations rather than approximate vector offsets.

**Why This Is Different:**

GATr and GAFL apply GA to problems with obvious geometric structure — 3D coordinates, protein frames. Language's geometry is hidden. But FGA argues it's there: semantics *is* geometry, just not the spatial kind we visualize.

The multivector hypothesis from Chapter 8 extends this: language has grade structure waiting to be discovered. The work exists at the frontier — not proven at scale, but pointing toward a research program.

---

### What Unites These Explorations

Three different domains. Three different problems. One common thread:

| Domain | Standard Approach | GA Approach |
|--------|------------------|-------------|
| 3D reasoning | Coordinates, matrices | Multivectors, rotors |
| Protein generation | Raw coordinates | SE(3) frames as multivectors |
| Language semantics | Vector embeddings | Grade-separated multivectors |

In each case, the standard approach treats the domain as raw numbers and learns structure from data. The GA approach encodes structure into the algebra, making the network's job easier and the representations more interpretable.

The question for the rest of this book: can we bring these threads together? GATr's architecture, GAFL's generation, FGA's semantics — unified in a single language model that thinks in geometric algebra.

---
