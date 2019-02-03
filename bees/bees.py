
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
    for i, j in population(n1, a, b):
        if i <= 0:
            return 0
        else:
            diff_2 = i - j
            if diff_2 > diff_1:
                return -1
            else:
                diff_1 = diff_2
                if diff_1 < err:
                    return i





#print(analyzer(0.5, 1, 1))


for i in population(0.5, 1, 1):
    print(i)



# with open("tests.txt", "r") as t:
#     n = int(t.readline())
#     # for i in range(n):
#     #     print(t.readline())