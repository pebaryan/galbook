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

### A Concrete Example in 2D

Let's see this in 2D, where the math is simplest. Suppose we want to rotate the vector x = (1, 0) — pointing east — by 90 degrees counterclockwise. The result should be (0, 1) — pointing north.

In 2D, there's only one plane: the xy-plane. The bivector representing this plane is e₁∧e₂. To rotate by 90 degrees (θ = π/2), we build the rotor:

```
R = exp((π/4) · e₁∧e₂) = cos(π/4) + sin(π/4) · e₁∧e₂
  = 0.707 + 0.707 · e₁∧e₂
```

Now apply the sandwich:

```
x' = R · (1, 0) · R̃
   = (0.707 + 0.707·e₁₂) · e₁ · (0.707 - 0.707·e₁₂)
   = e₂  (= north ✓)
```

The bivector e₁∧e₂ encodes the rotation plane (the xy-plane), and the angle is built into the rotor coefficients.

### Rotors vs Rotation Matrices

Now contrast this with a rotation matrix:

```
R_matrix = | 0  -1 |   ·   |1|   =   |0|
           | 1   0 |       |0|       |1|
```

Both give the same answer. But there's a crucial difference: the rotor *is the rotation plane*. If you extract the bivector part of R, you get e₁∧e₂ — a direct algebraic representation of "rotating in the xy-plane." The rotation matrix hides this information in its four entries.

### Why Rotors Win

Rotors solve several problems that plague matrices:

- They generalize to any number of dimensions
- They compose by simple multiplication (R₁ followed by R₂ = R₂R₁)
- They're numerically stable and differentiable
- They give you the rotation *plane* explicitly through the bivector

Here's the kicker: **SLERP is just a grade-1 projection of rotor sandwich.** The trigonometric formula we've been using for years is a shadow of something richer. The rotor sandwich also preserves the bivector — the rotation plane — which SLERP discards entirely.

```
SLERP(a, b, t) = ⟨R_t a R̃_t⟩₁

Where R_t = exp(t/2 · a∧b), and ⟨...⟩₁ means "take only the vector part"
```

The trigonometric SLERP throws away the bivector information. The rotor version keeps everything.

---