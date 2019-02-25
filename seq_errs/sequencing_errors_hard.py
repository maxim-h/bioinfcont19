from math import factorial, floor
from decimal import *


def coverage_probability(b, l, n, k):
    return float(Decimal(factorial(k)) / Decimal((factorial(b)) * Decimal(factorial(k - b))) * Decimal(n ** b) * Decimal((l - n) ** (k - b)) / Decimal(l ** (k - 1)))


def calling_errors(b: int, p: float):
    def binomial_pdf(p: float, n: int, k: int):
        def binomial(n: int, k: int):
            """n: int - Amount of bernoulli trials
            k: int - Amount of successes
            """
            return factorial(n) / (factorial(k) * factorial(n - k))
        return binomial(n, k) * (p ** k) * ((1 - p) ** (n - k))

    if b % 2 == 0:
        yield 0.5 * binomial_pdf(p, b, b/2)
    for i in range(int(floor(b / 2) + 1), b + 1):

        yield 1 * binomial_pdf(p, b, i)


def error_summ(b: int, p: float, appropr_err: float):
    err = 0
    for e in calling_errors(b, p):
        err += e
        if e < appropr_err:
            #print("broke {}".format(appropr_err))
            break
    return err


def error_probability(b: int, l: int, n: int, p: float, k: int):
    cov_prob = coverage_probability(b, l, n, k)
    if b == 0:
        return cov_prob * 0.75
    else:
        return cov_prob * error_summ(b, p, 1.0e-8 / cov_prob)


def total_error_probability(l: int, n: int, p: float, k: int):
    total_error = 0
    for cov in range(0, k+1):
        e = error_probability(cov, l, n, p, k)
        total_error += e
        #print("Total error {} Error {} Coverage {}".format(total_error, e, cov))
        if e < 1.0e-8:
            break
    return total_error


with open("2.txt", "r") as tests:
    with open("results_hard.txt", "w") as res:
        n = int(tests.readline())
        results = []
        for i in range(n):
            l, n, p, k = map(float, tests.readline().strip().split())
            results.append(str(total_error_probability(int(l), int(n), float(p), int(k))))
        res.write("\n".join(results))