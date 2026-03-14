import sys
import os
import site


def outside_venv() -> None:
    print("MATRIX STATUS: You're still plugged in\n")
    print(f"Current Python: {sys.executable}.11")
    print("Virtual Enviroment: None detected\n")

    print("WARNING: You're in the global environment!")
    print("The machines can see everything you install.\n")

    print("To enter the construct, run:")
    print("python -m venv matrix_env")
    print("source matrix_env/bin/activate # On Unix")
    print("matrix_env")
    print("Scripts")
    print("activate    # On Windows\n")

    print("Then run this program again.")


def inside_venv() -> None:
    print("MATRIX STATUS: Welcome to the construct\n")

    print(f"Current Python: {sys.executable}")
    print(f"Virtual Enviroment: {os.path.basename(sys.prefix)}")
    print(f"Enviroment Path: {sys.prefix}\n")

    print("SUCCESS: You're in an isolated environment!")
    print("Safe to install packages without affecting")
    print("the global system.\n")

    print("Package installation path:")
    print(f"{site.getsitepackages()}\n")


if __name__ == "__main__":
    if sys.base_prefix != sys.prefix:
        inside_venv()
    else:
        outside_venv()
