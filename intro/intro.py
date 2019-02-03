
with open("input.txt", "r") as t:
    n = int(t.readline())
    with open("output.txt", "w") as o:
        o.write("\n".join([str(sum(map(int, t.readline().strip().split()))) for i in range(n)]))