## 2. Traveling the World

Imagine you're exploring a vast, spherical planet. Every point on this planet represents a different word meaning. "King" is a location. "Queen" is another. "Apple" is somewhere else entirely.

This planet has thousands of dimensions — too many to visualize — but the metaphor holds: language is a geography, and understanding meaning is about knowing where things are and how to travel between them.

Modern language models live on this planet. After processing any input, they normalize their representations to sit on the surface of a high-dimensional sphere. Why? Because distances on a sphere's surface are meaningful. The angle between two points tells you how similar they are. The closer the angle, the closer the meaning.

### Why a Sphere?

Before we travel, let's understand the terrain. In high-dimensional spaces, vectors tend to have wildly different magnitudes. A word like "the" appears everywhere and might have huge values; a rare word like "pneumonoultramicroscopicsilicovolcanoconiosis" has seen fewer examples and smaller values.

Normalization fixes this. We scale every vector to length 1, forcing them onto the sphere's surface. Now comparisons are fair: only direction matters, not magnitude. The dot product between two points becomes the cosine of the angle between them — a pure measure of similarity.

This is why "cosine similarity" is the standard metric in NLP. It measures how close two travelers are on the planet's surface, regardless of how famous or obscure their home locations might be.

### The Art of Navigation

On a sphere, you don't walk in straight lines through the interior. You follow the surface — great circle routes, the paths airplanes fly. The shortest path from London to Tokyo isn't through the Earth's core; it's an arc across the surface.

Language models use the same principle: **spherical interpolation** (SLERP). To move from "cat" to "dog," you don't cut through the middle of the sphere. You follow the surface:

```
      cat
     /
    /
   /  ← What's halfway between cat and dog?
  /
 dog
```

For decades, this navigation required trigonometry:

```
SLERP(a, b, t) = sin((1-t)ω)/sin(ω) · a + sin(tω)/sin(ω) · b
```

Where ω is the angle between your starting point and destination, and t is how far along the journey you've traveled.

### Different Kinds of Journeys

Not all travel is the same. Consider these transformations in language:

**Gender:** king → queen, man → woman, actor → actress  
**Tense:** walk → walked, run → ran, eat → ate  
**Plurality:** cat → cats, child → children, mouse → mice  
**Sentiment:** happy → sad, good → bad, love → hate  
**Negation:** possible → impossible, happy → unhappy

Each is a different kind of journey on our spherical planet. Gender seems to follow a consistent direction across many words. Tense changes cluster together in their own region. Sentiment has its own axis.

In the early days of word embeddings, researchers discovered something remarkable: these semantic relationships showed up as geometric relationships. The vector from "king" to "queen" was strikingly similar to the vector from "man" to "woman." The direction of travel encoded the type of transformation.

This suggested a beautiful hypothesis: maybe all semantic relationships are just directions on the sphere. Want to make a word plural? Add the "plural direction." Want to negate it? Add the "negation direction."

But there's a problem. Real language transformations aren't simple vector additions. Consider:

- "Walk" + plural direction ≈ "walks" (works)
- "Run" + plural direction ≈ "runs" (works, but the transformation is different)
- "Child" + plural direction ≠ "children" (fails completely)

Irregular forms break the simple directional model. Worse, some transformations don't commute:

- happy → unhappy → unhappiness (works)
- happy → happiness → unhappiness (also works, but different intermediate)

The journey matters. The path you take affects where you end up.

### The Traveler's Dilemma

Here's the fundamental problem with spherical interpolation: it tells you *where* you'll end up, but not *how* you got there.

Imagine sailing from Lisbon to New York. The great circle route gives you the shortest path. But consider: you could have sailed the other way around the globe, past Africa, the Indian Ocean, Australia, and South America. Same start, same end — completely different journey.

SLERP always takes the shortest path. It has no memory of the route.

In language, this matters enormously. The relationship "king → queen" isn't just a destination. It's a *direction* — a gender transformation happening in a specific semantic plane. SLERP tells you the coordinates of the halfway point, but it forgets which way you were facing when you started. It discards the plane of travel.

Why does the plane matter? Because transformations compose differently depending on which planes they occupy. Two rotations in the same plane commute: rotate 30° then 40°, or 40° then 30° — same result. But rotations in different planes don't commute. The order matters.

Imagine you're at the North Pole facing New York. You could:
1. Rotate to face London, then rotate to face Tokyo
2. Rotate to face Tokyo, then rotate to face London

Different sequences, different final orientations. The planes of rotation interact.

Language has the same structure. Tense and plurality sometimes commute ("walked" → "walks" → "walkeds"? No, "walked" stays "walked"). Sometimes they don't (irregulars like "child" → "children" → ?). The semantic planes interact in complex ways.

### Three Limitations of the Old Maps

Spherical interpolation works. It's mathematically sound for what it does. But it has fundamental limits:

1. **It erases your tracks.** The rotation happens in a specific plane, but SLERP only gives you the destination coordinates. The geometry of the journey — which plane you traveled through, which direction you faced — is lost.

2. **You can't compose trips.** Sail from A to B, then B to C. There's no simple formula for the direct route from A to C. Each leg is computed separately, blind to the overall path. To compose rotations, you need to know their planes.

3. **It's a fixed map.** You get one operation: interpolation along the surface. If you want richer transformations — rotations that preserve the plane, reflections across subspaces, projections onto regions — you need different tools entirely.

These aren't just mathematical curiosities. Language is full of operations that aren't simple interpolation:

- **Negation** isn't a point between "happy" and "sad." It's a transformation that flips sentiment.
- **Question formation** isn't interpolation. It restructures the semantic field.
- **Metaphor** maps whole regions onto other regions: "time is money" reorients an entire conceptual domain.

We need a way to represent not just *where* meanings are, but *how* to move between them. We need to encode the planes of transformation, not just the endpoints.

### The Compass and the Map

Here's a question: what would a better navigation system look like?

On our spherical planet, SLERP is like having a GPS that tells you your coordinates but no compass direction. You know you're halfway between London and Tokyo, but you don't know which way is north. You don't know the orientation of your journey.

What if you had both? Coordinates *and* orientation? Position *and* direction?

This is the intuition behind Geometric Algebra. It doesn't just represent points on the sphere. It represents the *operations* that move between them — and crucially, it keeps track of the planes in which those operations happen.

Instead of just saying "go from A to B," it says "rotate in this specific plane by this specific angle." The plane is explicit. The orientation is preserved.

Think of it as the difference between:
- "Travel from Lisbon to New York" (SLERP)
- "Sail 53° west of north along the great circle, keeping the North Star 40° above the horizon" (Geometric Algebra)

The second description contains more information. It tells you not just where you're going, but how to get there — and how to continue from there.

In the next chapter, we'll meet the mathematical objects that make this possible: multivectors, the building blocks of Geometric Algebra. They're like having a compass, a sextant, and a complete map of the spherical planet — not just coordinates, but the full geometry of travel.

---