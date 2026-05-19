## 3. The Algebra We Forgot

Geometric Algebra (GA) was discovered — or rather, *re-discovered* — by the English mathematician William Kingdon Clifford in 1878. He died young (33), but his ideas were so ahead of their time that they're only now finding their natural home in machine learning.

The core idea is deceptively simple: **what if we could multiply vectors together?**

In school, we learn two ways to multiply vectors:
- The **dot product** (a·b): gives a number. "How much do these vectors point the same way?"
- The **cross product** (a×b): gives a vector perpendicular to both. Only works in 3D.

Clifford asked: what if we keep *both* pieces of information? The dot product captures alignment; the cross product captures oriented area. Why choose?

### The Problem with Traditional Tools

Before we dive into GA, let's understand why we need it. Traditional linear algebra gives us vectors and matrices. Vectors represent points and directions. Matrices represent transformations. This works, but it's limited.

Consider rotation. In 3D, we use rotation matrices — 3×3 arrays of numbers. But these have problems:
- They're redundant (9 numbers for 3 degrees of freedom)
- They can suffer from "gimbal lock" (losing a degree of freedom)
- They don't interpolate well (rotating halfway between two orientations is hard)
- They don't compose cleanly (matrix multiplication is expensive)

In higher dimensions, it gets worse. A rotation in n-dimensional space requires an n×n matrix. But the actual degrees of freedom grow as n(n-1)/2 — the number of independent planes you can rotate in.

GA solves this by representing rotations directly as operations on planes, not as matrices acting on coordinates.

### The Geometric Product

Clifford's insight was the **geometric product**:

```
ab = a·b + a∧b
```

The first part (a·b) is the dot product — a number (scalar). The second part (a∧b) is the *wedge product* — a new kind of object called a **bivector**, representing the oriented plane swept out by a and b.

![Geometric Product](../visualizations/media/images/ch3_ga_visualization/Scene1_GeometricProduct.png)

Instead of trying to visualize this with ASCII, here is a proper 3D animation that shows exactly how it works:

> **▶ Watch the 3D visualization**: [ch3_ga_visualization.mp4](../visualizations/ch3_ga_visualization.mp4)
> It demonstrates the geometric product, bivector orientation (including why a∧b = −b∧a), and how trivectors represent oriented volumes. The camera rotates around each object so you can see the geometry clearly.

### Understanding the Wedge Product

The wedge product (∧) is the key innovation. Where the dot product asks "how parallel?" the wedge product asks "how perpendicular?" More precisely, it captures the oriented area spanned by two vectors.

Imagine sweeping vector a along vector b. The area swept out is a parallelogram. This is the bivector a∧b. But it's not just an area — it's an *oriented* area. The order matters: a∧b is the negative of b∧a.

Why? Because sweeping a along b traces the parallelogram in the opposite direction from sweeping b along a. One is clockwise; the other is counterclockwise. The orientation is part of the object.

![Bivector Orientation](../visualizations/media/images/ch3_ga_visualization/Scene2_BivectorOrientation.png)

The antisymmetry of the wedge product — that a∧b = −(b∧a) — is fundamental. Swapping the order of vectors reverses the orientation of the resulting bivector.

### Higher Dimensions: Trivectors and Beyond

You can keep wedging. Three vectors a, b, c form a **trivector** a∧b∧c — an oriented volume. This is the 3D analog of the bivector.

The orientation follows the right-hand rule: if a, b, c follow your right-hand fingers (index, middle, thumb), the trivector is positive. Swap any two vectors, and it becomes negative.

![Trivector Volume](../visualizations/media/images/ch3_ga_visualization/Scene3_TrivectorVolume.png)

Three vectors combine to form a trivector, representing an oriented volume. The right-hand rule determines the orientation.

You can continue: four vectors form a quadvector (4D volume), and so on. In n-dimensional space, the highest grade object is an n-vector.

### Multivectors: The Unified Object

A **multivector** is the sum of objects of different grades:

```
M = scalar + vector + bivector + trivector + ...
```

In 3D, a general multivector looks like:
```
M = α + a₁e₁ + a₂e₂ + a₃e₃ + b₁e₁₂ + b₂e₂₃ + b₃e₃₁ + γe₁₂₃
```

Where:
- α is a scalar (grade 0)
- a₁e₁ + a₂e₂ + a₃e₃ is a vector (grade 1)
- b₁e₁₂ + b₂e₂₃ + b₃e₃₁ are bivectors (grade 2)
- γe₁₂₃ is a trivector (grade 3)

![Multivector Components](../visualizations/media/images/ch3_ga_visualization/Scene4_MultivectorComponents.png)

A single multivector can contain scalars, vectors, bivectors, and trivectors — all the geometric information about a point and its surrounding space.

This is powerful. A single multivector in 3D contains 8 numbers (2³ = 8), representing all possible geometric entities in that space. The geometric product knows how to combine these intelligently, preserving grade information.

### What GA Unifies

One of the remarkable things about Geometric Algebra is how it subsumes other mathematical systems:

- **Complex numbers** are multivectors in 2D with a scalar and one bivector (i = e₁₂)
- **Quaternions** are multivectors in 3D with a scalar and three bivectors
- **Vectors** are just grade-1 multivectors
- **Matrices** can be represented as multivector operators
- **Spinors** (used in quantum mechanics) are naturally multivectors

Instead of learning different systems for different dimensions and operations, GA provides one unified framework.

### Rotors: The Natural Representation of Rotation

Here's where GA gets really useful. In traditional math, we represent rotations with matrices. In GA, we represent them with **rotors**.

A rotor is an object of the form:
```
R = cos(θ/2) + sin(θ/2)B
```

Where B is a unit bivector representing the plane of rotation, and θ is the angle.

To rotate a vector v, you do:
```
v' = RvR⁻¹
```

This is called "sandwiching." The remarkable thing: this works in *any dimension*. The same formula rotates vectors in 2D, 3D, 4D, or 100D space. The rotor naturally encodes both the plane of rotation and the angle.

Compare this to rotation matrices:
- 2D rotation: 2×2 matrix
- 3D rotation: 3×3 matrix (Euler angles or axis-angle)
- 4D rotation: 4×4 matrix (what plane are you rotating in?)
- nD rotation: n×n matrix with n(n-1)/2 parameters

With rotors, the representation is always compact and geometrically meaningful. You always know what plane you're rotating in because it's explicit in the bivector part.

### Why This Matters for Language

Let's bring this back to language. In Chapter 2, we saw that language models live on a high-dimensional sphere, and that transformations (gender, tense, plurality) are like journeys on that sphere.

The problem with traditional vector approaches is that they only tell you *where* you are, not *how you got there* or *what plane you're moving in*.

Geometric Algebra solves this by:
1. **Encoding planes explicitly**: A bivector represents a transformation plane (like the "gender plane" that connects king↔queen)
2. **Composing transformations naturally**: Rotors multiply, so you can chain transformations
3. **Preserving orientation**: The antisymmetry captures the direction of transformation
4. **Working in any dimension**: Language models use hundreds or thousands of dimensions — GA scales naturally

Think about the transformation "king → queen." In vector space, this is a direction. In GA, this is a rotation in a specific plane. The bivector representing that plane encodes not just the transformation, but how it relates to other transformations.

If "man → woman" happens in the same plane (same bivector), we know these are the same *kind* of transformation. If it's a different plane, it's a different kind.

### The Geometric Intuition

The power of GA is that every object has geometric meaning:
- **Scalars** are magnitudes (grade 0)
- **Vectors** are directions (grade 1)
- **Bivectors** are oriented planes (grade 2)
- **Trivectors** are oriented volumes (grade 3)
- And so on...

When you multiply two vectors with the geometric product, you get both the scalar (how much they align) and the bivector (the plane they span). Both pieces of information are preserved.

This is why GA is sometimes called "the algebra of geometry." Every operation has a visual, geometric interpretation. You're not just manipulating numbers — you're manipulating geometric objects.

### From Here to Rotors

In the next chapter, we'll dive deep into rotors — the GA objects that represent rotations. We'll see how they:
- Encode rotation planes explicitly (solving the SLERP problem from Chapter 2)
- Compose naturally through multiplication
- Generalize to any dimension
- Give us the "compass and map" we were missing

But first, let's look at the landscape of GA in machine learning today.

The video is available in the `../visualizations/` folder, along with the Manim source code if you want to explore or modify the scenes yourself.

---