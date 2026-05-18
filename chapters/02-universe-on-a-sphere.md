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

### A Thought Experiment

Imagine yourself standing at the North Pole. If you walk in a straight line toward New York, you follow a great circle route — the shortest path on a sphere's surface. SLERP does the same thing in high-dimensional space: it moves between two points along the shortest arc on the sphere.

Now here's the problem: SLERP can tell you the coordinates of the halfway point between the North Pole and New York. But it can't tell you *which direction you were facing* when you started walking, or whether you passed through London or Tokyo on the way. The rotation plane — the 2D circle your path traces on the sphere's surface — is completely invisible.

This matters because in language, *how* you get from one concept to another often carries information. The relationship "king → queen" isn't just a start and end point — it's a gender transition happening in a specific semantic plane. SLERP discards that plane. Rotors preserve it.

### The Three Limitations

This works. It's mathematically correct. But it has limitations:

1. **It throws away information.** The rotation happens in a specific plane, but the trig formula only tells you the result — not *which way* you rotated.
2. **It can't compose cleanly.** Rotating from A to B, then B to C, doesn't give you a simple formula for going from A to C.
3. **It's rigid.** You only get one type of operation: interpolation on the sphere's surface. If you want richer transformations, you're out of luck.

These limitations might seem abstract, but they matter. Because language isn't just about moving between words — it's about *transforming meaning* in complex, compositional ways.

---