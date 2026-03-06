import sys

if __name__ == "__main__":
    arg = len(sys.argv)
    nb = 1
    print("=== Command Quest ===")
    if arg == 1:
        print("No arguments provided!")
    print(f"Program name: {sys.argv[0]}")
    if arg > 1:
        print(f"Arguments received: {arg - 1}")
        for i in sys.argv:
            if i != sys.argv[0]:
                print(f"Argument {nb}: {i}")
                nb = nb + 1
    print(f"Total arguments: {arg}")
