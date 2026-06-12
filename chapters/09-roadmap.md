## 9. The Roadmap

Geometric Algebra isn't the only mathematical frontier in AI, but it's a particularly promising one because of a fundamental observation:

**Neural networks are already doing geometry. They're just using the wrong vocabulary.**

The word embeddings, rotations, transformations, and comparisons that language models perform daily are inherently geometric operations. But the tools we use to describe and implement them — matrices, trigonometry, dot products — miss the deeper structure.

This book's projects aren't just separate experiments. They're **probes** into a single question: does GA provide advantage at any layer of the language modeling stack? The answer so far is **partial and conditional**:

- **gaflowlm**: Rotor primitives are mathematically correct. The CFS track is promising. But no language modeling win yet.
- **gattrlm**: Clifford attention provides free equivariance. But text quality is neutral or slightly worse.
- **gamuon**: Theoretical foundation is solid. But no training benchmarks exist.
- **gatoken**: Early implementation. No production comparisons yet.
- **bbt GA diffusion**: The only project with a real, published metric (PPL 1.723 at 1B tokens). But the model is tiny and the task is small.

---

### The Foundation

| Stage | Project | Status | What it does | What we know |
|-------|---------|--------|--------------|-------------|
| 1 | **gamuon** | Prototype implemented | Grade-aware optimizer. The training signal should respect geometry — rotors for rotations, separate control over scaling and strain. | Code exists. No training runs yet. |
| 2 | **gaflowlm** | RHF validated; CFS active | Rotor-based flow matching. Replaces trigonometric sphere operations with a unified algebraic framework. | RHF is numerically identical to SLERP. CFS has clean flow loss but not competitive LM quality. |
| 3 | **gattrlm** | Prototyped | GA-native architecture. DEQ models with built-in rotors, geometric products, and blade selection. Constant memory regardless of reasoning depth. | Equivariance is proven on synthetic tasks. Text quality is neutral or slightly worse. |
| 4 | **gatoken** | Early implementation | Geometric tokenization. Rotor-guided merging reduces language bias. | Cl(3,0) engine is correct. No benchmark comparisons yet. |
| 5 | **bbt GA diffusion** | Proven at small scale | Byte-level GA diffusion. 16L dim16 model reaches PPL 1.723 on TinyStories at 1B tokens. | **The only real metric in this book.** Small scale, simple task. |

These projects share a **consistent geometric vocabulary** — the same rotors, the same Clifford engine, the same multivector layout. But they are not yet an integrated stack. They are independent experiments.

![The integrated GA stack](../visualizations/media/images/ch9_roadmap/Scene1_IntegratedStack.png)

---

### The Honest Assessment

This is the section that every research book needs but few include. What have we **not** proven?

**gaflowlm has not proven that GA improves language modeling.** The RHF rotor ops are a correct rewrite of SLERP, not a better version. The CFS track has clean flow loss but `logit_ppl` ≈ 886 — far behind standard AR. The real test — scaling to real text with competitive quality — hasn't happened.

**gattrlm has not proven that Clifford attention wins on text.** The 0.022 val loss difference on wikitext-103 is within noise. The Clifford MLP adds 4× compute for zero quality gain. The equivariance win is real but niche — it applies to geometric tasks, not language.

**gamuon has not proven that GA optimization beats standard methods.** The grade decomposition, rotor exponential, and versor sandwich are all implemented. But no training runs have been performed. It is a prototype, not a validated optimizer.

**gatoken has not proven that geometric tokenization reduces bias.** The Cl(3,0) engine is correct. The merge logic runs. But the 49-sentence test set is tiny. No comparison against sentencepiece, tiktoken, or other production tokenizers exists.

**bbt GA diffusion has proven that GA can train at the byte level, but not that it scales.** PPL 1.723 at 1B tokens is real. But the model is 16L dim16 — tiny. The task is TinyStories — relatively easy. The gap to frontier models is enormous.

**The broader problems:**

- **Computational cost.** Full multivector operations in Cl(k) grow as 2^k. For k=8, that's 256-dimensional operations — manageable. For k=16, it's 65,536. Scaling GA-native models to GPT-scale hidden dimensions requires projection layers, which lose information at the bottleneck.
- **Small field, limited baselines.** Fewer than a thousand researchers worldwide work on GA for ML. There are no established best practices for multivector architecture design, no standard benchmarks, and no production-scale GA training runs.
- **Equivariance is proven for 3D, not for language.** GATr and GCANs have mathematically proven equivariance to E(3) rotations. But language doesn't have an obvious symmetry group. What does "rotate a sentence" even mean?
- **Hardware is not on our side.** GPUs are optimized for matrix multiply, not for geometric products. A single geometric product via einsum is ~2-10× more expensive than an equivalent matrix operation. Without custom CUDA kernels, wall-clock speed will lag.

These aren't reasons to stop. They're reasons to be precise about what we claim and rigorous about how we measure.

![Open questions to answer](../visualizations/media/images/ch9_roadmap/Scene3_HonestAssessment.png)

---

### The Road Ahead

The roadmap is now **conditional**. Each step depends on the previous step showing real results.

**Immediate (next 3 months):**

- **bbt GA diffusion**: Scale to 5B tokens. Evaluate on a held-out test set with proper bootstrap confidence intervals. Compare against a standard AR baseline at the same model size.
- **gatoken**: Benchmark against sentencepiece on a SEA-language corpus. Measure fertility, tokens/char, and downstream model performance.
- **gaflowlm**: CFS with proper cross-entropy training. The current flow objective is not a standard LM metric. Train a CFS model to minimize actual token perplexity.

**Medium-term (6-12 months):**
- **gattrlm**: Find a task where Clifford attention improves text quality. If it can't win on wikitext, test on a geometrically structured task (e.g., synthetic reasoning with spatial relations, code with structural patterns).
- **gamuon**: Benchmark against Adam and Muon on a standard LM training run. If GA optimization doesn't improve convergence or final loss, the theoretical elegance is not enough.
- **bbt**: Compare Mamba vs Transformer at matched compute on the same dataset. The goal is a decision memo: where Mamba is better, where it is not, and the default backbone recommendation.

**Long-term (1-2 years):**
- **Integration**: If any individual project shows a clear, reproducible win, build the stack. A GA-native model requires: tokenizer (gatoken), architecture (gattrlm), training (gamuon), generation (gaflowlm or bbt diffusion).
- **If none win**: Document the negative results. Publish what GA can't do and why. The field needs honest null results as much as it needs successes.

---

### What Success Looks Like

This isn't just a research program. It's a claim:

> *Linear algebra has been good to us. But it's not the right language for describing transformation, composition, and meaning. Geometric Algebra is.*

The five repos are the working prototypes for that worldview. This book is the explanation. The roadmap is the plan.

But the claim is **conditional**. It stands or falls based on what the next 12 months of experiments show. If bbt GA diffusion scales to competitive quality, if gattrlm finds a text task where Clifford attention wins, if gamuon beats Adam on a real training run — then the stack is worth building. If not, then GA is a powerful niche tool for geometric domains, not a general language modeling framework.

Both outcomes are valuable. The real failure is not a negative result. The real failure is a false positive — a claim that GA works for language because of a cherry-picked metric on a toy task, when the truth is more nuanced.

The 70.70% Sudoku figure referenced in earlier drafts of this chapter was removed after review. The original claim — that bivector regularization broke a performance ceiling on a structured reasoning task — could not be verified in the project repository. No log, checkpoint, or script produces that number. The metric has been removed from the book. This is the standard the rest of the work should be held to.

What we learn on the way — about neural networks, about geometry, about language — might matter more than any single result. The real signal is the pattern: every time we've had access to richer geometric structure, we've found something we couldn't see before. But the next step is proving that this pattern scales.

---
