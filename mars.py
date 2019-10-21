def main():
    with open('input.txt', 'r') as file:
        promo_len = int(file.readline())
        promo = file.readline()
        key_len = int(file.readline())
        keys = [file.readline()]
        L = int(file.readline())

        parts = []
        for i in range((promo_len // L)):
            parts.append(promo[L * i:L * (i + 1)])

        count = 0
        for part in parts:
            for key in keys:
                if part in key:
                    pos_key = key.find(part)
                    keys.append(key[:pos_key])
                    keys.append(key[pos_key + L:])
                    del key
                    count += 1
        if count == len(parts):
            return "YES"
        else:
            return "NO"


if __name__ == '__main__':
    print(main())
