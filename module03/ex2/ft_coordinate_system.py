import sys
import math


def parse_coordinates(coord_str) -> None:
    try:
        x, y, z = coord_str.split(",")
        return (int(x), int(y), int(z))
    except Exception as e:
        print(f"Error parsing coordinates: {e}")
        return None


def distance_3d(p1, p2) -> float:
    x1, y1, z1 = p1
    x2, y2, z2 = p2
    return math.sqrt(
        (x2 - x1) ** 2 +
        (y2 - y1) ** 2 +
        (z2 - z1) ** 2
    )


def main() -> None:
    if len(sys.argv) != 3:
        print("Usage: python3 ft_coordinate_system.py x1,y1,z1 x2,y2,z2")
        return

    p1 = parse_coordinates(sys.argv[1])
    p2 = parse_coordinates(sys.argv[2])

    if p1 is None or p2 is None:
        return

    dist = distance_3d(p1, p2)
    print(dist)


if __name__ == "__main__":
    main()
