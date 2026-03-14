import sys
import importlib.metadata


def check_dependencies():
    packages = ["pandas", "matplotlib", "numpy"]
    caract = ['Data manipulation',
              'Visualization ready', 'Numerical computing']
    all_ok = True
    print("\nChecking dependencies:")

    for pkg in packages:
        try:
            v = importlib.metadata.version(pkg)
            print(f"[OK] {pkg} ({v}) - {caract[packages.index(pkg)]} Ready")
        except importlib.metadata.PackageNotFoundError:
            print(f"[MISSING] {pkg} - Not found!")
            all_ok = False

    if not all_ok:
        print("\nERROR: Missing dependencies.")
        print("To install via pip: pip install -r requirements.txt")
        print("To install via Poetry: poetry install")
        sys.exit(1)


def run_analysis():
    import pandas as pd
    import numpy as np
    import matplotlib.pyplot as plt

    print("\nAnalyzing Matrix data...")
    print("Processing 1000 data points...")
    data = np.random.randint(0, 1000, size=1000)
    table = pd.DataFrame(data, columns=['Signal Intensity'])
    print("Generating visualization...")
    table.hist(bins=30, color='green')
    plt.title("Matrix Data Analysis")
    plt.savefig("matrix_analysis.png")

    print("\nAnalysis complete!")
    print("Results saved to: matrix\\_analysis.png}")


if __name__ == "__main__":
    print("\nLOADING STATUS: Loading programs...")
    check_dependencies()
    run_analysis()
