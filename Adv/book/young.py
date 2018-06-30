def improve(update, close, guess=1):
    while not close(guess):
        guess = update(guess)
    return guess


def integ():
    def update(k):
        return k + 1

    def close(k):
        return (abs(k - 6) == 0)

    return improve(update, close)

def app_eq(x, y, tolerance=1e-15):
        return abs(x - y) < tolerance

def golden_ratio():
    def update(k):
        return 1 / k + 1

    def close(k):
        return app_eq(k * k, k + 1)

    return improve(update, close)

