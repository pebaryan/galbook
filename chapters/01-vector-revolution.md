## 1. The Vector Revolution

Before we talk about Geometric Algebra, we need to understand a quiet revolution that happened in computer science over the last decade.

Machines don't understand words. They never have.

But they've learned something surprisingly close: they've learned to *place* words in space.

### How Computers Used to Process Language

Before dense vectors, computers handled language in much more rigid, symbolic ways.

In the early days of natural language processing (the 1950s through the 1990s), language was treated as a set of rules and symbols. Systems like ELIZA (1966) used pattern matching and substitution rules to simulate conversation. Later statistical approaches, such as n-gram models, simply counted how often words appeared next to each other in large corpora. These models could generate surprisingly fluent text for their time, but they had no real understanding of meaning — they were essentially sophisticated autocomplete systems.

![ELIZA and AIML Rule-Based Systems](../visualizations/media/images/ch1_eliza_alice/ElizaRuleBased0861.png)

When neural networks entered the picture, the first approach was **one-hot encoding**. Each word in the vocabulary was represented as a long vector of zeros with a single "1" in the position corresponding to that word. This worked, but it had two fatal problems:

- The vectors were extremely sparse (mostly zeros)
- There was no notion of similarity — "king" and "queen" were just as different as "king" and "apple"

Bag-of-words and TF-IDF improved on this by weighting words according to how important they were in a document, but they still treated words as independent atomic symbols. There was no geometry, no relationships, and no way to capture that "king" and "queen" share something meaningful.

![One-Hot vs TF-IDF](../visualizations/media/images/ch1_onehot_tfidf/OneHotVsTFIDF0782.png)

This was the world before the vector revolution.

### The Vector Revolution

Every word in your vocabulary — "king", "queen", "apple", "computer", "sadness" — can now be represented as a point in a high-dimensional space. Not 3D space like the one we live in, but a mathematical space with hundreds or thousands of dimensions. A single word becomes a list of numbers, like GPS coordinates for meaning.

This is called a **word embedding**, and it's arguably the single most important idea in modern AI.

### Why Embeddings Work

The magic is in the geometry. In this space, words that are related are *close together*. "King" and "queen" are near each other. More remarkably, the *relationships* between words show up as geometric patterns.

Consider a simple 2D analogy. Suppose we have two axes: one for "royalty" and one for "gender". In this toy space:

- "king" might sit at (0.9, 0.8)
- "queen" at (0.9, -0.8)
- "man" at (0.1, 0.7)
- "woman" at (0.1, -0.7)

The vector from "king" to "queen" is roughly (0, -1.6) — a downward shift in the gender direction. The vector from "man" to "woman" is almost identical. This is why the famous equation works:

![2D Embedding Space](../visualizations/media/images/ch1_vector_revolution/Scene2_2DEmbeddingSpace0294.png)

```
king - man + woman ≈ queen
```

You're not just adding numbers. You're performing a **geometric transformation** in meaning space. The relationship "royalty with gender flipped" is captured as a direction you can add or subtract.

### The Power and the Problem

Vectors capture meaning through their *positions and directions*. Language models — the things that power ChatGPT, Claude, Gemini — are built on this foundation. They take sequences of these word-vectors and learn to predict what comes next, transforming them through layer after layer of computation.

But here's the thing: there's a deep limitation to how we've been doing this. Vectors are excellent at representing *points* and *directions*, but they're surprisingly poor at representing *relationships*, *transformations*, and *compositions* — the very things language does constantly.

And Geometric Algebra offers a way forward.

---