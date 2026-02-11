import math

def f1(x): return math.sin(x)
def f2(x): return x**2 + 3*x + 2
def f3(x): return math.exp(x)
def f4(x): return math.sqrt(x)
def f5(x): return x**4 - 2*x**3 + x**2 + x + 1


def trapezoidal(f, a, b, n):
    h = (b - a) / n
    s = f(a) + f(b)
    for i in range(1, n):
        x = a + i*h
        s += 2 * f(x)
    return (h/2) * s


def simpson_one_third(f, a, b, n):
    if n % 2 != 0:
        raise ValueError("Simpson 1/3: n must be even")
    h = (b - a) / n
    s = f(a) + f(b)
    for i in range(1, n):
        x = a + i*h
        if i % 2 == 0:
            s += 2 * f(x)
        else:
            s += 4 * f(x)
    return (h/3) * s


def simpson_three_eight(f, a, b, n):
    if n % 3 != 0:
        raise ValueError("Simpson 3/8: n must be divisible by 3")
    h = (b - a) / n
    s = f(a) + f(b)
    for i in range(1, n):
        x = a + i*h
        if i % 3 == 0:
            s += 2 * f(x)
        else:
            s += 3 * f(x)
    return (3*h/8) * s


def boole_rule(f, a, b, n):
    if n % 4 != 0:
        raise ValueError("Boole: n must be divisible by 4")
    h = (b - a) / n
    s = 0
    for i in range(0, n+1):
        x = a + i*h
        if i == 0 or i == n:
            s += 7 * f(x)
        elif i % 2 == 1:
            s += 32 * f(x)
        elif i % 4 == 2:
            s += 12 * f(x)
        else:
            s += 14 * f(x)
    return (2*h/45) * s


def show_result(name, approx, exact):
    abs_err = abs(exact - approx)
    if exact != 0:
        rel_err = abs_err / abs(exact) * 100
        print(f"{name}: approx = {approx:.10f} | abs_err = {abs_err:.10f} | rel_err = {rel_err:.6f}%")
    else:
        print(f"{name}: approx = {approx:.10f} | abs_err = {abs_err:.10f} | rel_err = N/A (exact=0)")


# Task 1: ∫ sin(x) dx от 0 до pi/2 = 1
a, b, n = 0, math.pi/2, 10
exact = 1.0
print("Task 1: integral sin(x) [0, pi/2]")
show_result("Trapezoidal", trapezoidal(f1, a, b, n), exact)
show_result("Simpson 1/3", simpson_one_third(f1, a, b, n), exact)
print()

# Task 2: ∫ (x^2 + 3x + 2) dx от 1 до 5
# точный: [x^3/3 + 3x^2/2 + 2x]1^5
def exact_f2(a, b):
    F = lambda x: x**3/3 + 3*x**2/2 + 2*x
    return F(b) - F(a)

a, b = 1, 5
exact = exact_f2(a, b)
print("Task 2: integral (x^2+3x+2) [1,5]")
show_result("One trapezoid (n=1)", trapezoidal(f2, a, b, 1), exact)
show_result("Trapezoidal (n=4)", trapezoidal(f2, a, b, 4), exact)
print()

# Task 3: ∫ e^x dx от 0 до 2 = e^2 - 1
a, b = 0, 2
exact = math.e**2 - 1
print("Task 3: integral e^x [0,2]")
show_result("Simpson 1/3 (n=2)", simpson_one_third(f3, a, b, 2), exact)
show_result("Simpson 1/3 (n=4)", simpson_one_third(f3, a, b, 4), exact)
print()

# Task 4: ∫ sqrt(x) dx от 0 до 3 = (2/3)*x^(3/2) |0..3 = 2*sqrt(3)
a, b = 0, 3
exact = 2 * math.sqrt(3)
print("Task 4: integral sqrt(x) [0,3]")
show_result("Simpson 3/8 (n=3)", simpson_three_eight(f4, a, b, 3), exact)
show_result("Simpson 3/8 (n=6)", simpson_three_eight(f4, a, b, 6), exact)
print()

# Task 5: ∫ (x^4 - 2x^3 + x^2 + x + 1) dx от 0 до 4
# точный: [x^5/5 - x^4/2 + x^3/3 + x^2/2 + x]0..4 = 1652/15
a, b = 0, 4
exact = 1652/15
print("Task 5: integral polynomial [0,4]")
show_result("Boole (n=4)", boole_rule(f5, a, b, 4), exact)