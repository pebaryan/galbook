## 5. The GA+ML Landscape: A Map of the Frontier

Geometric Algebra in machine learning is a small but rapidly growing field. It's not one thing — it's several distinct threads of research, each with a different motivation and set of results. Let's map the territory.

### 5.1 GATr: Geometric Algebra Transformer (Qualcomm AI Research, 2023)

The most well-known GA + ML paper is the Geometric Algebra Transformer, or **GATr**, published at NeurIPS 2023 by researchers at Qualcomm AI Research.

GATr's key insight: many real-world problems involve geometric data — points, vectors, rotations, translations — that have built-in symmetries under rotations, reflections, and translations (the Euclidean group E(3)). Standard neural networks must learn these symmetries from data (through data augmentation), which is inefficient. GATr uses projective geometric algebra Cl(3,0,1) to encode these transformations *directly in the architecture*.

The 16-dimensional projective geometric algebra is remarkable: it can represent points, lines, planes, spheres, rotations, and translations all as first-class citizens. A rotation isn't a 3×3 matrix — it's a rotor, just like the ones we met in Chapter 4. A translation isn't a vector addition — it's also a rotor (a translation rotor in the conformal model).

GATr achieves **E(3) equivariance** by construction: rotate the input, and the output rotates the same way. This is critical for applications like:
- **N-body physics**: predicting particle trajectories respects rotational symmetry
- **Robotics**: a robot arm's decision shouldn't depend on arbitrary rotations of the scene
- **Medical imaging**: anatomical structures should be recognized regardless of orientation

GATr consistently outperformed non-geometric and equivariant baselines across these tasks. It was followed by **L-GATr** (Lorentz-equivariant for high-energy physics) and **LaB-GATr** (for large biomedical data).

But GATr wasn't designed for language. It was designed for 3D geometric reasoning. The question of how to adapt its ideas to the very different geometry of language is what drives much of the research we'll discuss next.

### 5.2 GAFL: Geometric Algebra Flow Matching (HITS, 2024)

**GAFL** (Geometric Algebra Flow Matching), published at NeurIPS 2024, uses GA for a different purpose: generating protein backbone structures.

Proteins are chains of amino acids, each with a position and orientation in 3D space. The space of all possible protein backbones is the product of SE(3) groups — rotation + translation for each amino acid. This is a highly structured geometric space.

GAFL represents protein frames as elements of the projective geometric algebra (the same Cl(3,0,1) as GATr) and uses the geometric product for message passing between residues. The flow matching objective learns to interpolate from noise to valid protein structures.

The results are impressive: GAFL generates protein backbones with high "designability" (the fraction of generated structures that fold into stable proteins) while preserving a realistic distribution of secondary structures. Other methods tend to over-represent alpha helices; GAFL captures the full diversity.

What GAFL showed is that Geometric Algebra's bilinear products — the geometric product between multivectors — capture richer interactions than standard vector operations. This is the same principle that makes GA interesting for language: words don't just *align* (dot product) — they *interact* (geometric product).

### 5.3 FGA: Functional Geometric Algebra for NLP (Pustejovsky, 2026)

The most directly relevant work for our story is James Pustejovsky's **Functional Geometric Algebra** (FGA), published in April 2026. It's a 43-page paper that argues — passionately and in detail — that Geometric Algebra is a mathematically superior foundation for natural language semantics.

Pustejovsky's core claim: current approaches to language semantics are built on linear algebra (vectors, matrices, tensors), but the operations we *actually need* for compositional semantics — type coercion, operator-level contrasts, semantic transformation — are geometric operations that linear algebra expresses awkwardly or not at all.

FGA proposes that words and phrases should be represented as **multivectors**, not vectors. The scalar grade captures category information. The vector grade captures entity-level semantics. The bivector grade captures relational and transformational structure. The geometric product between two word multivectors produces a richer interaction than any composition of dot products.

Crucially, Pustejovsky shows that many operations already implicit in transformer attention can be made *explicit* through GA — transforming opaque neural computations into interpretable geometric transformations. The paper includes worked examples of type coercion ("began the book" → began reading/writing the book) expressed as operator-level geometric operations.

This paper is important not just for its technical contributions but for its timing: it signals that the GA-for-NLP idea has moved from fringe speculation to serious academic discourse.

### 5.4 Other Threads

Several other works are worth noting:

- **CliffordNet** (2025): proposes Clifford algebras as a general framework for neural network design, including for NLP tasks
- **Word2Mvec** (Princeton, 2024): a senior thesis showing that representing words as multivectors (instead of vectors) and taking geometric products outperforms standard Word2Vec on word similarity and analogy tasks
- **LLM + CGA for 3D scene editing** (2024): uses conformal geometric algebra as an intermediate representation for LLM-driven 3D manipulation

What unites these threads is the belief that **the mathematical language we use shapes what we can think about**. Linear algebra is good for many things, but it's not the best language for describing composition, transformation, and geometric structure. Geometric Algebra might be.

---

