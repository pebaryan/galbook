# The Geometry of Meaning

## How Geometric Algebra Is Changing the Way Machines Understand Language

---

> *A gentle introduction for curious minds*

---

## 1. The Vector Revolution

Before we talk about Geometric Algebra, we need to understand a quiet revolution that happened in computer science over the last decade.

Machines don't understand words. They never have.

But they've learned something surprisingly close: they've learned to *place* words in space.

Every word in your vocabulary — "king", "queen", "apple", "computer", "sadness" — can be represented as a point in a high-dimensional space. Not 3D space like the one we live in, but a mathematical space with hundreds or thousands of dimensions. A single word becomes a list of numbers, like GPS coordinates for meaning.

This is called a **word embedding**, and it's arguably the single most important idea in modern AI.

The magic is in the geometry. In this space, words that are related are *close together*. "King" and "queen" are near each other. More remarkably, the *relationships* between words show up as geometric patterns. The vector from "king" to "queen" looks like the vector from "man" to "woman". You can literally do:

```
king - man + woman ≈ queen
```

Vectors capture meaning through their *positions and directions*. Language models — the things that power ChatGPT, Claude, Gemini — are built on this foundation. They take sequences of these word-vectors and learn to predict what comes next, transforming them through layer after layer of computation.

But here's the thing: there's a deep limitation to how we've been doing this. And Geometric Algebra offers a way forward.

---

## 2. The Universe on a Sphere

Imagine all possible word meanings living on the surface of a hypersphere — a sphere with many dimensions. Every concept is a point on this sphere, at unit distance from the center.

This isn't a metaphor. Most modern language models *actually do this*. After processing input, they normalize their representations to live on the surface of a sphere. Why? Because it makes the math stable and the comparisons meaningful.

On a sphere, the natural operation is **rotation**. To transform one thought into another, you rotate. To interpolate between "cat" and "dog", you move along a great arc on the sphere's surface — geodesic interpolation, or SLERP (Spherical Linear Interpolation).

```
      cat
     /
    /
   /  ← What's halfway between cat and dog?
  /
 dog
```

For years, this has been done with trigonometry. The formula for SLERP looks like this:

```
SLERP(a, b, t) = sin((1-t)ω)/sin(ω) · a + sin(tω)/sin(ω) · b
```

Where ω is the angle between vectors a and b, and t is how far along the path you want to go.

This works. It's mathematically correct. But it has limitations:

1. **It throws away information.** The rotation happens in a specific plane, but the trig formula only tells you the result — not *which way* you rotated.
2. **It can't compose cleanly.** Rotating from A to B, then B to C, doesn't give you a simple formula for going from A to C.
3. **It's rigid.** You only get one type of operation: interpolation on the sphere's surface. If you want richer transformations, you're out of luck.

These limitations might seem abstract, but they matter. Because language isn't just about moving between words — it's about *transforming meaning* in complex, compositional ways.

---

## 3. The Algebra We Forgot

Geometric Algebra (GA) was discovered — or rather, *re-discovered* — by the English mathematician William Kingdon Clifford in 1878. He died young (33), but his ideas were so ahead of their time that they're only now finding their natural home in machine learning.

The core idea is deceptively simple: **what if we could multiply vectors together?**

In school, we learn two ways to multiply vectors:
- The **dot product** (a·b): gives a number. "How much do these vectors point the same way?"
- The **cross product** (a×b): gives a vector perpendicular to both. Only works in 3D.

Clifford asked: what if we keep *both* pieces of information? The dot product captures alignment; the cross product captures oriented area. Why choose?

His insight was the **geometric product**:

```
ab = a·b + a∧b
```

The first part (a·b) is the dot product — a number. The second part (a∧b) is the *wedge product* — a new kind of object called a **bivector**, representing the oriented plane swept out by a and b.

```
    b
    ↑
    |    ← The parallelogram a∧b
    |   /    has area and orientation
    |  /
    | /
    a
```

This might seem like a small change, but it unlocks an entirely new mathematical universe. You can keep multiplying vectors and get higher-dimensional objects: **trivectors** (oriented volumes), **quadvectors**, and so on. These are all **multivectors** — the fundamental objects in Geometric Algebra.

A multivector lives in a space of 2^k dimensions, where k is the dimensionality of your original space. Because it doesn't just store the coordinates of a point — it stores scalars, vectors, planes, volumes, and more, all in a single unified mathematical object.

---

## 4. Rotors: The Engine of Change

If bivectors represent oriented planes, they're also the key to describing rotations.

In Geometric Algebra, a rotation is performed by a **rotor** — a special kind of multivector that encodes the rotation plane and angle. The rotor is built from a bivector using exponentiation:

```
R = exp(B/2)
```

Where B is a bivector representing the rotation plane and angle.

To rotate a vector x, you use the **sandwich product**:

```
x' = R x R̃
```

Where R̃ is the reverse of R (like a conjugate). The sandwich wraps around x, applies the rotation, and gives you the result.

This is a fundamentally different way of thinking about rotation. In school, we learn rotation matrices — rectangular arrays of numbers that transform vectors. Matrices work, but they can't compose cleanly (matrix multiplication is expensive, and small errors accumulate). Quaternions solve some of these problems in 3D, but they don't generalize to higher dimensions.

Rotors solve *all* of these problems:
- They generalize to any number of dimensions
- They compose by simple multiplication (R₁ followed by R₂ = R₂R₁)
- They're numerically stable and differentiable
- They give you the rotation *plane* explicitly through the bivector

Here's the kicker: **SLERP is just a grade-1 projection of rotor sandwich.** The trig formula we've been using for years? It's a shadow of something richer. The rotor sandwich also preserves the bivector — the rotation plane — which SLERP discards entirely.

```
SLERP(a, b, t) = ⟨R_t a R̃_t⟩₁

Where R_t = exp(t/2 · a∧b), and ⟨...⟩₁ means "take only the vector part"
```

The trigonometric SLERP throws away the bivector information. The rotor version keeps everything.

---

## 5. Why This Matters for Language

Okay, so rotors are mathematically elegant. But why should anyone who works with language care?

Let me tell you a story about Sudoku.

### The Sudoku Puzzle

In our lab, we've been training language models to solve Sudoku puzzles. The model sees the first 81 digits of a Sudoku grid (the "clues") and has to predict the remaining 81 digits. It's a simple test bed for evaluating new ideas.

The traditional approach works like this:
1. Each digit (1-9, plus special tokens) is embedded as a vector on a sphere
2. The model learns to transform noise into structured predictions through a process called **flow matching**
3. At the core of flow matching are SLERP operations — moving along the sphere from random noise toward meaningful content

We trained multiple models. Each hit the same ceiling: **62.90% accuracy**.

No matter what we changed — model size, number of layers, learning rate — we couldn't break through. It was like hitting a wall in a video game where you need a new ability to proceed.

### The Rotor Replacement

Then we tried something different. We replaced the trigonometric SLERP operations with rotor-based equivalents. Not changing the model architecture — just swapping the math under the hood.

The models were *numerically identical*. Same training loss, same convergence. No improvement.

But here's what changed: we had access to the bivectors now. The rotation planes. Information that was previously discarded.

We added a simple loss term that pushed the word embeddings toward orthogonality — making them more separable, more distinct. This is a natural thing to want: you want "1" and "2" to be clearly different, not overlapping.

But this loss competes with the main training objective. To make it matter, we had to weight it 30x relative to the primary loss.

The result: **70.70% accuracy.** A 7.8 point jump.

The rotor representation gave us access to geometric structure we couldn't touch before. The bivectors revealed the rotation dynamics, and that information let us design a better training signal.

This is just one small example, but it illustrates a broader point. When you have access to richer geometric structure, you can do richer things.

---

## 6. Beyond Rotors: The Multivector Hypothesis

If you're intrigued by the idea of bivectors (oriented planes), you might wonder: what else hides inside the multivector structure?

A multivector in Cl(3,0,0) — Geometric Algebra of 3D space — has eight components:

- 1 scalar (grade 0): a pure number
- 3 vectors (grade 1): directions
- 3 bivectors (grade 2): oriented planes
- 1 trivector (grade 3): oriented volume

Now imagine that instead of representing each word as a single vector in 512-dimensional space, you represent it as a *multivector* in a smaller Cl(8,0,0) space. Each word is now a package with:
- A **scalar** part: perhaps encoding abstract category information (noun-ness, verb-ness)
- A **vector** part: the primary semantic direction
- A **bivector** part: relationships, interactions, transformations
- Higher-grade parts: complex compositional structure

This is the **multivector embedding hypothesis**: different aspects of linguistic meaning naturally map to different grades of a multivector. The geometric product between words becomes a rich interaction, not just a simple comparison.

In this framework, the relationship between "king" and "queen" isn't just a vector difference — it's a full geometric transformation encoded in a multivector. The subspace captures "royalty" while the bivector captures "gender transition" as a rotation plane.

This is speculative. We're still early in testing it. But the math is there, waiting to be used.

---

## 7. Clifford Attention: Seeing in Planes

One of the most exciting developments is **Clifford Frame Attention (CFA)**.

Standard attention — the "attention is all you need" mechanism that powers every major AI system — compares vectors using dot products. It asks: "how similar is this word to that word?"

CFA asks a richer question: "how does this multivector transform that multivector?"

In CFA, each query, key, and value is a multivector. The attention computation uses the geometric product, which captures not just alignment but oriented-plane relationships. The model can learn to attend to specific *types* of geometric relationships — not just "similar words" but "words that rotate each other in a particular plane."

Early experiments suggest this captures syntactic structure more naturally. The geometric product between a subject and verb multivector might directly encode their grammatical relationship, without needing dozens of layers to learn it implicitly.

---

## 8. The Bigger Picture

Geometric Algebra isn't the only mathematical frontier in AI, but it's a particularly promising one because of a fundamental observation:

**Neural networks are already doing geometry. They're just using the wrong vocabulary.**

The word embeddings, rotations, transformations, and comparisons that language models perform daily are inherently geometric operations. But the tools we use to describe and implement them — matrices, trigonometry, dot products — miss the deeper structure.

Geometric Algebra offers:
- A **unified vocabulary** for scalars, vectors, planes, volumes, and rotations
- **Compositional operations** that naturally chain together
- **Richer representations** that capture information standard approaches discard
- **Differentiable** operations that work with modern machine learning frameworks

But it also faces real challenges:
- It's computationally expensive (a 256-dimensional multivector requires 2^256 components in full — we use projections to keep it tractable)
- The field is small — fewer than a thousand researchers worldwide work on GA for ML
- The benefits are often subtle, not dramatic 10x improvements

The history of science suggests that when you align your mathematics with the structure of your problem, progress accelerates. We used complex numbers instead of awkward trig for waves. We used matrices instead of scalar formulas for linear systems. We used tensors for general relativity.

Geometric Algebra for language modeling might be the next step in that progression.

---

## 9. Where We Are and Where We're Going

Our experiments are small — Sudoku puzzles, not billion-parameter models. But the trajectory is promising.

| Method | Accuracy | What changed |
|--------|----------|-------------|
| Standard SLERP flow | 62.90% | Baseline |
| Rotor replacement (same math) | 62.90% | Proves equivalence |
| Rotor + embedding contrastive | 70.70% | Used bivector structure |
| Clifford attention | Unknown | Next frontier |

The jump from 62.90% to 70.70% came not from replacing SLERP with rotors, but from *having access to the rotation plane information* that rotors provide. The bivectors told us something we couldn't see before, and we used that information to improve training.

That's the pattern we expect to repeat: not "replace A with B and get 10% better," but "use B's richer structure to discover something new."

The next steps:
- **Full multivector embeddings** for words, not just vectors on a sphere
- **Clifford attention layers** that process geometric relationships directly
- **Grade-structured losses** that give different geometric features different learning rates
- **Scalability** testing on larger models and real language tasks

---

## 10. A Personal Note

If you're reading this and thinking "this is fascinating but I don't know where to start," you're not alone. Geometric Algebra has a steep learning curve, partly because it's so different from what most of us learned in school, and partly because it's not widely taught.

Start with these intuitions:

1. **Vectors are great, but they're limited.** They can point in a direction, but they can't describe planes, volumes, or rotations cleanly.

2. **Bivectors are the unsung heroes.** Planes of rotation, oriented areas — these show up everywhere in machine learning, but we've been using the wrong math to describe them.

3. **The geometric product is the star.** a·b + a∧b combines all the information from two vectors into one operation. Everything else follows from this.

4. **Rotors replace rotation matrices.** Cleaner, more general, differentiable, and they expose the rotation plane as a first-class citizen.

The beauty of Geometric Algebra is that it doesn't contradict anything you already know about vectors — it *completes* it. The dot product becomes grade-lowering part of a larger whole. The cross product becomes the dual of the wedge product. Everything is connected.

And in a field where connection is everything — language — that might be exactly the right tool.

---

### Further Reading

- *Linear and Geometric Algebra* by Alan Macdonald — The gentlest introduction
- *Geometric Algebra for Computer Science* by Dorst, Fontijne, and Mann — Practical and intuitive
- *Clifford Algebra to Geometric Calculus* by Hestenes and Sobczyk — The original modern treatment, for the mathematically brave

Our lab's work: [github.com/pebaryan/gaflowlm](https://github.com/pebaryan/gaflowlm) — includes code, experiments, and mathematical derivations.

---

*Written in May 2026, after one small victory (70.70% on Sudoku) and many questions still open.*
