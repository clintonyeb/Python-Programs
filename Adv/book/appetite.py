def pressure(v, t, n):
    """Computes the pressure in paschals of an ideal gas
    v -- volume of gas
    t -- absolute temperature of gas
    n -- particle of gas
    """
    k = 1.38e-23  # Boltzmann's constant
    return n * k * t / v


def sum_naturals(n):
    total, k = 0, 1
    while k <= n:
        total, k = total + k, k + 1
    return total


def sum_cubes(n):
    total, k = 0, 1
    while k <= n:
        total, k = total + k * k * k, k + 1
    return total


def pi_sum(n):
    total, k = 0, 1
    while k <= n:
        total, k = total + 8 / ((4 * k - 3) * (4 * k - 1)), k + 1
    return total


def summation(n, term):
    total, k = 0, 1
    while k <= n:
        total, k = total + term(k), k + 1
    return total


def cube(x):
    return x * x * x


def sum(x):
    return x


def sum_pi(x):
    return 8 / ((4 * x - 3) * (4 * x - 1))

def improve(update, close, guess=1):
    while not close(guess):
        guess = update(guess)
    return guess

def golden_update(guess):
    return 1/guess + 1

def approx_eq(x, y, tolerance=1e-15):
    return abs(x-y) < tolerance

def square_close_to_successor(guess):
    return approx_eq(guess* guess, guess + 1)
