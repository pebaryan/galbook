## 10. Tokenization as Geometry

Every language model starts with a tokenizer. It converts raw text into a sequence of numbers that the model can process. Standard tokenizers use byte-pair encoding (BPE): start with individual characters, then repeatedly merge the most frequent adjacent pairs into new tokens.

BPE works, but it has a bias problem. Tokenizers trained on English-dominated corpora produce much longer token sequences for non-English languages — especially Southeast Asian languages, logographic scripts, and morphologically rich languages. The model sees more tokens for the same meaning, pays more compute, and often performs worse.

What if tokenization were a geometric operation?

---

### The Language Bias Problem

Standard BPE makes purely statistical decisions: merge the pair that appears most often. This naturally favors the language with the most training data. For English, the tokenizer finds efficient subwords quickly. For Indonesian, Malay, Tagalog, or Thai, it doesn't.

The result is **fertility disparity**: the number of tokens needed to represent the same content varies dramatically across languages.

| Language | Fertility | tokens/char | Ratio vs English |
|----------|-----------|-------------|------------------|
| English | 3.30 | 0.57 | 1.00× |
| Indonesian | 4.12 | 0.71 | 1.25× |
| Chinese | 2.45 | 0.43 | 0.75× |

A 25% longer sequence for Indonesian means 25% more compute for the same semantic content. The model is structurally penalized for processing non-English text.

---

### The GA Opportunity

What if merge decisions were based on geometric coherence, not just frequency?

Characters are embedded as multivectors in Cl(3,0). The embedding uses a non-degenerate basis derived from Unicode codepoints. Two adjacent characters form a potential merge. The geometric product between them tells us something about their relationship:

- **Strong scalar component**: the characters are compatible (they belong together)
- **Clean bivector**: the pair forms a coherent rotation plane
- **High trivector noise**: the combination is geometrically unstable

This shifts the merge criterion from "how often do they appear?" to "how geometrically coherent is their combination?"

**The Core Idea:**

1. Embed each character as a multivector in Cl(3,0)
2. For each potential merge, compute the geometric product of the two character multivectors
3. Score the merge using grade-aware metrics: bivector strength, scalar compatibility, and trivector noise
4. Merge the highest-scoring pair
5. Repeat

The result is a rotor-guided tokenizer that makes geometrically informed subword decisions.

---

### What We Built

**gatoken** implements two tokenizer variants:

**RotorSubwordTokenizer** uses the geometric product to score merges. Each character is embedded as a multivector. Merge candidates are ranked by the geometric coherence of their product, not by corpus frequency.

**TokenMultivectorTokenizer** extends this with learnable multivector representations. Each subword token is an `nn.Parameter` multivector. The tokenizer can be trained with geometric objectives:

- **E — Rotor Consistency Loss**: Related tokens should form clean bivector rotors; unrelated tokens should not.
- **C — Grade-wise Prediction Loss**: The scalar component predicts frequency, the bivector norm predicts syntactic role.
- **B — Reconstruction Loss**: A merged token should be reconstructible from its components via geometric product.

**Current Status:**

The implementation is early. The Cl(3,0) geometric product is correct and unit-tested (15 sign errors were fixed in the initial version). The rotor-guided merging runs on synthetic benchmarks.

But there are **no production comparisons yet** against sentencepiece, tiktoken, or other standard tokenizers. The fertility numbers shown above are from a small 49-sentence test set. Whether the geometric approach scales to corpus-level tokenization and whether it actually reduces cross-language bias remains to be tested.

---

### Why This Matters

Tokenization is the first operation in every language pipeline. If the tokenizer is biased, the entire pipeline is biased. A geometric approach doesn't just change how tokens are formed — it changes what information is preserved at the boundary between text and model.

If words are multivectors (Chapter 8), then tokens should be multivectors too. The tokenizer is the first geometric operation in the stack.

---
