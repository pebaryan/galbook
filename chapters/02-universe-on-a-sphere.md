## 2. Traveling the World

Imagine you're exploring a vast, spherical planet. Every point on this planet represents a different word meaning. "King" is a location. "Queen" is another. "Apple" is somewhere else entirely.

This planet has thousands of dimensions — too many to visualize — but the metaphor holds: language is a geography, and understanding meaning is about knowing where things are and how to travel between them.

Modern language models live on this planet. After processing any input, they normalize their representations to sit on the surface of a high-dimensional sphere. Why? Because distances on a sphere's surface are meaningful. The angle between two points tells you how similar they are. The closer the angle, the closer the meaning.

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

### The Traveler's Dilemma

Here's the problem with this kind of navigation: it tells you *where* you'll end up, but not *how* you got there.

Imagine sailing from Lisbon to New York. The great circle route gives you the shortest path. But consider: you could have sailed around the other way, past Africa and South America. Same start, same end — completely different journey. The route matters.

In language, this matters even more. The relationship "king → queen" isn't just a destination. It's a *direction* — a gender transformation happening in a specific semantic plane. SLERP tells you the coordinates of the halfway point, but it forgets which way you were facing when you started. It discards the plane of travel.

### Three Limitations of the Old Maps

Spherical interpolation works. It's mathematically sound. But it has fundamental limits:

1. **It erases your tracks.** The rotation happens in a specific plane, but the formula only gives you the destination — not the journey's geometry.

2. **You can't compose trips.** Sail from A to B, then B to C. There's no simple formula for the direct route from A to C. Each leg is computed separately, blind to the overall path.

3. **It's a fixed map.** You get one operation: interpolation along the surface. If you want richer transformations — rotations, reflections, projections — you need different tools entirely.

These aren't just mathematical curiosities. Language is full of complex transformations: negation, tense change, pluralization, sentiment shifts. Each is a different kind of journey. We need a way to represent not just *where* meanings are, but *how* to move between them.

We need better maps.

---