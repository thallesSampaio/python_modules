import math


def parse_coordinate(coord_str: str) -> tuple[int, int, int]:
    """Converts a comma-separated string into a 3D tuple."""
    try:
        parts: list[str] = coord_str.split(",")
        return (int(parts[0]), int(parts[1]), int(parts[2]))
    except ValueError as e:
        print(f"Error parsing coordinates: {e}")
        print(f"Error details - Type: {type(e).__name__}, Args: {e.args}")


def get_distance(p1: tuple[int, int, int], p2: tuple[int, int, int]) -> float:
    x1, y1, z1 = p1
    x2, y2, z2 = p2
    return float(math.sqrt((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2))


def show_unpacking(p: tuple[int, int, int]) -> None:
    x, y, z = p
    print(f"Player at x={x}, y={y}, z={z}")
    print(f"Coordinates: X={x}, Y={y}, Z={z}")


def main() -> None:
    print("=== Game Coordinate System ===")

    origin: tuple[int, int, int] = (0, 0, 0)
    p1: tuple[int, int, int] = (10, 20, 5)
    print(f"\nPosition created: {p1}")
    dist1: float = get_distance(origin, p1)
    print(f"Distance between {origin} and {p1}: {dist1:.2f}")

    coord_input: str = "3,4,0"
    print(f"\nParsing coordinates: \"{coord_input}\"")
    p2: tuple[int, int, int] = parse_coordinate(coord_input)
    print(f"Parsed position: {p2}")
    dist2: float = get_distance(origin, p2)
    print(f"Distance between {origin} and {p2}: {dist2:.2f}")

    invalid_input: str = "abc,def,ghi"
    print(f"\nParsing invalid coordinates: \"{invalid_input}\"")
    parse_coordinate(invalid_input)

    print("\nUnpacking demonstration:")
    parsed_pos = parse_coordinate(coord_input)
    show_unpacking(parsed_pos)


if __name__ == "__main__":
    main()
