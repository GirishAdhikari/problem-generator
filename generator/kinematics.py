import sympy as sp
import random

s, u, v, a, t = sp.symbols("s u v a t")


# -----------------------------
# VALIDATION LAYER
# -----------------------------

def validate_eq1(u_val, a_val, t_val):
    # v = u + at (always physically valid if t > 0)
    return t_val > 0


def validate_eq2(u_val, a_val, s_val):
    # v^2 = u^2 + 2as must be ≥ 0
    inside = u_val**2 + 2 * a_val * s_val
    return inside >= 0


def validate_eq3(u_val, a_val, t_val):
    # s = ut + 1/2 at^2
    return t_val > 0


# -----------------------------
# GENERATOR (with validation loop)
# -----------------------------

def generate_eq1():
    while True:
        u_val = random.randint(0, 100)
        a_val = random.randint(-20, 20)   # allow direction
        t_val = random.randint(1, 25)

        if validate_eq1(u_val, a_val, t_val):
            eq = sp.Eq(v, u + a*t)
            eq_sub = eq.subs({u: u_val, a: a_val, t: t_val})
            ans = sp.solve(eq_sub, v)[0]

            return {"u": u_val, "a": a_val, "t": t_val}, ans


def generate_eq2():
    while True:
        u_val = random.randint(0, 100)
        a_val = random.randint(-20, 20)
        s_val = random.randint(1, 100)

        if validate_eq2(u_val, a_val, s_val):
            eq = sp.Eq(v**2, u**2 + 2*a*s)
            eq_sub = eq.subs({u: u_val, a: a_val, s: s_val})

            solutions = sp.solve(eq_sub, v)

            # pick physically meaningful solution (optional refinement later)
            ans = solutions

            return {"u": u_val, "a": a_val, "s": s_val}, ans


# -----------------------------
# RUN EXAMPLE
# -----------------------------

inputs, answer = generate_eq2()

print("Given:")
for k, v in inputs.items():
    print(f"{k} = {v}")

print("\nAnswer:", answer)