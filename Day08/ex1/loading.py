import sys
import numpy


def main() -> None:
    print("\nLOADING STATUS: Loading programs...\n")
    print("Checking dependencies:")
    try:
        import pandas
        print(f"[OK] pandas ({pandas.__version__}) - Data manipulation ready")
    except ImportError:
        print("pandas: no instal")
        return
    try:
        import requests
        print(f"[OK] requests ({requests.__version__}) - Network access ready")
    except ImportError:
        print("requests: no instal")
        return
    try:
        import matplotlib
        import matplotlib.pyplot as plt
        m = "Visualization ready"
        print(f"[OK] matplotlib ({matplotlib.__version__}) - {m}")
    except ImportError:
        print("matplotlib: no instal")
        return
    print("\nAnalyzing Matrix data...")
    age = numpy.random.normal(loc=45, scale=15, size=10000)
    age = pandas.Series(age)
    age.plot.hist(color='#36b33a', bins=20)

    plt.savefig("analysis.png", dpi=300, bbox_inches='tight')
    print("Results saved to: analysis.png}")
    sys.exit()


if __name__ == "__main__":
    main()
