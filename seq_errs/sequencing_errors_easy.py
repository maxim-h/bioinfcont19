from math import factorial, floor



def coverage_probability(b: int, l: int, n: int, k: int):
    return factorial(k) / (factorial(b) * factorial(k - b)) * n ** b * (l - n) ** (k - b) / l ** (k - 1)


def sequencing_errors(b: int, p: float):
    if b % 2 == 0:
        yield 0.5 * p ** (b / 2)
    for i in range(int(floor(b / 2) + 1), b + 1):
        yield p ** i


def error_summ(b: int, p: float, appropr_err: float):
    err = 0
    for e in sequencing_errors(b, p):
        err += e
        if e < appropr_err:
            print("broke {}".format(appropr_err))
            break
    return err


def error_probability(b: int, l: int, n: int, p: float, k: int):
    cov_prob = coverage_probability(b, l, n, k)
    if b == 0:
        return cov_prob * 0.75
    else:
        return cov_prob * error_summ(b, p, 1.0e-9)


def total_error_probability(l: int, n: int, p: float, k: int):
    total_error = 0
    for cov in range(0, k+1):
        e = error_probability(cov, l, n, p, k)
        total_error += e
        if e < 1.0e-10:
            break
    return total_error




print(total_error_probability(10, 3, 0.05, 4))

print(error_probability(0, 10, 3, 0.05, 4))

