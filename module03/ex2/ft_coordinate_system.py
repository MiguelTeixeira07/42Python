import math


def parse_coordinates(coord_str: str) -> tuple:
    try:
        str_points = coord_str.split(',')
        if len(str_points) != 3:
            raise SyntaxError('Invalid syntax')

        for item in str_points:
            try:
                float(item)
            except ValueError as e:
                raise ValueError(f"Error on parameter '{item}': {e}")

        return *[float(point) for point in str_points],
    except ValueError as e:
        print(e)
        return ()
    except SyntaxError as e:
        print(e)
        return ()


def distance_3d(p1: tuple, p2: tuple) -> float:
    x1, y1, z1 = p1
    x2, y2, z2 = p2

    distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2)

    return round(distance, 4)


def write_coords(x: float, y: float, z: float) -> str:
    return f'x={x}, y={y}, z={z}'


def main() -> None:
    print('=== Game Coordinate System ===')

    print('\nGet a first set of coordinates')
    while 1 == 1:
        temp = input("Enter new coordinates as floats in format 'x,y,z': ")
        point1 = parse_coordinates(temp)
        if len(point1) == 3:
            break
    print('Got a first tuple', point1)
    print('It includes:', write_coords(*point1))
    print('Distance to center:', distance_3d(point1, (0, 0, 0)))

    print('\nGet a second set of coordinates')
    while 1 == 1:
        temp = input("Enter new coordinates as floats in format 'x,y,z': ")
        point2 = parse_coordinates(temp)
        if len(point2) == 3:
            break

    print('Distance between the 2 sets of coordinates: ', end='')
    print(distance_3d(point1, point2))


if __name__ == '__main__':
    main()
