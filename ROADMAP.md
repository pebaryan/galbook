# Geometric Algebra for Language: A Research Roadmap

## The Vision

**Stop treating neural networks as bags of matrices. Start treating them as geometric objects in a proper algebra.**

This is the north star: a complete language modeling stack built on Geometric Algebra — from the tokenizer that processes text, to the optimizer that trains weights, to the architecture that runs inference, to the generation mechanism that produces output. Every piece speaks the same mathematical language. Rotors for rotations. Bivectors for relationships. Multivectors for meaning.

But the vision is **conditional**. It stands or falls based on whether GA provides measurable advantage at each layer of the stack.

---

## Foundation: What We've Built

### Stage 1 — The Optimizer (gamuon)

*Status: **Negative result***

> *The training signal itself should respect geometry.*

Muon reformulated in GA. Grade-aware updates that treat rotations, scales, and strains differently — because they *are* different. A drop-in optimizer for PyTorch models.

**What we know:**
- [x] Core GA reformulation of matrix sign function
- [x] Grade decomposition (scalar, bivector, strain)
- [x] Rotor exponential with closed-form 2×2/3×3 and `torch.matrix_exp` fallback
- [x] **Benchmarked on wikitext-2 and bbt 16L dim16**
- [x] **6× slower than Adam with worse convergence**
- [ ] Faster rotor approximation (e.g., Newton-Schulz, truncated Taylor)
- [ ] Integration with gaflowlm and gattrlm training loops

**Conclusion:** The `torch.matrix_exp` bottleneck on the rotor exponential dominates the step cost. The grade-aware updates do not compensate for the compute cost. Gamuon is not competitive with AdamW for standard LM training. Unless a faster rotor approximation is found, the project is a negative result.

---

### Stage 2 — The Generative Backbone (gaflowlm)

*Status: RHF validated; CFS active research*

> *Meaning flows through rotation. Give it the right language.*

Flow matching on the hypersphere, but with rotors instead of trigonometry. The rotor sandwich preserves the bivector — the rotation plane — that SLERP throws away.

**What we know:**
- [x] Rotor replacement for SLERP (numerically identical — proves correctness)
- [x] CFS architecture with Clifford Frame Attention
- [ ] Scale to real language with competitive perplexity
- [ ] Integrate CFA with proper cross-entropy training (not just flow loss)
- [ ] Compare against standard AR baselines at matched scale

**Honest assessment:** The RHF rotor ops are a correct rewrite, not a better version. The CFS track has clean flow loss on wikitext-2 but `logit_ppl` ≈ 886 — far behind standard AR. The real test hasn't happened yet.

---

### Stage 3 — The Architecture (gattrlm)

*Status: Prototype; equivariance proven, text quality neutral*

> *Deep reasoning shouldn't cost more memory.*

Deep Equilibrium (DEQ) models iterate a single block to a fixed point — constant memory regardless of effective depth. Add Clifford algebra layers, and you get built-in rotation equivariance.

**What we know:**
- [x] Cl(3,0) Euclidean algebra implementation
- [x] Cl(4,1) Conformal Geometric Algebra for 3D reasoning
- [x] RotorLayer, CliffordLinear, GeometricProductLayer prototypes
- [x] Equivariance proven on synthetic rotor tasks (4×–48× better extrapolation)
- [ ] Train CliffordAttractor at scale with competitive text quality
- [ ] Benchmarks on reasoning tasks (GSM8K, ARC-AGI) vs standard DEQ

**Honest assessment:** Clifford attention is neutral or slightly worse on wikitext-103 (6.0156 vs 6.0376 — within noise). The Clifford MLP adds 4× compute for zero quality gain. The equivariance win is real but niche. The challenge is finding a text task where it actually helps.

---

### Stage 4 — Tokenization (gatoken)

*Status: Early implementation*

> *If words are multivectors, tokens should be too.*

Rotor-guided tokenization. Instead of frequency-based BPE merging, use geometric coherence between adjacent characters as the merge criterion.

**What we know:**
- [x] Cl(3,0) geometric product engine (corrected 15 sign errors from initial version)
- [x] RotorSubwordTokenizer with geometric merge scoring
- [x] TokenMultivectorTokenizer with learnable multivector representations
- [ ] Benchmark against sentencepiece on SEA-language corpus
- [ ] Measure fertility, tokens/char, and downstream model performance

**Honest assessment:** The tokenizer runs on a 49-sentence test set. No production comparison exists. Whether geometric merging reduces cross-language bias is still to be tested.

---

### Stage 5 — Byte-Level Diffusion (bbt)

*Status: Proven at small scale — PPL 1.723 at 1B tokens*

> *The byte level is the ultimate stress test.*

A single-GPU training stack for byte-level language models. The GA diffusion track trains a 16L dim16 model with a geometric diffusion objective on raw bytes.

**What we know:**
- [x] 16L dim16 model reaches PPL 1.723, BPB 0.5441 on TinyStories at 1B tokens
- [x] Bootstrap confidence interval: PPL 1.721–1.726
- [ ] Scale to 5B tokens
- [ ] Evaluate on held-out test set with proper comparison to AR baseline
- [ ] Scale model size and task difficulty

**Honest assessment:** This is the strongest real metric in the entire stack. But the model is tiny (16L dim16), the task is simple (TinyStories), and the scale is small (1B tokens). The critical question is whether this result scales.

---

## The Honest Assessment

This is the section that every research roadmap needs.

**What we have NOT proven:**

1. **gaflowlm** has not proven that GA improves language modeling. The rotor primitives are correct. The CFS track is interesting. But no competitive LM quality result exists.

2. **gattrlm** has not proven that Clifford attention improves text quality. The equivariance win is real for geometric tasks, but language is not obviously a geometric task.

3. **gamuon** has not proven that GA optimization beats standard methods. Benchmarks on wikitext-2 and bbt 16L dim16 show that Gamuon is **6× slower than Adam** with **worse convergence**. The `torch.matrix_exp` bottleneck on the rotor exponential dominates the step cost.

4. **gatoken** has not proven that geometric merging reduces bias. The implementation is early. The benchmarks are tiny.

5. **bbt** has not proven that GA scales. The 1.723 PPL is real but at small scale.

**The broader challenges:**

- **Computational cost.** Full multivector operations in Cl(k) grow as 2^k. For k=8, that's 256-dimensional operations. For k=16, it's 65,536. Scaling to GPT-scale hidden dimensions requires projection layers, which lose information.
- **Hardware mismatch.** GPUs are optimized for matrix multiply, not geometric products. A single geometric product via einsum is ~2-10× more expensive than equivalent matrix operations.
- **Small field.** Fewer than a thousand researchers work on GA for ML. No established best practices, no standard benchmarks, no production-scale training runs.
- **Equivariance is proven for 3D, not for language.** What does "rotate a sentence" mean?

These aren't reasons to stop. They're reasons to be precise about what we claim and rigorous about how we measure.

---

## The Road Ahead

The roadmap is now **conditional**. Each step depends on the previous step showing real, reproducible results.

### Immediate (next 3 months)

- **bbt GA diffusion**: Scale to 5B tokens. Compare against standard AR at same model size.
- **gatoken**: Benchmark against sentencepiece on SEA-language corpus.
- **gaflowlm**: CFS with proper cross-entropy training. The flow objective is not a standard LM metric.

### Medium-term (6-12 months)

- **gattrlm**: Find a task where Clifford attention improves text quality. If not on wikitext, test on geometrically structured tasks.
- **gamuon**: Investigate faster rotor approximations (e.g., Newton-Schulz, truncated Taylor series) or accept the negative result and document it. The benchmark is done.
- **bbt**: Mamba vs Transformer comparison at matched compute.

### Long-term (1-2 years)

- **Integration**: If any individual project shows a clear win, build the stack.
- **If none win**: Document the negative results. Publish what GA can't do and why.

The real failure is not a negative result. The real failure is a false positive.

---

## The Bigger Picture

This isn't just a research program. It's a claim:

**Linear algebra has been good to us. But it's not the right language for describing transformation, composition, and meaning. Geometric Algebra is.**

The five repos are the working prototypes. The book is the explanation. This roadmap is the plan.

But the claim is conditional. It stands or falls based on what the next 12 months of experiments show.

---

*June 2026 — Peb Aryan*
