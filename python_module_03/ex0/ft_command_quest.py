import sys


def main() -> None:
    try:
        print("=== Command Quest ===")
        argc: int = len(sys.argv)
        if argc == 1:
            print("No arguments provided!")
            print(f"Program name: {sys.argv[0]}")
            print(f"Total arguments: {argc}")
        elif argc > 1:
            print(f"Program name: {sys.argv[0]}")
            print(f"Arguments received: {argc - 1}")
            i: int = 1
            while i < argc:
                print(f"Argument {i}: {sys.argv[i]}")
                i += 1
        print(f"Total arguments: {argc}")
    except Exception as e:
        print(f"Fatal error: {e}")


if __name__ == "__main__":
    main()
