def get_pr(x, pr):
    max_k = sorted(pr, key=lambda x: x[0], reverse=True)[0][0]
    if x > max_k:
        return -1
    return max(list(filter(lambda k: k[0] == x, pr)), key=lambda x: x[1])


def get_opt(curr, ust, price, K, total):
    tt = get_pr(curr, price)
    if tt != -1:
        if len(tt) == 0:
            curr += 1
            ust = 0 if ust == 0 else ust - 1
            return get_opt(curr, ust, price, K, total)
        else:
            if ust <= K:
                curr += tt[1]
                ust += tt[1] * 2
                total += tt[1]
                return get_opt(curr, ust, price, K, total)
            else:
                curr += ust - K
                ust = K
                return get_opt(curr, ust, price, K, total)
    return total


def main():
    file = open('input.txt', 'r')
    N, K = list(map(int, file.readline().split()))
    pr = []
    for i in range(N):
        pr.append(list(map(int, file.readline().split())))
    total = 0
    total = get_opt(0, 0, pr, K, total)
    return  total

if __name__ == '__main__':
    print(main())
