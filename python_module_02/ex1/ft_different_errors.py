def garden_operations():
    def v_error() -> None:
        int("abc")

    def z_error() -> None:
        10 / 0

    def f_error() -> None:
        open("missing.txt")

    def k_error() -> None:
        {"tomato": 5}["missing_plant"]

    return v_error, z_error, f_error, k_error


def test_error_types() -> None:
    v_error, z_error, f_error, k_error = garden_operations()

    try:
        print("Testing ValueError...")
        v_error()
    except ValueError:
        print("Caught ValueError: invalid literal for int()\n")

    try:
        print("Testing ZeroDivisionError...")
        z_error()
    except ZeroDivisionError:
        print("Caught ZeroDivisionError: division by zero\n")

    try:
        print("Testing FileNotFoundError...")
        f_error()
    except FileNotFoundError:
        print("Caught FileNotFoundError: No such file 'missing.txt'\n")

    try:
        print("Testing KeyError...")
        k_error()
    except KeyError:
        print("Caught KeyError: 'missing\\_plant'\n")

    try:
        print("Testing multiple errors together...")
        v_error()
        z_error()
        f_error()
        k_error()
    except (ValueError, ZeroDivisionError, FileNotFoundError, KeyError):
        print("Caught an error, but program continues!\n")


if __name__ == "__main__":
    print("=== Garden Error Types Demo ===\n")
    test_error_types()
    print("All error types tested successfully!")
