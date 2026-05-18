## 1. The Vector Revolution

Before we talk about Geometric Algebra, we need to understand a quiet revolution that happened in computer science over the last decade.

Machines don't understand words. They never have.

But they've learned something surprisingly close: they've learned to *place* words in space.

Every word in your vocabulary — "king", "queen", "apple", "computer", "sadness" — can be represented as a point in a high-dimensional space. Not 3D space like the one we live in, but a mathematical space with hundreds or thousands of dimensions. A single word becomes a list of numbers, like GPS coordinates for meaning.

This is called a **word embedding**, and it's arguably the single most important idea in modern AI.

### Why Embeddings Work

The magic is in the geometry. In this space, words that are related are *close together*. "King" and "queen" are near each other. More remarkably, the *relationships* between words show up as geometric patterns.

Consider a simple 2D analogy. Suppose we have two axes: one for "royalty" and one for "gender". In this toy space:

- "king" might sit at (0.9, 0.8)
- "queen" at (0.9, -0.8)
- "man" at (0.1, 0.7)
- "woman" at (0.1, -0.7)

The vector from "king" to "queen" is roughly (0, -1.6) — a downward shift in the gender direction. The vector from "man" to "woman" is almost identical. This is why the famous equation works:

```
king - man + woman ≈ queen
```

You're not just adding numbers. You're performing a **geometric transformation** in meaning space. The relationship "royalty with gender flipped" is captured as a direction you can add or subtract.

### The Power and the Problem

Vectors capture meaning through their *positions and directions*. Language models — the things that power ChatGPT, Claude, Gemini — are built on this foundation. They take sequences of these word-vectors and learn to predict what comes next, transforming them through layer after layer of computation.

But here's the thing: there's a deep limitation to how we've been doing this. Vectors are excellent at representing *points* and *directions*, but they're surprisingly poor at representing *relationships*, *transformations*, and *compositions* — the very things language does constantly.

And Geometric Algebra offers a way forward.

---