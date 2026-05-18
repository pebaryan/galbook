# Geometric Algebra for Language: A Research Roadmap

## The Vision

**Stop treating neural networks as bags of matrices. Start treating them as geometric objects in a proper algebra.**

This is the north star: a complete language modeling stack built on Geometric Algebra — from the optimizer that trains it, to the generative dynamics that drive it, to the architecture that runs it. Every piece speaks the same mathematical language. Rotors for rotations. Bivectors for relationships. Multivectors for meaning.

---

## Foundation: What We've Built

### Stage 1 — The Optimizer (gamuon)

*Status: Early prototype*

> *The training signal itself should respect geometry.*

Muon reformulated in GA. Grade-aware updates that treat rotations, scales, and strains differently — because they *are* different. A drop-in optimizer that makes any PyTorch model train more stably, especially when geometric structure matters.

**Milestones:**
- [x] Core GA reformulation of matrix sign function
- [ ] Verification on standard LM benchmarks (perplexity match or beat Adam/Muon)
- [ ] Integration with GaFlowLM and GAttrLM training loops
- [ ] Scaling experiments (does GA-Muon help at 1B+ parameters?)

---

### Stage 2 — The Generative Backbone (gaflowlm)

*Status: Proven on toy tasks*

> *Meaning flows through rotation. Give it the right language.*

Flow matching on the hypersphere, but with rotors instead of trigonometry. The rotor sandwich preserves the bivector — the rotation plane — that SLERP throws away. This extra information let us break a performance ceiling (62.90% → 70.70% on Sudoku).

**Milestones:**
- [x] Rotor replacement for SLERP (numerically identical — proves correctness)
- [x] Embedding contrastive via bivector information (70.70% — proves utility)
- [ ] Scale from Sudoku to real language (OpenWebText, TinyGSM)
- [ ] Integrate Clifford Frame Attention for full multivector processing
- [ ] Compare against standard S-FLM baselines at 100M+ param scale

---

### Stage 3 — The Architecture (gattrlm)

*Status: Fork with Clifford extension layers*

> *Deep reasoning shouldn't cost more memory.*

Deep Equilibrium (DEQ) models iterate a single block to a fixed point — constant memory regardless of effective depth. Add Clifford algebra layers (RotorLayer, GeometricProductLayer, BladeSelector), and you get built-in rotation equivariance without data augmentation.

**Milestones:**
- [x] Cl(3,0) Euclidean algebra implementation
- [x] Cl(4,1) Conformal Geometric Algebra for 3D reasoning
- [x] RotorLayer, CliffordLinear, GeometricProductLayer prototypes
- [ ] Train CliffordAttractor at scale (1B+ tokens)
- [ ] Benchmarks: Sudoku, ARC-AGI, GSM8K vs standard DEQ

---

## The Spine: What Connects Them

### Grade-Wise Scheduling

The insight that different grades of a multivector (scalar, vector, bivector, ...) need different learning rates. Already prototyped in gaflowlm's GWS research. This isn't just a trick — it's the first principled way to train multivector networks that acknowledges their internal structure.

### Consistent Geometric Vocabulary

All three repos should speak the same language. Same rotor convention. Same CliffordEngine primitives. Same multivector layout. The book *(The Geometry of Meaning)* defines this vocabulary for a general audience and serves as the manifesto tying everything together.

---

## The Road Ahead

### Stage 4 — GA-Native Attention (Near-term)

Replace dot-product attention with geometric product attention. Not just in the DEQ block (gattrlm) but as a general mechanism. Query-key comparison becomes a geometric operation, not just a scalar similarity score.

**Why it matters:** Dot products collapse everything to a single number. Geometric products preserve the full interaction structure — which planes words rotate in, how grades mix, what transformations are implied.

### Stage 5 — Full GA Language Model (Medium-term)

Combine all three:
- **Train** with gamuon (grade-aware optimizer)
- **Generate** with gaflowlm (rotor-based flow matching)
- **Reason** with gattrlm (Clifford attractor for deep fixed-point computation)

Target: a 1B+ parameter GA-native language model trained from scratch, evaluated on reasoning (GSM8K, MATH, ARC-AGI), and compared head-to-head against equivalent standard architectures.

### Stage 6 — Multimodal Grounding (Long-term)

Conformal Geometric Algebra Cl(4,1) can represent 3D points, spheres, planes, and rotations as first-class citizens. Connect the GA language model to vision, robotics, and 3D scenes — creating a model that *understands* physical space because it speaks the language of space natively.

### Stage 7 — Inference Pipeline (Long-term)

GA-specific quantization, speculative decoding, and KV-cache compression. If the model is built on rotors and multivectors, the inference pipeline should exploit their structure rather than treating them as opaque matrices.

---

## The Bigger Picture

This isn't just a research program. It's a claim:

**Linear algebra has been good to us. But it's not the right language for describing transformation, composition, and meaning. Geometric Algebra is.**

The three repos are the working prototypes for that worldview. The book is the explanation. This roadmap is the plan.

---

*May 2026 — Peb Aryan*
