# The Geometry of Meaning

![Book Cover](assets/cover.png)

*How Geometric Algebra Is Changing the Way Machines Understand Language*

An accessible book-length introduction to Geometric Algebra (GA) and its applications to language modeling, written for a general audience. No advanced math required — just curiosity and basic vector concepts.

## What's Inside

| Ch | Title | Focus |
|----|-------|-------|
| — | [Frontmatter](chapters/00-frontmatter.md) | Introduction |
| 1 | [The Vector Revolution](chapters/01-vector-revolution.md) | Embeddings, from one-hot to subword tokenization |
| 2 | [Traveling the World](chapters/02-universe-on-a-sphere.md) | The hypersphere, SLERP, and spherical geometry |
| 3 | [The Algebra We Forgot](chapters/03-algebra-we-forgot.md) | Geometric Algebra fundamentals |
| 4 | [Rotors: The Engine of Change](chapters/04-rotors.md) | Rotations in GA |
| 5 | [The Attention Mechanism](chapters/05-attention-mechanism.md) | How transformers focus, and their linear limitation |
| 6 | [Explorations](chapters/06-ga-ml-landscape.md) | How others apply GA (GATr, GAFL, FGA) |
| 7 | [Three Projects](chapters/07-three-projects.md) | gaflowlm, gattrlm, gamuon — our research |
| 8 | [The Multivector Hypothesis](chapters/08-multivector-hypothesis.md) | Language as geometric algebra |
| 9 | [The Roadmap](chapters/09-roadmap.md) | Where we go from here |
| 10 | [Tokenization as Geometry](chapters/10-tokenization-as-geometry.md) | gatoken: rotor-guided tokenization |
| 11 | [The Byte-Level Test](chapters/11-the-byte-level-test.md) | bbt: GA diffusion at the byte level |
| 12 | [A Personal Note](chapters/12-personal-note.md) | Getting started with GA |

## Book Structure

The book follows a learning progression:

- **Chapters 1-4**: Foundations — from familiar concepts (embeddings, attention) to GA machinery (multivectors, rotors)
- **Chapters 5-7**: The Landscape — how GA is being applied, by others and by us
- **Chapters 8-11**: The Hypothesis — what language might *be*, and how to test it
- **Chapter 12**: Starting point — resources for readers who want to explore further

## Projects Covered

This book draws on both published research and active open-source projects:

| Project | Repo | Chapter | Status |
|---------|------|---------|--------|
| gaflowlm | [github.com/pebaryan/gaflowlm](https://github.com/pebaryan/gaflowlm) | 7 | RHF validated; CFS active research |
| gattrlm | [github.com/pebaryan/gattrlm](https://github.com/pebaryan/gattrlm) | 7 | Prototype; equivariance proven, text neutral |
| gamuon | [github.com/pebaryan/gamuon](https://github.com/pebaryan/gamuon) | 7 | Implemented; no benchmarks yet |
| gatoken | [github.com/pebaryan/gatoken](https://github.com/pebaryan/gatoken) | 10 | Early implementation |
| bbt | [github.com/pebaryan/bbt](https://github.com/pebaryan/bbt) | 11 | PPL 1.723 at 1B tokens (small scale) |

And key external works: GATr (Qualcomm), GAFL (HITS), FGA (Pustejovsky), CliffordNet, and more.

## Visualizations

Each chapter includes Manim visualizations:

- Chapter 1: 7 illustrations (embeddings, Zipf's law, tokenization)
- Chapter 2: 5 illustrations (hypersphere, SLERP, journeys)
- Chapter 3: 4 illustrations (geometric product, bivectors, trivectors)
- Chapter 4: 6 illustrations (rotors, sandwich product, quaternions)
- Chapter 5: 4 illustrations (Q/K/V, attention scores, multi-head, GA comparison)
- Chapter 6: 4 illustrations (3D symmetry, structured generation, composition)
- Chapter 7: 4 illustrations (hidden information, architecture, memory, stack)
- Chapter 8: 4 illustrations (red car, vocabulary, rotor vs offset, CFA)
- Chapter 9: 3 illustrations (integrated stack, roadmap, honest assessment)
- Chapter 10: 3 illustrations (tokenization, language bias, geometric merging)
- Chapter 11: 3 illustrations (byte-level, diffusion, scaling test)

## Status

Revised draft (June 2026). Chapter 7 was rewritten to remove an unverifiable Sudoku metric (70.70%) and replace it with an honest accounting of each project's status. Chapters 10-11 were added to cover gatoken and bbt. The roadmap (Chapter 9) is now conditional — each step depends on previous results showing real, reproducible wins.

## License

The text and illustrations in this book are licensed under **CC BY-SA 4.0** (Creative Commons Attribution-ShareAlike 4.0 International).

You are free to share and adapt the content for any purpose, as long as you provide attribution and share any adaptations under the same terms.

Code in this repository (examples, scripts) is licensed under the **MIT License** — see the individual files for details.
