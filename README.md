# CEGIS
# When Physics Computes Without Symbolic Reason  
## Turing-Rationality, Abductive Reconstruction, and the Limits of Symbolic Computation

**Bruce Matichuk**

---

## Abstract

The Church–Turing thesis characterizes which functions are computable, but it is silent on a distinct question: under what conditions does a computation count as rational in a symbolic sense? Contemporary physical and statistical computing systems—including quantum computers, optical processors, and large language models—routinely produce correct symbolic outputs while offering little or no symbolic account of how those outputs are obtained.

We introduce **Turing-rationality** as a criterion for when computation admits rational explanation. A computation is Turing-rational iff its transition from input to output can be abductively reconstructed as a sequence of symbolic intermediate states—**reason-states**—that track inferential progress. We operationalize this criterion with three tests for reason-states: **type-level interpretability**, **alternative realizability**, and **compositional evaluability**, together with a run-level requirement that the resulting trace be **run-specific**, **counterfactually discriminable**, and **narratively coherent**.

Applying this framework, we argue that quantum computation, optical diffraction, and many continuous dynamical systems fail Turing-rationality not due to practical opacity but due to structural features of their state spaces and evolution. These systems compute functions that are Turing-computable—there exist Turing machines that can simulate their behavior. However, such simulations replace the original physical process with classical bookkeeping that has its own (different) symbolic state structure. The simulation’s states are not the original system’s states, and the simulation’s reason-trace (if any) does not explain the original system’s inference. The gap is not whether a process can be simulated Turing-rationally, but whether the process itself admits Turing-rational reconstruction.

Large language models present a distinctive case. Unlike quantum systems whose intermediates are purely physical, LLMs exhibit partial symbolic structure: learned representations preserve compositional, inferential, and analogical regularities drawn from language without implementing discrete symbolic commitments. We formalize this as **Partial Symbol Inductive Reasoning (PSIR)** and show that PSIR systems occupy a novel category—symbol-producing computation without Turing-rational intermediates.

This yields a principled account of hallucination: a conclusion is hallucinatory (relative to a hypothesis language) when no consistent abductive explanation exists that makes it necessary from the premises. Hallucination is thus not merely factual error but failure of rational justification—a predictable consequence of reasoning without symbolic commitments.

Finally, we show that non-Turing-rational systems can be scaffolded externally. Using **counterexample-guided inductive synthesis (CEGIS)**, one can recover explicit symbolic theories from PSIR behavior. These recovered theories function as rational guardrails—validating outputs, stabilizing iteration, and closing systematic reasoning gaps—without requiring the underlying system to become Turing-rational internally. We conclude by arguing that the universe itself is not Turing-rational: physical laws are not the universe’s reasons but our abductive reconstructions. Rationality is therefore not fundamental but emergent—local, fragile, and engineered within a fundamentally non-rational cosmos.

**Keywords:** computability; rationality; quantum computation; abduction; explainability; hallucination; large language models; theory recovery; CEGIS; philosophy of science

---

## 1. Introduction

The Church–Turing thesis (CTT) is the canonical boundary marker of computability: it characterizes which functions are effectively computable, abstracting away from physical realization, efficiency, and implementation detail. Yet CTT is largely silent on a question that has become increasingly urgent: **when does a computation count as rational in a symbolic sense?**

Modern computing systems repeatedly expose this gap. We now deploy systems that reliably map symbolic inputs to symbolic outputs while offering little or no symbolic account of how those outputs are produced. Quantum computers can achieve dramatic speedups by exploiting superposition and interference, yet their intermediate states resist interpretation as discrete reasoning steps. Optical processors compute transforms such as Fourier transforms through wave propagation and interference rather than via inspectable symbolic intermediates. Large language models, meanwhile, generate fluent and often correct text by evolving distributed activation patterns that typically lack explicit symbolic commitments.

These cases are philosophically salient not because they exceed Turing computability—most do not—but because they appear to perform inferential work without instantiating symbolically reconstructible reasoning processes. The motivating distinction of this paper is therefore **intensional** rather than extensional. We are not primarily asking what can be computed in principle; we are asking when a computation admits a symbolic form of rational explanation.

Classical Turing machines matter not merely because of what they compute, but because of how they compute: through sequences of discrete, symbolically representable states connected by explicit transition rules. These intermediate states function as **reasons**—partial commitments, constraints, or conclusions—whose ordered progression can explain why a particular output was produced rather than another. By contrast, many physically grounded computations accept symbolic inputs and return symbolic outputs while lacking intermediate states that function as symbolic reasons. Their internal dynamics do not support a reason-trace; at best they admit a law-like specification of behavior.

To articulate this gap precisely, we introduce **Turing-rationality**: a computation is Turing-rational when its input–output transition admits an abductive reconstruction as a sequence of symbolic intermediate states that plausibly track inferential progress. This criterion separates two questions that are often conflated. Extensional questions ask which functions can be computed at all, while intensional questions ask how a computation is rationally explainable as a sequence of intelligible commitments or inferential moves. A system may be correct, reliable, physically realizable, and Turing-computable—and still fail to be rationally transparent in the symbolic sense.

This paper makes seven contributions:

1. Introduces **Turing-rationality** as a criterion separating computability from rational intelligibility.  
2. Provides operational tests for **reason-states** and run-level reconstruction constraints.  
3. Applies the framework to **quantum computation**, including a response to the circuit-description objection.  
4. Introduces **PSIR** to explain why LLMs are symbol-producing systems whose intermediates typically fail to be Turing-rational.  
5. Defines **hallucination** as abductive justification failure relative to a hypothesis language, rather than mere factual error.  
6. Develops **CEGIS-based theory recovery** as external rational scaffolding.  
7. Advances a cosmological thesis: the universe itself is not Turing-rational; physical laws are abductive reconstructions rather than nature’s reasons.

**Roadmap.** Section 2 develops background distinctions. Section 3 defines Turing-rationality. Section 4 applies the framework to quantum computation. Section 5 generalizes to physical computation and argues for a non-rational universe. Section 6 introduces PSIR for LLMs. Section 7 defines hallucination as abductive explainability failure. Section 8 develops CEGIS theory recovery as scaffolding. Section 9 concludes.

---

## 2. Background: Computation, Explanation, and Abduction

CTT concerns whether a function is effectively computable. It does not imply that an effective procedure must instantiate discrete symbolic steps in its physical realization. Rather, it asserts an equivalence of computable mappings: for any effective procedure, a Turing machine exists that computes the same input–output function. A crucial consequence follows: a physical system may compute a Turing-computable function even if its internal dynamics bear little resemblance to stepwise symbolic manipulation. Accordingly, we must distinguish **computability**—what input–output mappings can be realized—from **rationality**—whether a mapping is realized in a way that admits symbolic explanation.

In logic, mathematics, and classical AI, rational computation is typically identified with **symbolic reasoning**. It proceeds through discrete intermediate states that can be represented symbolically, connected by explicit inferential rules, and interpreted as reasons in the justificatory sense—premises, constraints, partial conclusions, or preserved commitments. A familiar example is binary search, whose intermediate states are constraints on where the solution may lie. Even when too fast or too long to follow in detail, the process remains intelligible as a chain of commitments. Importantly, symbolic rationality does not require determinism. Heuristic and stochastic procedures can be rational when their intermediate states remain interpretable as reason-states.

Physical computation stresses the identification of computation with symbolic reason-traces. In many physical systems, the relevant “states” are physical configurations, transitions are governed by physical laws rather than symbolic rules, and state spaces are continuous, global, or non-local. This highlights a second distinction, between **law-specification** and **reason-tracing**. Law-specification explains why a process behaves as it does in general at the type level, typically by giving governing dynamics. Reason-tracing explains how this particular output follows from this particular input by citing intermediate symbolic commitments that track inferential progress at the run level. Physics provides exceptionally powerful law-specifications, but the existence of a law-specification does not entail that the physical process instantiates a symbolic reason-trace.

A common reply is that any physical process can be simulated digitally, and therefore must have symbolic intermediate states. But simulation replaces the physical process with a symbolic surrogate. It preserves the input–output mapping, not the internal inferential structure of the original process. The question here is not whether a reason-trace exists for *some* system computing the same function, but whether the actual computation performed admits rational reconstruction as a symbolic reason-trace.

This motivates **abduction**—inference to the best explanation—as a minimal standard of rational explanation. We do not require that intermediate states be directly observable, and we do not require that a reconstruction mirror physical mechanism step-by-step. What we do require is that a plausible symbolic sequence can be posited that tracks inferential progress in a way that supports public justification.

---

## 3. Turing-Rationality

Turing machines exemplify a distinctive form of rationality: they compute by stepping through discrete symbolic configurations under explicit transition rules. Those configurations can function as reasons. The aim of this section is to formalize when that kind of rational explanation is available more generally, even for systems whose internal mechanisms may not literally match a classical machine.

### 3.1 Reason-states and reason-traces

The core intuition is **abductive reconstructibility**. A computation is Turing-rational when we can abductively reconstruct an internal narrative of progress in which constraints are applied, alternatives are eliminated, partial solutions are refined, and commitments are made and preserved in an intelligible order. This motivates a two-part requirement:

1. Intermediate states must qualify as **reason-states**.  
2. Those states must form a run-specific **reason-trace** explaining why this output resulted from this input.

Not every intermediate configuration counts as a reason. We capture the reason-state concept with three properties:

- **Type-level interpretability:** describable in problem-domain vocabulary (constraint set, candidate solution, partial proof).  
- **Alternative realizability:** the same inferential position can be reached by more than one route while retaining meaning.  
- **Compositional evaluability:** supports partial evaluation (progress/consistency/partial correctness) without completing the run.

**Definition (Reason-State).**  
An intermediate state *S* is a **reason-state** iff it is type-level interpretable, alternatively realizable, and compositionally evaluable.

Even if reason-states exist, a computation is not Turing-rational unless they can be organized into a coherent run-specific trace.

**Definition (Law-specification vs. reason-trace).**  
A **law-specification** describes the rules/dynamics governing state evolution (type-level). A **reason-trace** is a run-specific sequence of reason-states that explains why this output followed from this input (token-level).

A reason-trace must satisfy three run-level constraints:

- **Run-specificity:** distinguishes this run from other runs of the same algorithm type.  
- **Counterfactual discriminability:** small input variations yield systematic, interpretable trace variations.  
- **Narrative coherence:** each transition is intelligible as an inferential step.

**Definition (Run-Level Reconstruction).**  
A sequence \( R=\langle S_1,\dots,S_n\rangle \) is a **reason-trace** for run \( C(I)=O \) iff it is run-specific, counterfactually discriminable, and narratively coherent.

**Definition (Turing-Rationality).**  
A computation \( C \) with input \( I \) and output \( O \) is **Turing-rational** iff there exists a sequence \( \langle S_1,\dots,S_n\rangle \) such that each \( S_i \) is a reason-state, the sequence is a reason-trace for this run, \( S_1 \) is consistent with \( I \), and \( S_n \) is consistent with \( O \).

These definitions are operational rather than metaphysically demanding. Turing-rationality does not require determinism, deductive certainty, real-time observability, efficiency, or a reconstruction that mirrors physical mechanism step-for-step. It requires only that a plausible abductive reason-trace exists under the stated constraints.

---

## 4. Quantum Computation Without Turing-Rationality

Quantum computing is a paradigmatic case where symbolic interfaces coexist with non-symbolic interiors. Quantum computation is typically bracketed by classical interfaces: classical data are encoded into a quantum state, the system evolves via unitary transformations, and a classical output is obtained by measurement. This supports computability (and sometimes dramatic complexity advantages) but does not by itself provide a reason-trace.

The reason-state tests fail for structural reasons. Quantum intermediates are vectors in a (typically enormous) Hilbert space. Amplitude assignments are not naturally interpretable as “hypotheses considered,” “constraints applied,” or “partial conclusions.” Intermediate states are tightly path-dependent under unitary evolution, undermining alternative realizability in the intended justificatory sense. Compositional evaluability is blocked because direct inspection generally requires measurement, which collapses the state and changes the computation. Quantum computation is therefore usually **law-specifiable** without being **reason-traceable**.

A predictable objection is that the circuit is the reason-trace. Quantum circuits are symbolic descriptions of operations—initialize, apply an oracle, apply a diffusion-like transform, repeat, then measure—and it is tempting to treat this sequence as a chain of reasons. The problem is that circuit descriptions function as law-specifications: they explain why the algorithm works in general rather than how this particular run arrived at this particular output via intermediate symbolic commitments. On the run-level criteria, the same circuit description applies across many runs and outcomes, so it lacks run-specificity; varying the marked element changes parameters rather than producing an interpretable chain of commitments; and while the evolution is mathematically coherent (unitary rotations), it is not narratively coherent as a sequence of symbolic reasons with eliminations, commitments, and checkpoints.

Grover search offers a clear contrast. Classical search offers reason-states of the familiar kind: “checked index 0,” “not found,” “checked index 1,” and so on. Grover’s algorithm acts globally on a superposition; it does not instantiate candidate-by-candidate commitments. A correct output is achieved without a reason-trace of the classical kind. This suggests a performance–transparency tradeoff: quantum advantage often arises from bypassing symbolically inspectable intermediate commitments.

### Table 1: Classical vs. Quantum Search

| Feature | Classical symbolic search | Grover-style quantum search |
|---|---:|---:|
| Intermediate “states” | symbolic commitments | amplitude distributions |
| Inspectable without disruption | yes | no (measurement disrupts) |
| Compositional evaluation | yes | no |
| Reason-trace available | typically yes | typically no |
| Complexity | \(O(N)\) | \(O(\sqrt{N})\) (idealized) |

---

## 5. Physical Computation and the Non-Rational Universe

Quantum computation illustrates a broader phenomenon: many physical processes compute functions (or realize reliable input–output relations) without supporting Turing-rational reconstruction. Across many physical computing regimes we encounter continuous state spaces, global or non-local dynamics, limited access to intermediates, strong path dependence, and an absence of discrete symbolic commitments. These are not merely pragmatic obstacles; they are often structural features of the systems’ state spaces and dynamics.

Consider chaotic dynamical systems (for example, a double pendulum). Their trajectories are computable to arbitrary precision via numerical methods (within practical limits), yet their intermediate physical states are not naturally reason-states: they are not partial symbolic commitments in a goal-directed inference. We can often specify governing equations (law-specification), but we do not get a reason-trace of the system “inferring” its later state. Optical computation shows a similar pattern. Optical systems compute transforms through propagation and interference, and intermediate electromagnetic field configurations typically do not decompose into semantically stable, inspectable reason-states. Again, powerful law-specifications exist, but reason-traces generally do not.

Energy-based optimization sits on a boundary. Physical relaxations in an energy landscape (analog optimizers, certain recurrent networks, annealing dynamics) sometimes support limited interpretability when coarse-grained into algorithmic variables such as candidate solution and energy value. But their fine-grained trajectories often lack stable, discrete inferential commitments. Whether such systems become Turing-rational may depend on whether a stable, semantically meaningful coarse-graining exists that supports partial evaluation and alternative realizability.

This points to an important generalization: symbolic rationality appears to be emergent. It arises when physical systems are engineered (or evolved) into regimes that sustain discrete, stable state distinctions, compositional structure, and semantically stable mappings between states and commitments. Digital computers and formal symbolic practices are paradigmatic examples. They are not the default form of physical evolution; they are special regimes.

We can now ask whether the universe itself is Turing-rational. To avoid category errors, distinguish the universe-as-total-state (the total physical state evolving under fundamental laws), local subsystems (brains, computers, organisms, laboratories), and our models (symbolic theories we construct). The claim defended here is that the universe-as-total-state is not Turing-rational, even though local subsystems can instantiate Turing-rational processes and our models can be Turing-rational representations.

Three considerations support this claim:

1. Fundamental physical state spaces are typically modeled as continuous (phase spaces, fields, Hilbert spaces), while Turing-rationality requires a privileged decomposition into discrete, semantically stable reason-states. Discretizations are possible, but they are typically observer-relative and non-unique.  
2. Turing-rationality presupposes an input–output framing: a problem specification and an output that counts as a solution. The universe-as-total-state is not naturally organized as a computation with a goal-directed inferential direction.  
3. Run-level reconstruction relies on counterfactual discriminability: varying inputs yields interpretable changes in the trace. For the universe-as-total-state, counterfactuals (“different initial conditions”) are not operationally accessible in a way that supports stable semantic mapping of “the same reason-state across worlds.”

A predictable objection is that physical laws are rational explanations. The reply is that this confuses law-specification with reason-tracing. Laws are our abductive reconstructions that make nature intelligible; they are not intermediate commitments that nature “uses” to infer its next state. Non-rationality helps enable science: because the world is not packaged with a single privileged symbolic decomposition as its own reason-trace, we can choose representations, idealize and abstract, and model at multiple levels. Scientific explanation is thus an activity of abductive reconstruction: building Turing-rational models of processes that are not themselves Turing-rational.

---

## 6. Partial Symbol Inductive Reasoning and Large Language Models
*(PSIR)*

LLMs differ from quantum and optical systems in one crucial respect: their internal representations are neither fully symbolic nor merely “raw physics.” They exhibit partial symbolic alignment learned from language. This allows them to behave in ways that strongly resemble symbolic reasoning while still typically lacking Turing-rational intermediates.

A popular critique claims LLMs merely generate statistically likely continuations and therefore do not reason. This critique often assumes Turing-rationality as the only genuine form of reasoning. Our framework enables a sharper diagnosis. The issue is not stochasticity, since stochastic procedures can be rational when intermediate commitments are interpretable; the issue is the absence of stable symbolic commitments that bind and justify progress across steps. LLMs can produce impressive reasoning-like behavior while lacking Turing-rational intermediates.

A useful schematic model represents an LLM as \( S=(\Sigma, X, \iota, F, \pi) \), where:

- \( \Sigma \) is a discrete token vocabulary providing the symbolic interface  
- \( X \) is a high-dimensional latent state space  
- \( \iota:\Sigma^*\to X \) is an encoding/embedding map  
- \( F:X\to X \) is a learned update operator (stacked transformer layers)  
- \( \pi:X\to \Delta(\Sigma) \) maps latents to next-token distributions  

Structurally, inputs and outputs are symbolic, but intermediate states are latent and distributed, and those states are not stable symbolic commitments.

Despite this, LLM representations often preserve patterns correlated with symbolic structure, including compositional regularities, analogical mappings, entailment-like tendencies, and constraint-sensitive generation. However, these regularities are typically context-dependent, approximate, and not guaranteed to correspond to discrete commitments. On the reason-state tests, interpretability is partial and fragile; alternative realizability is weak; and compositional evaluability is weak because there is no clear mid-computation criterion for a “partially correct” activation pattern. On run-level reconstruction, chains-of-thought rendered as text are not reliable evidence of internal reason-traces, since they are themselves products of the same latent dynamics they purport to report.

These observations motivate a distinct category: **Partial Symbol Inductive Reasoning (PSIR).**

**Definition (PSIR).**  
A system performs **PSIR** when it has symbolic interfaces (symbolic inputs and outputs), its internal dynamics are non-symbolic (continuous or distributed latent states), those dynamics exhibit partial alignment with symbolic relations learned inductively, and its behavior is best modeled as abductive continuation under learned constraints rather than as explicit rule-following.

PSIR explains why LLMs can be both powerful and brittle: they can approximate symbolic inference without possessing symbolic commitments that enforce global validity.

### Table 2: Comparison of paradigms

| Feature | Quantum | Optical | LLMs (PSIR) | Classical symbolic |
|---|---|---|---|---|
| Intermediate states | quantum amplitudes | fields | latent activations | symbolic structures |
| Symbolic alignment | none | none | partial (learned) | explicit (designed) |
| Symbol production | at end | at end | sequential tokens | varied |
| Reason-trace | typically none | typically none | typically none | typically yes |
| Failure mode | opacity | opacity | fluent unjustified outputs | traceable errors |

---

## 7. Hallucination as Abductive Explainability Failure

PSIR predicts a characteristic failure mode: fluent, locally coherent outputs that lack global justificatory support. Hallucination is often defined as factual incorrectness or unfaithfulness to a source. These are useful operational notions, but they do not capture the deeper epistemic issue: justification. A claim can be correct yet unjustified, or incorrect yet justified under a false theory. This is why factual incorrectness alone does not capture the relevant defect.

We therefore define hallucination in abductive terms.

**Definition (Hallucination relative to a hypothesis language).**  
Let \(P\) be premises, \(c\) a conclusion, and \(L_\Gamma\) a hypothesis language of candidate constraints. The conclusion \(c\) is a **hallucination** (relative to \(L_\Gamma\)) iff no constraint set \( \Gamma \subseteq L_\Gamma \) exists such that:

1. **Necessity:** \( \Gamma \cup P \models c \), and  
2. **Consistency:** \( \Gamma \cup P \) is consistent.

On this view, hallucination is failure of abductive justification, not merely error. The definition also clarifies why PSIR systems can hallucinate fluently. When constraints are sparse, PSIR systems tend to continue generating because local coherence remains rewarded; they preserve syntax and discourse structure because language constraints are strong; they drift semantically because evidential constraints are weak; and they produce plausible but unsupported continuations.

The abductive account predicts that hallucination should correlate with constraint availability. Adding grounding constraints such as retrieval, tools, or explicit sources should reduce hallucination; iterative checking should reduce semantic drift; and stronger external verification should reduce unsupported claims. These expectations align with many reported empirical patterns, but the framework’s point is structural: even with improvement, PSIR systems lack the internal symbolic commitments that would make hallucination impossible in principle.

Humans exhibit related phenomena under constraint sparsity (memory confabulation, motivated reasoning). The key difference is that humans sometimes deploy meta-cognitive monitoring: uncertainty expression, source tracking, and consistency checks. PSIR systems can approximate such monitoring only via external scaffolding—precisely what the next section develops.

---

## 8. Theory Recovery and Rational Scaffolding

If PSIR systems cannot supply internal reason-traces, we can still impose rational structure externally by recovering symbolic constraints that explain and regulate behavior. The abductive definition of hallucination suggests a direct engineering response: diagnose an output as hallucinatory when no abductive theory justifies it, then attempt to recover a justifying theory and use the recovered theory as a guardrail.

We define abductive explanations as symbolic constraint sets that make the conclusion necessary given the premises, remain consistent, and are minimal under an appropriate simplicity criterion.

**Definition (Abductive explanation).**  
Given premises \(P\), a system-produced conclusion \(c\), and hypothesis language \(L_\Gamma\), an **abductive explanation** is a constraint set \( \Gamma \subseteq L_\Gamma \) such that:

1. \( \Gamma \cup P \models c \) (**necessity**),  
2. \( \Gamma \cup P \) is consistent, and  
3. \( \Gamma \) is minimal under an appropriate simplicity criterion.

These theories are normative: they justify outputs publicly; they need not mirror internal mechanism. The practical problem is how to find such \( \Gamma \) automatically. **Counterexample-Guided Inductive Synthesis (CEGIS)** offers a general method for searching a hypothesis language \(L_\Gamma\) by alternating between proposing a candidate theory that fits observed behavior and refining that theory using counterexamples that reveal overgeneralization.

### Algorithm 1: CEGIS for abductive theory recovery (schematic)

1. **Collect examples:** Positive examples \(E^+ = \{(P_i, c_i)\}\) from system behavior.  
2. **Synthesize** a candidate \( \Gamma \) such that for all \( (P_i, c_i) \in E^+ \), \( \Gamma \cup P_i \models c_i \).  
3. **Validate** by searching for counterexamples \( (P, c') \) that should be excluded but are not excluded by \( \Gamma \).  
4. **If counterexamples are found,** add them to a negative set \(E^-\) and refine \( \Gamma \) to exclude them while preserving \(E^+\).  
5. **Repeat** until no counterexamples are found or the search fails.

A simple example illustrates the approach. Suppose an LLM is asked:

> **If \(x + 3 = 7\), what is \(2x\)?**

In many contexts, it outputs 8, but it may also output plausible alternatives (10 or 14), and it may drift under iterative use of its own intermediate results. The issue is not merely correctness but whether an abductive constraint set can be recovered that makes \(2x = 8\) necessary.

A CEGIS loop can search an arithmetic hypothesis language capable of expressing simple algebraic implications and identities. A candidate such as

\[
\Gamma_3 = \{ x+3=7 \rightarrow x=4,\ 2x = 2\cdot x,\ 2\cdot 4 = 8 \}
\]

suffices: \( \Gamma_3 \cup \{x+3=7\} \models 2x=8 \), and counterexamples like \(2x=10\) and \(2x=14\) are excluded.

Once recovered, \( \Gamma \) can serve as external rational scaffolding in several patterns:

- **Validation:** filter candidate answers not entailed by \( \Gamma \cup P \).  
- **Guidance:** bias decoding away from theory-violating continuations.  
- **Pruning:** eliminate inconsistent hypothesis families in multi-step generation.  
- **Repair loops:** violations trigger targeted regeneration conditioned on an explanation of the constraint failure.

```python
def generate_with_validation(model, prompt, theory, n=10):
    candidates = model.generate(prompt, n=n)
    valid = [c for c in candidates if theory.entails(prompt, c)]
    return valid[0] if valid else None

def theory_guided_search(refine_step, initial, theory, max_steps=10):
    candidates = initial
    for _ in range(max_steps):
        candidates = [c for c in candidates if theory.consistent(c)]
        if len(candidates) <= 1:
            return candidates[0] if candidates else None
        candidates = refine_step(candidates)
    return candidates[0] if candidates else None

def generate_with_refinement(model, prompt, theory, max_rounds=5):
    output = model.generate(prompt)
    rounds = 0
    while not theory.entails(prompt, output) and rounds < max_rounds:
        violation = theory.explain_violation(prompt, output)
        output = model.generate(prompt + "\n\nConstraint violation:\n" + violation)
        rounds += 1
    return output

```

The result is not that the underlying model becomes internally Turing-rational, but that the **overall system** becomes **publicly justifiable** in a Turing-rational way. This is **prosthetic rationality**: internal inference remains non-symbolic and non-traceable, but outputs are constrained by publicly inspectable commitments. Such scaffolding is compatible with black-box systems because it operates at the symbolic interface (inputs/outputs) and does not require access to hidden states, gradients, or training data.

**Limitations remain:**
- CEGIS may struggle with scalability.
- Abductive explanation is underdetermined (theory choice matters).
- Stochastic behavior complicates counterexample refinement.
- Designing hypothesis languages \(L_\Gamma\) is itself a representational choice.
- Composing recovered theories requires conflict detection and resolution.

These are not peripheral inconveniences; they reflect the deeper point that **justification is always relative to representational resources**.

---

## 9. Conclusion

This paper separates two questions that are often conflated:

1. **What can be computed at all**, and  
2. **What can be rationally explained as symbolic inference under a reason-trace**.

We introduced **Turing-rationality** as abductive reconstructibility into **reason-states** and **reason-traces**, and argued that many powerful computational systems—quantum, optical, continuous dynamical, and PSIR systems—can compute without being Turing-rational.

We then characterized LLMs as **PSIR systems**: symbol-producing reasoners whose internal dynamics preserve partial symbolic structure without implementing discrete commitments. This makes possible both their success and their signature failure mode: **hallucination**, understood here as abductive explainability failure relative to a hypothesis language.

Finally, we argued that non-Turing-rational systems can be made practically reliable via **external rational scaffolding**: recover explicit symbolic constraints using CEGIS, then use those constraints as guardrails for validation, guidance, stabilization, and accumulation.

The cosmological endpoint generalizes the moral: the universe is not Turing-rational. Symbolic reasons are not written into nature; they are abductive achievements of local systems—brains, cultures, and machines—that carve discrete, compositional structure out of a continuous world.

> **Rationality is not fundamental. It is built, maintained, and repaired.**

---

# Appendix A. Toy CEGIS Runs for Abductive Theory Recovery

This appendix reports a small suite of toy runs demonstrating the CEGIS-style recovery described in Section 8. The purpose is not to claim empirical performance on realistic theorem-proving or synthesis benchmarks, but to make two points concrete:

1. **Resource- and language-relativity (engineering reading).** Whether an output is “justified” depends on what hypothesis language \(L_\Gamma\) is available and what verification resources are used to search it.
2. **Recovered guardrails can introduce explicit intermediate commitments.** Even when the underlying system is treated as a black box, the recovered \(\Gamma\) can supply a public, symbolic reason-trace at the interface level.

---

## A.1 Setup

We use a minimal symbolic term language with variables, integer constants, addition and multiplication terms, equalities, and Horn-style implication rules of the form `Eq -> Eq`. The verifier \(V\) is a toy forward-chaining entailment procedure that repeatedly applies rules whose antecedents are present, together with a lightweight transitivity step (not a full congruence closure). Consistency is defined syntactically: \(\Gamma \cup P\) is inconsistent iff the derived closure contains an equality `Const(a) = Const(b)` with \(a \neq b\).

Each run uses:

- Premises: \(P = \{x + a = b\}\)
- Target conclusion: \(c_{\text{true}}\) of the form \(kx = k(b-a)\)
- A hypothesis language \(H\) containing:
  - a rule encoding the intermediate commitment (solve for \(x\)): \((x+a=b)\rightarrow(x=b-a)\)
  - a rule encoding the downstream consequence: \((x=b-a)\rightarrow(kx=k(b-a))\)
  - and several “bad” candidate rules that would justify specified wrong conclusions.

CEGIS searches for a minimal \(\Gamma \subseteq H\) (by cardinality) such that \(V\) certifies \(\Gamma \cup P \models c_{\text{true}}\) and \(V\) does not certify entailment of designated wrong conclusions.

---

## A.2 Eight-run suite

| Run | Premise \(P\) | Target \(c_{\text{true}}\) | \(|H|\) | \(|\Gamma|\) | iters | neg | status |
|---|---|---:|---:|---:|---:|---:|---|
| E1 | \(x+3=7\)  | \(2x=8\)  | 6 | 2 | 1 | 0 | OK |
| E2 | \(x+5=12\) | \(2x=14\) | 6 | 2 | 1 | 0 | OK |
| E3 | \(x+1=9\)  | \(3x=24\) | 6 | 2 | 1 | 0 | OK |
| E4 | \(x+4=11\) | \(3x=21\) | 6 | 2 | 1 | 0 | OK |
| E5 | \(x+6=20\) | \(2x=28\) | 6 | 2 | 1 | 0 | OK |
| E6 | \(x+2=10\) | \(4x=32\) | 6 | 2 | 1 | 0 | OK |
| E7 | \(x+7=19\) | \(3x=36\) | 6 | 2 | 1 | 0 | OK |
| E8 | \(x+8=23\) | \(2x=30\) | 6 | 2 | 1 | 0 | OK |

---

## A.3 Recovered guardrails and intermediate commitments

In each run, the recovered guardrail \(\Gamma\) contains exactly two implications:

\[
(x+a=b)\rightarrow(x=b-a),
\qquad
(x=b-a)\rightarrow(kx=k(b-a)).
\]

For example, in run E1 CEGIS recovers:

\[
(x+3=7)\rightarrow(x=4),
\qquad
(x=4)\rightarrow(2x=8).
\]

These are run-appropriate symbolic commitments: the first rule introduces an intermediate commitment about \(x\) that is interpretable in the problem domain, and the second rule propagates that commitment to the target claim. This is the sense in which theory recovery can provide a **public reason-trace** at the symbolic interface.

---

## A.4 Interpretation: language-relativity and minimality

The suite illustrates the engineering relativity emphasized in Section 7. The recovered guardrail depends on the available hypothesis language \(L_\Gamma\) and on the verifier \(V\). Under a different \(L_\Gamma\) (e.g., one with more general algebraic rewrite rules), the recovered \(\Gamma\) might be more reusable across tasks or require more steps to derive \(c_{\text{true}}\). “Justification” in this engineering sense is not absolute: it is a property of \((V, L_\Gamma)\).

---

## A.5 Reproducibility

The reference implementation for the term language, closure-based verifier, and CEGIS loop used in this repository.

