from __future__ import annotations
from dataclasses import dataclass
from itertools import combinations
from typing import List, Optional, Sequence, Set, Tuple


# ----------------------------
# Tiny term language (purely symbolic)
# ----------------------------

@dataclass(frozen=True)
class Term:
    pass

@dataclass(frozen=True)
class Var(Term):
    name: str

@dataclass(frozen=True)
class Const(Term):
    value: int

@dataclass(frozen=True)
class Add(Term):
    a: Term
    b: Term

@dataclass(frozen=True)
class Mul(Term):
    a: Term
    b: Term

@dataclass(frozen=True)
class Eq:
    left: Term
    right: Term

@dataclass(frozen=True)
class Imp:
    """Horn-style symbolic rule: if ant holds (syntactically), then cons holds."""
    ant: Eq
    cons: Eq


# ----------------------------
# Pretty printing
# ----------------------------

def term_str(t: Term) -> str:
    if isinstance(t, Var):
        return t.name
    if isinstance(t, Const):
        return str(t.value)
    if isinstance(t, Add):
        return f"({term_str(t.a)}+{term_str(t.b)})"
    if isinstance(t, Mul):
        return f"({term_str(t.a)}*{term_str(t.b)})"
    raise TypeError(t)

def eq_str(e: Eq) -> str:
    return f"{term_str(e.left)} = {term_str(e.right)}"

def imp_str(r: Imp) -> str:
    return f"{eq_str(r.ant)}  ->  {eq_str(r.cons)}"


# ----------------------------
# Symbolic derivation engine
# ----------------------------

def normalize_eq(e: Eq) -> Eq:
    # canonicalize equality by sorting string forms (cheap canonicalization)
    a, b = term_str(e.left), term_str(e.right)
    return e if a <= b else Eq(e.right, e.left)

def closure(P: Sequence[Eq], Gamma: Sequence[Imp], max_steps: int = 1000) -> Set[Eq]:
    """
    Compute the closure of derived equalities starting from P,
    applying rules whose antecedent equality is present.
    Also closes under symmetry (via normalization) and transitivity on identical terms.
    """
    derived: Set[Eq] = set(normalize_eq(e) for e in P)

    # Very lightweight transitive closure: if (A=B) and (B=C), add (A=C).
    # This is not a full congruence closure (deliberately toy).
    def add_transitives() -> bool:
        added = False
        eqs = list(derived)
        for e1 in eqs:
            for e2 in eqs:
                if term_str(e1.right) == term_str(e2.left):
                    new = normalize_eq(Eq(e1.left, e2.right))
                    if new not in derived:
                        derived.add(new)
                        added = True
        return added

    steps = 0
    changed = True
    while changed and steps < max_steps:
        steps += 1
        changed = False

        # apply implication rules
        for r in Gamma:
            ant = normalize_eq(r.ant)
            cons = normalize_eq(r.cons)
            if ant in derived and cons not in derived:
                derived.add(cons)
                changed = True

        # apply cheap transitivity
        if add_transitives():
            changed = True

    return derived

def consistent(P: Sequence[Eq], Gamma: Sequence[Imp]) -> bool:
    """
    Consistent if closure does not contain a contradiction of the form Const(a)=Const(b) with a!=b.
    """
    derived = closure(P, Gamma)
    for e in derived:
        if isinstance(e.left, Const) and isinstance(e.right, Const):
            if e.left.value != e.right.value:
                return False
    return True

def entails(P: Sequence[Eq], Gamma: Sequence[Imp], c: Eq) -> bool:
    """
    Derivability-based entailment: Gamma ∪ P ⊢ c iff c is in the derived closure.
    """
    derived = closure(P, Gamma)
    return normalize_eq(c) in derived


# ----------------------------
# Synthesis + CEGIS
# ----------------------------

def synthesize_minimal(
    E_pos: Sequence[Tuple[Sequence[Eq], Eq]],
    E_neg: Sequence[Tuple[Sequence[Eq], Eq]],
    H: Sequence[Imp],
) -> Optional[List[Imp]]:
    """
    Find minimal Gamma subset of H (by cardinality) s.t.:
      - For all (P,c) in E_pos: consistent(P,Gamma) and entails(P,Gamma,c)
      - For all (P,c_bad) in E_neg: NOT entails(P,Gamma,c_bad)
    """
    for k in range(len(H) + 1):
        for subset in combinations(H, k):
            Gamma = list(subset)

            ok = True
            for P, c in E_pos:
                if not consistent(P, Gamma):
                    ok = False
                    break
                if not entails(P, Gamma, c):
                    ok = False
                    break
            if not ok:
                continue

            for P, c_bad in E_neg:
                if entails(P, Gamma, c_bad):
                    ok = False
                    break
            if not ok:
                continue

            return Gamma
    return None

def cegis_recover(
    P: Sequence[Eq],
    c_true: Eq,
    H: Sequence[Imp],
    wrong_conclusions: Sequence[Eq],
    max_iters: int = 50,
) -> Tuple[Optional[List[Imp]], List[Tuple[Sequence[Eq], Eq]], int]:
    """
    Returns (Gamma, E_neg, iters_used)
    """
    E_pos = [(P, c_true)]
    E_neg: List[Tuple[Sequence[Eq], Eq]] = []

    iters_used = 0
    for _ in range(max_iters):
        iters_used += 1
        Gamma = synthesize_minimal(E_pos, E_neg, H)
        if Gamma is None:
            return None, E_neg, iters_used

        # Validate: exclude any wrong conclusion that becomes derivable
        added = False
        for c_bad in wrong_conclusions:
            if entails(P, Gamma, c_bad):
                E_neg.append((P, c_bad))
                added = True
                break

        if not added:
            return Gamma, E_neg, iters_used

    return None, E_neg, iters_used


# ----------------------------
# Example generator (8 runs)
# ----------------------------

@dataclass(frozen=True)
class Example:
    name: str
    P: List[Eq]
    c_true: Eq
    H: List[Imp]
    wrong: List[Eq]

def make_linear_example(
    name: str,
    a: int,
    b: int,
    k: int,
    wrong_vals: Sequence[int],
) -> Example:
    """
    Premise: x + a = b
    Target: k*x = k*(b-a)
    Hypothesis language includes:
      - correct: (x+a=b) -> x=(b-a)
      - correct: x=(b-a) -> kx = k(b-a)
      - bad: (x+a=b) -> kx = wrong_val   (one per wrong_val)
      - bad: x=(b-a) -> kx = wrong_val   (one per wrong_val)
    """
    x = Var("x")
    v = b - a
    kv = k * v

    premise = Eq(Add(x, Const(a)), Const(b))
    P = [premise]
    c_true = Eq(Mul(Const(k), x), Const(kv))

    wrong = [Eq(Mul(Const(k), x), Const(w)) for w in wrong_vals]

    H: List[Imp] = []

    # "Helpful" rules
    H.append(Imp(premise, Eq(x, Const(v))))                      # x+a=b -> x=v
    H.append(Imp(Eq(x, Const(v)), Eq(Mul(Const(k), x), Const(kv))))  # x=v -> kx=kv

    # Some alternative helpful paths (slightly redundant, but realistic hypothesis noise)
    # Direct shortcut: x+a=b -> kx=kv
    # H.append(Imp(premise, Eq(Mul(Const(k), x), Const(kv))))

    # "Bad" rules (overfitting / hallucination-like justifications)
    for w in wrong_vals:
        H.append(Imp(premise, Eq(Mul(Const(k), x), Const(w))))
        H.append(Imp(Eq(x, Const(v)), Eq(Mul(Const(k), x), Const(w))))

    return Example(name=name, P=P, c_true=c_true, H=H, wrong=wrong)


def demo_suite() -> None:
    # 8 small variations (counterfactual-ish), same variable x
    examples = [
        make_linear_example("E1: x+3=7, 2x", a=3, b=7, k=2, wrong_vals=[10, 14]),
        make_linear_example("E2: x+5=12, 2x", a=5, b=12, k=2, wrong_vals=[12, 16]),
        make_linear_example("E3: x+1=9, 3x", a=1, b=9, k=3, wrong_vals=[21, 30]),
        make_linear_example("E4: x+4=11, 3x", a=4, b=11, k=3, wrong_vals=[15, 24]),
        make_linear_example("E5: x+6=20, 2x", a=6, b=20, k=2, wrong_vals=[24, 30]),
        make_linear_example("E6: x+2=10, 4x", a=2, b=10, k=4, wrong_vals=[28, 40]),
        make_linear_example("E7: x+7=19, 3x", a=7, b=19, k=3, wrong_vals=[27, 45]),
        make_linear_example("E8: x+8=23, 2x", a=8, b=23, k=2, wrong_vals=[24, 40]),
    ]

    print("=== CEGIS Suite (8 examples) ===\n")

    # Compact summary header
    print(f"{'Example':<18} {'|H|':>4} {'|Γ|':>4} {'iters':>5} {'neg':>4}  status")
    print("-" * 60)

    for ex in examples:
        Gamma, E_neg, iters = cegis_recover(ex.P, ex.c_true, ex.H, ex.wrong)

        status = "OK" if Gamma is not None else "FAIL"
        h_sz = len(ex.H)
        g_sz = len(Gamma) if Gamma is not None else 0
        neg_sz = len(E_neg)

        print(f"{ex.name[:18]:<18} {h_sz:>4} {g_sz:>4} {iters:>5} {neg_sz:>4}  {status}")

        # Print recovered rules and learned negatives (brief but readable)
        print("  P:", ", ".join(eq_str(p) for p in ex.P))
        print("  target:", eq_str(ex.c_true))
        if Gamma is None:
            print("  Recovered Γ: None")
        else:
            print("  Recovered Γ:")
            for r in Gamma:
                print("    ", imp_str(r))
        if E_neg:
            print("  Negatives learned:")
            for _, c_bad in E_neg:
                print("    excluded:", eq_str(c_bad))
        print()

        # Sanity checks
        if Gamma is not None:
            assert consistent(ex.P, Gamma)
            assert entails(ex.P, Gamma, ex.c_true)
            for c_bad in ex.wrong:
                assert not entails(ex.P, Gamma, c_bad)

    print("Done.")


if __name__ == "__main__":
    demo_suite()
