
err = 1.0e-10

def population(n1, a, b):
    i = 0
    previous = 0
    while True:
        if i == 0:
            yield (n1, 0)
            previous = n1
            i += 1
        else:
            next = a*previous - b*previous*previous
            yield (next, previous)
            previous = next
            i += 1

def analyzer(n1, a, b):
    diff_1 = n1
    iterations = 0
    for i, j in population(n1, a, b):
        iterations += 1
        if i <= 0:
            return (0, iterations)
        else:
            diff_2 = abs(i - j)
            if diff_2 > diff_1:
                return (-1, iterations)
            else:
                diff_1 = diff_2
                if diff_1 < err:
                    return (round(i, 8), iterations)





# print(analyzer(0.5, 1, 1))

# c = 0
# for i in population(0.5, 1, 1):
#     print(i)
#     if c == 10:
#         break
#     c += 1



with open("tests.txt", "r") as t:
    with open("results.txt", "w") as res:
        n = int(t.readline())
        results = []
        for i in range(n):
            n, a, b = map(float, t.readline().strip().split())
            results.append(str(analyzer(n, a, b)[0]))
        res.write("\n".join(results))
