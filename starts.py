import itertools


def D(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1]) + abs(a[2] - b[2])


def perm(first, second):
    n = len(second)
    for x in itertools.permutations(first, n):
        yield zip(x, second)


def main():
    file = open('input.txt', 'r')
    N = int(file.readline())
    first = []
    second = []
    for i in range(N):
        first.append(list(map(int, file.readline().split())))
    for i in range(N):
        second.append(list(map(int, file.readline().split())))
    file.close()
    mins = []
    for i in perm(first, second):
        sum_d = 0
        for j in i:
            sum_d += D(j[0], j[1])
        mins.append(sum_d)

    return min(mins)


if __name__ == '__main__':
    print(main())
