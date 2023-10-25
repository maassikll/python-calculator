from sympy import symbols, diff, integrate, simplify


def calcul_derivee(fn):
    x = symbols('x')
    expression = simplify(fn)
    derivee = diff(expression, x)
    return derivee

def calcul_integrale(fn):
    x = symbols('x')
    expression = simplify(fn)
    integrale = integrate(expression, x)
    return integrale



