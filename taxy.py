def delta_s(coord_D: int, coord_0: int, coord_1: int) -> int:
    delta = 0
    if coord_D < coord_0:
        delta = coord_0 - coord_D
    elif coord_0 <= coord_D < coord_1:
        delta = 0
    elif coord_1 <= coord_D:
        delta = coord_D - (coord_1 - 1)
    return delta


def main():
    with open('input.txt', 'r') as file:
        info = file.readlines()

        K, D = list(map(lambda x: int(x), info[2].split()))
        available_cars = list(map(lambda x: int(x), info[3].split()))
        if K <= D:
            demand_zone = info[1].split()

            x0, y0, x1, y1 = map(lambda x: int(x), demand_zone)
            available_cars_coords = list(zip(available_cars[::2], available_cars[1::2]))
            cars_times = []
            for i in available_cars_coords:
                time = delta_s(i[0], x0, x1) + delta_s(i[1], y0, y1)
                cars_times.append(time)

            cars_times.sort()
            return max(cars_times[:K])
        else:
            return -1


if __name__ == '__main__':
    print(main())
