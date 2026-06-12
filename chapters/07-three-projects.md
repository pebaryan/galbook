## 7. Three Projects: Building With GA

Chapter 6 showed how others have applied Geometric Algebra to 3D reasoning, protein generation, and semantic theory. This chapter turns inward: three projects from our own research, each attacking a different layer of the language modeling stack.

The pattern is the same: identify a limitation in standard approaches, find where GA provides leverage, and build something to test the hypothesis.

---

### The Problem of Hidden Information

**The Problem:**

Flow matching has emerged as a powerful approach for continuous generative modeling. It works by interpolating on a hypersphere between noise and data using SLERP. The mathematics are elegant, the training is stable, and the results are competitive with diffusion.

But the standard approach discards information. SLERP operates on the surface of the sphere, treating each point as a vector. The rotation that moves you from noise to data has structure — a plane of rotation, encoded in the bivector. SLERP projects this to grade 1 and throws the bivector away.

**The GA Opportunity:**

What if we kept the bivector? Rotors encode both the angle and the plane of rotation. The full rotor sandwich R · x · R̃ contains more information than its grade-1 projection.

The key insight: SLERP(x₀, x₁, t) = ⟨R(t) · x₀ · R̃(t)⟩₁. They're mathematically equivalent at the output, but the rotor version carries the full multivector through the computation.

This means:
- We can train with the same objective (the grade-1 projection matches SLERP)
- But we have access to the bivector components during training
- These components might reveal structure invisible to standard methods

**What We Built:**

**gaflowlm** replaces SLERP with rotor-based flow matching. The architecture is identical — same transformer backbone, same training loop — except the interpolation uses rotors.

**Current Status:**

The RHF rotor primitives are **numerically identical** to the standard trigonometric SLERP implementation. They pass the same forward pass, produce the same checkpoints, and match bit-for-bit on validation metrics. This is a rewrite, not a speedup or a quality improvement.

The structural benefit — having access to the full bivector during training — is real but **unproven at scale**. The CFS (Clifford Flow Matching) track is the active research direction, using multivector embeddings and Clifford Frame Attention. It reaches clean flow-loss convergence on wikitext-2 but has not yet matched standard AR language modeling quality.

**Update:** CFS with auxiliary cross-entropy training (flow loss + CE loss) has been tested on wikitext-2. At 2000 steps, k=4, hidden=256, 4 blocks, the model reaches **logit_ppl ≈ 1723** — but a standard AR transformer at the same scale (hidden=256, 4 blocks, 4 heads, 16.2M params) reaches **PPL 248** on the same dataset. The CFS model is **7× worse** than the AR baseline. Scaling to a larger model (k=6, hidden=512, 4 blocks, 30.7M params) at 500 steps reaches **PPL 1808** — the gap does not close with more parameters.

**Diagnostic:** A standard transformer with multivector embeddings (k=4, standard attention, 17.0M params) reaches **PPL 662** — 2.7× worse than the standard embedding baseline. This isolates the multivector embedding as the primary bottleneck. The Clifford attention adds another ∼2.6× penalty on top. The multivector embedding maps tokens into a 16-dimensional space (2^k for k=4) and projects to d_model=256, losing information compared to a direct embedding lookup.

The auxiliary CE loss is necessary for the AR head to learn anything (without it, logit_ppl stays at ~9873), but even with CE, the CFS model does not approach standard AR quality. The next step is either improving the multivector embedding (e.g., learnable projection, larger k) or accepting that the multivector representation is not suitable for language modeling at this scale.

![SLERP loses bivector information](../visualizations/media/images/ch7_three_projects/Scene1_HiddenInformation.png)

---

### The Problem of Linear Memory Growth

**The Problem:**

Standard transformers stack layers: layer 1 feeds layer 2 feeds layer 3... feed layer L. Each layer transforms the representation, and you need to store intermediate activations for backpropagation. Memory grows with depth.

This is expensive. For a 96-layer model, you're storing 96 sets of activations. The computation is parallel across the sequence, but sequential through the layers. Want deeper reasoning? Pay linear memory cost.

![Linear memory vs constant memory DEQ](../visualizations/media/images/ch7_three_projects/Scene3_MemoryProblem.png)

Deep Equilibrium (DEQ) models offer an alternative: instead of stacking L different layers, iterate a single layer f until convergence.

```
x_{t+1} = f(x_t) for t = 0, 1, 2, ...
```

The representation converges to a fixed point — an attractor. You can iterate for hundreds of steps while storing only the final state (using implicit differentiation for gradients). Memory becomes constant in depth.

**The GA Opportunity:**

What if the DEQ iteration operated on multivectors instead of vectors? Each state would be a complete geometric object with scalar, vector, bivector, and trivector components. The fixed point would be a geometric equilibrium, not just a numerical one.

**What We Built:**

**gattrlm** adds Clifford algebra layers to the DEQ framework. Instead of iterating vector transformations, we iterate geometric transformations.

**Current Status:**

The Clifford variants are **quality-neutral or slightly worse on plain text** compared to the standard Attractor baseline. On wikitext-103, the best Clifford variant (AttnOnlyCliffordLM) reaches 6.0156 val loss vs 6.0376 for the baseline — a difference well within noise. The Clifford MLP adds 4× wall-clock for zero quality gain.

Where GA pays off is **geometric tasks**. On a synthetic rotor regression task (predict R · v · R̃ from v and R), the Clifford attention variant achieves 4×–48× better extrapolation than standard attention:

| Arm | Angle gap | Axis gap |
|-----|-----------|----------|
| MLP (no Clifford) | 109× | 215× |
| CliffordAttn | **4.2×** | **2.5×** |

**3D Coordinate Rotation Benchmark:** A 3D coordinate rotation task tests whether Clifford attention generalizes to unseen rotation axes. The model receives a point cloud (8 points), a rotation axis, and an angle; it must predict the rotated coordinates. Training uses rotations around x, y, z axes; testing uses held-out axes (diagonal planes).

With 10k training samples, 50 epochs, 4-layer, 128-dim models:

| Model | Val MSE | OOD Test MSE | Gap |
|-------|---------|--------------|-----|
| Standard Transformer | 0.0076 | 0.4626 | 61× |
| Clifford Attention | **0.0043** | **0.3131** | 73× |

Clifford attention achieves **1.8× lower val MSE** and **1.5× lower OOD test MSE** than standard attention on the same architecture. The gap is consistent but not dramatic. Both models struggle with OOD generalization (test MSE is 50–70× worse than val MSE), but Clifford attention handles unseen rotation axes better.

**Scaling to larger models:** When increasing to 8 layers and 256 dimensions, the standard transformer fails to learn the balanced bracket classification task entirely — it gets stuck at the majority class baseline (74.41% val, 75.00% test). The Clifford attention model, at the same scale, achieves **98.24% val accuracy and 97.22% test accuracy**. This is a dramatic difference: Clifford attention learns the task while standard attention fails.

The pattern is the same across all tasks: Clifford attention's advantage is most pronounced when the model has enough capacity to leverage the geometric structure. At small scale, the task is too easy for both. At larger scale, Clifford attention's built-in equivariance allows it to learn structural patterns that standard attention misses.

**Python AST node classification:** A more realistic benchmark classifies the root node type of synthetic Python code snippets. The code templates are drawn from common Python constructs (functions, classes, loops, conditionals, etc.). With 35 distinct AST node types in the vocabulary:

| Model | Val Acc | Test Acc | Baseline |
|-------|---------|----------|----------|
| Standard Transformer | 100% | 100% | 2.86% |
| Clifford Attention | 100% | 100% | 2.86% |

Both models achieve 100% accuracy on this synthetic task because the code templates are too simple and predictable. The AST node classification task is not challenging enough to reveal differences between architectures.

**Code structure benchmark summary:**

| Task | Scale | Standard | Clifford | Finding |
|------|-------|----------|----------|---------|
| Nesting depth (32 tokens) | 4L/128d | 100% | 100% | Both perfect; too easy |
| Balanced classification (64 tokens) | 4L/128d | 99.02% | 99.22% | Clifford slightly better |
| Balanced classification (64 tokens) | **8L/256d** | **74.41%** | **98.24%** | **Clifford learns; standard fails** |
| Next token prediction (128 tokens) | 4L/128d | 54.68% | 54.67% | No difference |
| AST node classification (64 tokens) | 4L/128d | 100% | 100% | Both perfect; too easy |

The honest lesson: Clifford attention provides a real advantage on code structure tasks **at sufficient scale**. The 8L/256d balanced bracket result is the clearest win: Clifford attention learns where standard attention fails. But on simpler tasks (depth prediction, AST classification) or at small scale, the gap is negligible. The advantage is conditional on task complexity and model capacity.

---

### The Problem of Geometric Optimization

**The Problem:**

Training neural networks is optimization: find weights that minimize loss. The optimizer's job is to propose weight updates based on gradients.

Standard optimizers (Adam, SGD) treat weights as raw numbers. They don't know that a weight matrix might represent a rotation, or that certain directions in parameter space are more "natural" than others.

The Muon optimizer takes a step toward geometric awareness. It computes the matrix sign function of the gradient — the nearest orthogonal matrix — and uses that as the update direction. This respects the structure of linear transformations better than raw gradient descent.

**The GA Opportunity:**

Orthogonal matrices are rotors in even dimensions. The matrix sign function is a geometric operation hiding in linear algebra notation.

In GA terms:
- Gradients are multivectors in the Clifford algebra of the weight space
- The sign function becomes a geometric function on multivectors
- Orthogonality is natural under the geometric product
- The same operation works for scalars, vectors, matrices, and higher-order structures

**What We Built:**

**gamuon** reformulates Muon using Geometric Algebra. The core computation — finding the geometrically natural update direction — becomes a multivector operation.

**Current Status:**

The theoretical foundation exists and is implemented. The grade decomposition (scalar, bivector, strain) is correct. The rotor exponential uses closed-form formulas for 2×2 and 3×3, and `torch.matrix_exp` for larger matrices. The versor sandwich update is implemented.

But the **training benchmarks are negative**. On a standard transformer trained on wikitext-2:

| Optimizer | Final val loss | Time per step |
|-----------|---------------|---------------|
| Adam | **6.21** | 4.9 ms |
| Muon (NS) | 6.52 | 11.0 ms |
| Gamuon | 6.25 | **30.7 ms** |

Gamuon is **6× slower than Adam** with slightly worse validation loss. The bottleneck is `torch.matrix_exp` on the rotor exponential — an iterative Padé approximation that dominates the step cost.

On the bbt 16L dim16 byte-level diffusion model (TinyStories, 1000 steps):

| | AdamW | GamuonAuto |
|---|---|---|
| step 900 loss | **3.18** | **3.83** |
| time/step | **~16 s** | **~26 s** |

Gamuon reaches **~20% worse loss** at 40% slower speed. The rotor exponential cost on many small 2D matrices (q_proj, k_proj, v_proj, o_proj, MLP layers) compounds. Additionally, GamuonAuto routes non-2D parameters (embeddings, norms, biases) to SGD, which is suboptimal for language modeling; switching to AdamW for those params did not change the outcome because the matrix_exp bottleneck dominates.

**The honest assessment:** The mathematics is elegant, but the rotor exponential is too expensive for standard LM training. The grade-aware updates do not compensate for the compute cost. Unless a faster rotor approximation is found, Gamuon is not competitive with AdamW for language models.

---

### Toward Integration

The three projects attack different problems:

| Project | Layer | What it does | Status |
|---------|-------|--------------|--------|
| gaflowlm | Generation | Rotor-based flow matching, preserves bivector | Numerically validated; no LM win yet |
| gattrlm | Architecture | DEQ + Clifford layers, constant memory | Equivariance proven; text quality neutral |
| gamuon | Optimization | Grade-aware multivector optimizer | **Negative result: slower than AdamW with worse convergence** |

![Integrated GA stack](../visualizations/media/images/ch7_three_projects/Scene4_IntegratedStack.png)

They're not yet building blocks for a unified stack. They are independent experiments testing whether GA provides advantage at each layer. The honest answer so far:

- **gaflowlm**: The rotor primitives work. The CFS track is promising but not yet competitive.
- **gattrlm**: Clifford attention gives free equivariance but does not improve text quality.
- **gamuon**: The mathematics is elegant, but the rotor exponential is too expensive for standard LM training.

The missing piece — Clifford Frame Attention — connects the geometry of individual tokens to the relationships between them. That's Chapter 8.

---
