# External Review of Pebaryan's GA Research Program

*A thoughtful review of the GA-for-language repos (gaflowlm, gattrlm, gamuon, gatoken, bbt) by an external reader.*

---

## Overall Direction

Core idea: Neural networks (especially transformers and generative models) deal with rotations, orientations, symmetries, and structured representations. Geometric Algebra (GA/Clifford algebra) provides the right mathematical language for this — rotors for exact rotations, multivectors for richer embeddings, grade decomposition for separating different kinds of operations (scaling, rotating, straining).

Strategy: Take promising recent ideas (Muon optimizer, hyperspherical flow models, attractor/DEQ models, byte-level diffusion) and reformulate them in GA for exactness, stability, equivariance, and potential performance gains.

Long-term goal: Create components (optimizer + generative backbone + memory-efficient architecture + tokenizer) that can be combined into a full GA-native LLM pipeline. But the goal is conditional — each component must show measurable advantage before integration.

---

## How the Repos Fit Together

| Repo | Role | What it contributes | Status |
|------|------|---------------------|--------|
| **gamuon** | Training foundation | Exact, grade-aware optimizer. Drop-in upgrade for any PyTorch model. | **Negative result**: 6× slower than Adam with worse convergence on wikitext-2 and bbt 16L dim16 |
| **gaflowlm** | Generative / flow-based modeling | Replaces trig-based spherical flows with rotor sandwiches and Clifford attention. | RHF validated; CFS + CE tested at multiple scales with diagnostic. Auxiliary CE achieves logit_ppl ≈ 1723 on wikitext-2, but standard AR baseline at same scale reaches PPL 248 (7× better). Diagnostic isolates multivector embedding as primary bottleneck (2.7× penalty vs standard embedding); Clifford attention adds another ∼2.6×. Next: test whether improving multivector embedding or replacing Clifford attention can close the gap. |
| **gattrlm** | Efficient deep reasoning | Attractor models (DEQ) with GA layers. Constant memory, built-in equivariance. | Prototype; equivariance proven, text neutral |
| **gatoken** | Tokenization | Rotor-guided subword tokenization. Reduces language bias. | **Positive results under review** — FLORES-101 benchmark across 12 languages shows improved parity. Exact numbers withheld pending peer review. |
| **bbt** | Byte-level efficiency | Single-GPU stack. GA diffusion track reaches PPL 1.723 at 1B tokens. | Proven at small scale |

Connections:
- Use gamuon to train models from the other repos more effectively (if it proves better than Adam/Muon)
- Apply grade-wise scheduling across the stack
- Leverage rotors and multivectors consistently for embeddings, attention, normalization, and updates

---

## Identified Gaps (Promising Next Directions)

1. **Full-scale Transformer Backbones & Pretraining** — No large-scale causal decoder-only transformer with GA layers throughout pretraining on massive web data. Scaling multivector representations or Clifford attention to 7B+ parameters while staying efficient remains a big engineering challenge.

2. **Multimodal & Grounded Language Modeling** — No integration with vision, audio, or robotics. Conformal GA (in gattrlm) is perfect for 3D geometry, but not yet connected to VLMs or agentic workflows.

3. **Retrieval, Long-Context, and Memory Mechanisms** — No GA-enhanced RAG, state space models, or infinite-context techniques. GA could shine in structured key-value memories or rotor-based compression/rotation of context.

4. **Inference-Time Techniques & Alignment** — Quantization, distillation, or speculative decoding for multivectors/rotors. RLHF with geometric losses. Test-time scaling that leverages GA equivariance.

5. **Theoretical & Interpretability Work** — Formal proofs of advantages. Probing grade-specific semantics (bivectors for relations, higher grades for hierarchy). Connections to formal semantics or neurosymbolic AI.

6. **Hybrid/Alternative GA Signatures** — Beyond Cl(3,0)/Cl(4,1): projective GA, spacetime algebras, custom signatures for language. Efficiency optimizations for sparse multivectors or hardware-aware GPU kernels.

7. **Frontier Reasoning & Scientific Tasks** — No results on advanced math, code, physics simulation, or agentic benchmarks. The strongest published metric is bbt GA diffusion at PPL 1.723 on TinyStories (small scale). gatoken has positive results under review on FLORES-101 parity.

---

## Reviewer's Closing Take

> *"This is passionate, high-signal independent research. It's early-stage (small repos, research-focused), but cohesive and forward-looking. If successful, these could influence 'geometric deep learning' beyond niche use — especially for efficient reasoning models, scientific AI, or anything needing strong inductive biases for structure and symmetry."*
>
> *"He's essentially asking: 'What if we stopped treating neural nets as bags of matrices and started treating them as geometric objects in a proper algebra?' The repos are his working prototypes for that worldview."*
>
> *"The honest framing is important: most of these are prototypes or negative results, not proven wins. The strongest published metric is bbt byte-level diffusion (PPL 1.723). gatoken has positive results under review on FLORES-101 parity. gaflowlm CFS + CE achieves logit_ppl ≈ 1723 on wikitext-2, but a standard AR baseline at the same scale reaches PPL 248 — 7× better. A diagnostic isolates the multivector embedding as the primary bottleneck (2.7× penalty vs standard embedding); Clifford attention adds another ∼2.6×. gamuon is a negative result — the rotor exponential is too expensive for standard LM training. The rest is theoretical elegance waiting for empirical validation."*

---

*Received May 2026. Revised June 2026 after galbook audit removed unverifiable metrics, added honest status assessment, documented gamuon negative result, added CFS + CE downstream evaluation with AR baseline comparison, and ran diagnostic isolating multivector embedding bottleneck.*
