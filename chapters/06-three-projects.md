## 6. Three Projects

This chapter tells the story of three projects that apply Geometric Algebra to language modeling. They're different approaches to the same question: *can GA improve how machines understand and generate language?*

### 6.1 gaflowlm: Flow Matching on the Sphere

Our first project, **gaflowlm**, starts with a simple observation: the most successful language models based on continuous diffusion — flow matching — operate on the surface of a hypersphere (S^{d-1}). They interpolate between noise and meaningful content using SLERP (spherical linear interpolation), which is a trigonometric operation.

But as we saw in Chapter 4, SLERP is a grade-1 projection of a rotor sandwich. The rotor operation is richer — it preserves the bivector (rotation plane) information that SLERP discards.

The experiment was straightforward: replace SLERP with rotor-based operations in an existing flow matching architecture (called S-FLM). The model is otherwise identical — same transformer backbone, same training procedure. The rotor version produces mathematically identical results (SLERP = rotor sandwich projected to grade 1).

We trained multiple models on **Sudoku** — a puzzle task where the model sees the first 81 digits of a 9×9 grid and must predict the remaining 81 digits. It's a simple test bed for evaluating new ideas in language modeling.

Every variant hit the same wall: **62.90% accuracy**. SFM baseline: 62.90%. RHF (rotor replacement): 62.90%. Clifford variant: 62.90%. No matter what we changed — model size, layers, learning rate — the ceiling held.

The breakthrough came when we realized the rotor representation gave us access to something new: the bivectors. By adding a loss term that pushed the 12 token embeddings toward orthogonality — making them geometrically more separable — we achieved **70.70% accuracy**. The bivector information let us see and fix a separability bottleneck we couldn't detect before.

**What gaflowlm taught us:** You don't need to change the model. You need to change what information you have access to. The rotor representation gave us a window into the rotation geometry, and that window revealed a fix.

---

### 6.2 gattrlm: Clifford Attractor Models (USC, 2025)

The second project, **gattrlm**, takes a completely different approach. Instead of flow matching, it uses **attractor models** — a fascinating alternative to transformer stacks.

#### The Deep Equilibrium (DEQ) Idea

Standard language models stack layers: layer 1, layer 2, ..., layer L. Each layer transforms the representation, and the total computation grows with the number of layers.

Deep Equilibrium models ask a different question: what if we learn a single transformation f and iterate it until we reach a fixed point?

```
x_{t+1} = f(x_t)   for t = 0, 1, 2, ...
```

Instead of stacking L layers, you apply the same block f repeatedly until the representation stops changing — until it reaches an **attractor** state. This decouples effective depth from memory: you can iterate for hundreds of steps while only storing the final state (using a mathematical trick called implicit differentiation).

This is the idea behind the paper *"Solve the Loop"* (Fein-Ashley & Rashidinejad, USC, 2025), which shows that attractor models match or exceed standard transformers at language modeling, reasoning (Sudoku, ARC-AGI), and in-context learning — while using constant memory.

#### Adding Geometric Algebra

The **gattrlm** extension adds Clifford algebra layers directly into the DEQ iteration block. Instead of processing plain vectors, the model processes **multivectors** — complete geometric objects with scalar, vector, bivector, and trivector components.

The DEQ block becomes a chain of geometric operations:
1. **RotorLayer**: learns bivector coefficients and applies the sandwich product R·x·R̃, giving the model built-in rotation equivariance
2. **CliffordLinear**: channel mixing that preserves blade structure across the multivector components
3. **GeometricProductLayer**: computes the geometric product of x with itself (quadratic self-interaction), creating cross-blade terms without adding parameters
4. **BladeSelector**: learns which geometric grades to amplify or suppress — effectively letting the model decide what kind of geometric information matters for each task

The result is an architecture with **built-in geometric priors** that would require extensive data augmentation for standard networks to learn.

#### Conformal Geometric Algebra for 3D Reasoning

The gattrlm project also implements **Cl(4,1) Conformal Geometric Algebra (CGA)**, which extends 3D Euclidean space into a 5D Minkowski-like space. CGA can represent spheres, circles, planes, and lines as **grade-1 multivectors** — the same type of object as a point. This means:
- Intersection of two spheres = geometric product, no special-case code
- Translation and rotation = same operation (a rotor), no separate matrix and vector
- Rigid motions = screw rotors combining rotation and translation in a single step

For language models that need to reason about physical space — describing a scene, following navigation instructions, or manipulating objects — this unified representation could be transformative.

**What gattrlm taught us:** GA isn't just about replacing operations in existing architectures. It enables entirely new model designs where geometry is built in from the ground up — and the DEQ framework gives you constant memory regardless of how deep the geometric reasoning goes.

---

### 6.3 gamuon: GA Reformulation of the Muon Optimizer

The third project, **gamuon**, takes GA in a completely different direction — not into the model architecture, but into the **optimizer**.

#### What is Muon?

The Muon optimizer (from the Grok paper, 2024) is a recent innovation in training large language models. It's based on a theoretical insight: the gradient signal in neural network training can be understood as a matrix structure, and the optimal update is related to the **orthogonalization** of that structure.

Muon works by computing the **matrix sign function** of the gradient — essentially asking "what is the nearest orthogonal matrix to this gradient?" — and using that as the update direction. This is related to Newton's method but much cheaper computationally.

For language models, Muon has been shown to train significantly faster than Adam (the standard optimizer), especially at scale.

#### Reformulating with GA

The key insight of **gamuon** is that the matrix sign function — the core computational primitive of Muon — is actually a **geometric operation**. Orthogonal matrices are rotors (in even dimensions). The sign function is related to the polar decomposition, which in GA terms is the decomposition of a multivector into a rotor times a positive definite factor.

Gamuon reformulates the entire Muon optimizer using Geometric Algebra:
- Gradients are multivectors in the Clifford algebra of the weight space
- The matrix sign function becomes a geometric function on multivectors
- The orthogonal constrain behaves naturally under the geometric product

This reformulation offers several potential advantages:
- **Natural gradient structure**: GA captures the manifold structure of the optimization landscape more faithfully
- **Unified treatment**: the same operations work for scalars, vectors, matrices, and higher-order weight structures — no special cases
- **Differentiable metric**: the geometric product naturally respects the metric of the parameter space

The project is in its early stages, but the core idea is compelling: if the optimal update in neural network training is a geometric operation, it should be expressed in the language of geometry.

**What gamuon teaches us:** GA isn't just about model architecture. It's a mathematical framework that can reshape how we think about training, optimization, and learning dynamics at every level.

---

