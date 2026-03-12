def garden_operations(object: str, division: str, files: str,
                      dico: dict, plant: str, multple: bool) -> str:

    if multple == 1:
        try:
            x = int(object) / int(division)
            x = open(files)
            x.close()
            x = (dico[f"{plant}"])
        except (ZeroDivisionError, ValueError, KeyError, FileNotFoundError):
            print("Caught an error, but program continues!", "\n")
            return
    try:
        nbr = int(object)
        result = nbr / int(division)
    except ValueError:
        print("Caught ValueError: invalid literal for int()", "\n")
        return
    except ZeroDivisionError:
        print("Caught ZeroDivisionError: division by zero", "\n")
        return
    try:
        with open(f'{files}', 'r') as file:
            pass
        del file
    except FileNotFoundError:
        print(f"Caught FileNotFoundError: No such file '{files}'", "\n")
        return
    try:
        result = (dico[f"{plant}"])
        del result
    except KeyError:
        print(f"Caught KeyError: 'missing \\_{plant}'", "\n")
        return


def test_error_types() -> None:

    dico = {'nom': 'Alice', 'age': 30}

    print("=== Garden Error Types Demo ===", "\n")
    print("Testing ValueError...")
    garden_operations("Test", "1", "fichier.txt", dico, "nom", 0)
    print("Testing ZeroDivisionError...")
    garden_operations("5", "0", "fichier.txt", dico, "nom", 0)
    print("Testing FileNotFoundError...")
    garden_operations("5", "1", "fake_file.txt", dico, "nom", 0)
    print("Testing KeyError...")
    garden_operations("5", "1", "fichier.txt", dico, "plant", 0)
    print("Testing multiple errors together...")
    garden_operations("Text", "0", "fichier.txt", dico, "plant", 1)
    print("All error types tested successfully!")


if __name__ == "__main__":
    test_error_types()
