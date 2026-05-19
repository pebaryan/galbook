## 10. A Personal Note

If you're reading this and thinking "this is fascinating but I don't know where to start," you're not alone. Geometric Algebra has a steep learning curve, partly because it's so different from what most of us learned in school, and partly because it's not widely taught.

Start with these intuitions:

1. **Vectors are great, but they're limited.** They can point in a direction, but they can't describe planes, volumes, or rotations cleanly.

2. **Bivectors are the unsung heroes.** Planes of rotation, oriented areas — these show up everywhere in machine learning, but we've been using the wrong math to describe them.

3. **The geometric product is the star.** a·b + a∧b combines all the information from two vectors into one operation. Everything else follows from this.

4. **Rotors replace rotation matrices.** Cleaner, more general, differentiable, and they expose the rotation plane as a first-class citizen.

The beauty of Geometric Algebra is that it doesn't contradict anything you already know about vectors — it *completes* it. The dot product becomes the grade-lowering part of a larger whole. The cross product becomes the dual of the wedge product. Everything is connected.

And in a field where connection is everything — language — that might be exactly the right tool.

---

### Further Reading

- *Geometric Algebra for Computer Graphics* by John Vince — An accessible and very readable introduction, great for programmers
- *Linear and Geometric Algebra* by Alan Macdonald — The gentlest introduction
- *Geometric Algebra for Computer Science* by Dorst, Fontijne, and Mann — Practical and intuitive
- *Clifford Algebra to Geometric Calculus* by Hestenes and Sobczyk — The original modern treatment, for the mathematically brave

### Key Papers

| Paper | Where | What |
|-------|-------|------|
| GATr (Geometric Algebra Transformer) | NeurIPS 2023 | GA for E(3)-equivariant geometric data |
| GCANs (Geometric Clifford Algebra Networks) | ICML 2023 | Microsoft Research — group action layers via Clifford algebras |
| GAFL (Geometric Algebra Flow Matching) | NeurIPS 2024 | GA for protein backbone generation |
| Solve the Loop (Attractor Models) | arXiv 2605.12466 | DEQ fixed-point models for language |
| FGA (Functional GA for NLP) | arXiv 2604.25902 | GA as foundation for language semantics |
| CliffordNet | arXiv 2601.06793 (Jan 2026) | GA as general framework for neural nets (vision backbone) |

### Project Repositories

- **gaflowlm**: [github.com/pebaryan/gaflowlm](https://github.com/pebaryan/gaflowlm) — GA flow matching for language
- **gattrlm**: [github.com/pebaryan/gattrlm](https://github.com/pebaryan/gattrlm) — Clifford attractor model
- **gamuon**: [github.com/pebaryan/gamuon](https://github.com/pebaryan/gamuon) — GA reformulation of Muon optimizer
- **galbook**: [github.com/pebaryan/galbook](https://github.com/pebaryan/galbook) — This book (manuscript, roadmap, reviews)

---

The work described in these pages is still early. But every time we have given geometric structure a first-class role — in optimization, in generation, in attention, in reasoning — we have found something we could not see with matrices alone. That pattern is the real signal.

Whether Geometric Algebra becomes the next foundational language for machine learning or remains a powerful niche tool will depend on the rigor, scale, and honesty with which we pursue it. This book is one step in that direction.

*Written in May 2026, after one small victory (70.70% on Sudoku) and many questions still open.*
