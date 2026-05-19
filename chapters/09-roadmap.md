## 9. The Roadmap

Geometric Algebra isn't the only mathematical frontier in AI, but it's a particularly promising one because of a fundamental observation:

**Neural networks are already doing geometry. They're just using the wrong vocabulary.**

The word embeddings, rotations, transformations, and comparisons that language models perform daily are inherently geometric operations. But the tools we use to describe and implement them — matrices, trigonometry, dot products — miss the deeper structure.

This book's three projects aren't just three separate experiments. They're **building blocks** for a single vision: a complete language modeling stack built on Geometric Algebra — from the optimizer that trains it, to the generative dynamics that drive it, to the architecture that runs it.

### The Foundation

| Stage | Project | Status | What it does |
|-------|---------|--------|--------------|
| 1 | **gamuon** | Early prototype | Grade-aware optimizer. The training signal itself should respect geometry — rotors for rotations, separate control over scaling and strain. A drop-in upgrade for any PyTorch model. |
| 2 | **gaflowlm** | Proven on Sudoku (70.70%) | Rotor-based flow matching. Replaces trigonometric sphere operations with a unified algebraic framework — cleaner gradients, preserved bivector information, better separability. |
| 3 | **gattrlm** | Clifford layers prototyped | GA-native architecture. Deep Equilibrium models with built-in rotors, geometric products, and blade selection. Constant memory regardless of reasoning depth. |

These three pieces connect through a **consistent geometric vocabulary** — the same rotors, the same Clifford engine, the same multivector layout. The book you're reading defines this vocabulary and serves as the manifesto tying everything together.

### The Spine

**Grade-Wise Scheduling** — the insight that different grades of a multivector need different learning rates — runs through all three projects. It was prototyped in gaflowlm's GWS research and is the first principled way to train multivector networks that acknowledges their internal structure. This isn't a trick. It's a new capability: the ability to say "learn rotations faster than scales" and have that mean something mathematically precise.

### How the Pieces Connect

The three projects and Clifford Frame Attention are not independent experiments — they form a potential stack:

- **gamuon** provides the optimizer that respects geometric structure during training.
- **gaflowlm** supplies rotor-based generative dynamics that preserve bivector information.
- **gattrlm** offers a constant-memory reasoning backbone with built-in Clifford layers.
- **CliffordFrameAttention** can serve as the attention mechanism that ties them together, replacing dot-product attention with geometric product operations across both flow and attractor models.

The shared vocabulary (rotors, multivectors, grade-wise operations) means components developed in one project can be reused in the others with minimal friction. The long-term vision is to train a model with gamuon, generate with rotor-based flow matching, and reason with a Clifford attractor — all speaking the same geometric language.

### The Road Ahead

**Stage 4 — GA-Native Attention** (near-term)
Replace dot-product attention with geometric product attention. The query-key comparison becomes a geometric operation — not just a scalar similarity score but a full interaction that preserves which planes words rotate in and what transformations are implied.

**Head start:** A working implementation already exists — `CliffordFrameAttention` (CFA) in `gaflowlm/models/cfs_arch.py`. It projects Q, K, V from multivectors, scores via grade-weighted geometric product (`Q·reverse(K)` using engine reverse_signs), and produces bilinear output via `engine.geometric_product(Q, V_agg)`. The gap is integration: CFA currently lives inside the CFS flow-matching pipeline (MSE loss, Cl(4) space, tiny-vocabulary ceiling). The next step is extracting it into the attractor backbone (gattrlm) and the flow backbone (gaflowlm RHF), paired with proper CE training.

**Stage 5 — Full GA Language Model** (medium-term)
Combine all three: train with gamuon, generate with gaflowlm, reason with gattrlm. A 1B+ parameter GA-native language model trained from scratch, evaluated on reasoning benchmarks (GSM8K, MATH, ARC-AGI), and compared head-to-head against equivalent standard architectures.

**Stage 6 — Multimodal Grounding** (long-term)
Conformal Geometric Algebra Cl(4,1) — already implemented in gattrlm — can represent 3D points, spheres, planes, and rotations as first-class citizens. Connect the GA language model to vision, robotics, and 3D scenes. A model that *understands* physical space because it speaks the language of space natively.

**Stage 7 — Inference Pipeline** (long-term)
GA-specific quantization, speculative decoding, and KV-cache compression. If the model is built on rotors and multivectors, the inference pipeline should exploit their structure.

### Limitations and Open Questions

A honest assessment of where this approach falls short:

**Computational cost.** Full multivector operations in Cl(k) grow as 2^k. For k=8, that's 256-dimensional operations — manageable. For k=16, it's 65,536. Scaling GA-native models to GPT-scale hidden dimensions requires projection layers (embed → Cl(8) → embed), which lose information at the bottleneck. Whether the geometric benefits outweigh the compression cost is an open question.

**Small field, limited baselines.** Fewer than a thousand researchers worldwide work on GA for ML. There are no established best practices for multivector architecture design, no standard benchmarks, and no production-scale GA training runs. Every result so far — including ours — comes from small models on toy tasks.

**The Sudoku ceiling is not yet broken on real language.** Our 70.70% improvement came on a 12-token Sudoku vocabulary. The real test — scaling to 50K-token vocabularies on open-domain text — hasn't been attempted. The multivector hypothesis may prove true for small, structured domains and false for the messy entropy of natural language.

**Equivariance is proven for 3D, not for language.** GATr and GCANs have mathematically proven equivariance to E(3) rotations — but language doesn't have an obvious symmetry group. What does "rotate a sentence" even mean? GA for language may need different mathematical guarantees than GA for physics.

**Hardware is not on our side.** GPUs are optimized for matrix multiply, not for geometric products. A single geometric product via einsum is ~2-10x more expensive than an equivalent matrix operation. Without custom CUDA kernels for GA operations, wall-clock speed will lag behind standard architectures regardless of theoretical advantages.

These aren't reasons to stop. They're reasons to be precise about what we claim and rigorous about how we measure.

### What Success Looks Like

This isn't just a research program. It's a claim:

> *Linear algebra has been good to us. But it's not the right language for describing transformation, composition, and meaning. Geometric Algebra is.*

The three repos are the working prototypes for that worldview. This book is the explanation. The roadmap is the plan.

What we learn on the way — about neural networks, about geometry, about language — might matter more than any single result. The 70.70% on Sudoku is one data point. The real signal is this: every time we've had access to richer geometric structure, we've found something we couldn't see before.

History suggests that when you align your mathematics with the structure of your problem, progress accelerates. We used complex numbers instead of awkward trig for waves. We used matrices instead of scalar formulas for linear systems. We used tensors for general relativity.

Geometric Algebra for language modeling might be the next step in that progression — not because it's more mathematically sophisticated, but because it's a better match for what language models are actually doing.

---

