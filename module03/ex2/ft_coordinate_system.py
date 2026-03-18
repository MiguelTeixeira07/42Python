import sys
import math


def parse_coordinates(coord_str) -> tuple:
    try:
        x, y, z = coord_str.split(",")
        coords = (int(x), int(y), int(z))
        print(f'Parsed position: {coords}')
        return coords
    except Exception as e:
        print(f'Error parsing coordinates: {e}')
        return None


def distance_3d(p1, p2) -> float:
    x1, y1, z1 = p1
    x2, y2, z2 = p2
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2)


def unpack(x: int, y: int, z: int) -> str:
    return f'x={x}, y={y}, z={z}'


def main() -> None:
    if len(sys.argv) != 3:
        print('Usage: python3 ft_coordinate_system.py x1,y1,z1 x2,y2,z2')
        return

    p1 = parse_coordinates(sys.argv[1])
    if p1 is None:
        return
    p2 = parse_coordinates(sys.argv[2])
    if p2 is None:
        return

    dist = distance_3d(p1, p2)
    print(f'Distance between {p1} and {p2}: {dist:.2f}')

    print(f'\nPlayer at {unpack(*p1)}')
    print(f'Coordinates: {unpack(*p2)}')


if __name__ == '__main__':
    main()
