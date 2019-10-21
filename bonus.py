def main():
    with open('input.txt', 'r') as file:
        N = int(file.readline())

        ratings = [int(line) for line in file.readlines()]
        if len(ratings) >= N:
            del ratings[N:]

            bonuses = [500]
            for i in range(1, len(ratings)):
                if ratings[i - 1] < ratings[i]:
                    bonuses.append(bonuses[-1] + 500)
                # elif ratings[i - 1] == ratings[i]:
                #     bonuses.append(bonuses[-1])
                else:
                    bonuses.append(500)

            for i in range(len(ratings) - 2, -1, -1):
                if ratings[i] > ratings[i+1]:
                    bonuses[i] = max(bonuses[i + 1] + 500, bonuses[i])
                # elif ratings[i] == ratings[i+1]:
                #     bonuses[i] = bonuses[i+1]

            return sum(bonuses)


if __name__ == '__main__':
    print(main())
