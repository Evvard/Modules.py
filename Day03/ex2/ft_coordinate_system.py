import math


def Pythagorean_theorem(base: tuple, end: tuple) -> float:
    final = math.sqrt((end[0] - base[0])**2 + (end[1] - base[1])**2 +
                      (end[2] - base[2])**2)
    return final


if __name__ == "__main__":

    pos_base = (10, 20, 5)
    pos_spawn = (0, 0, 0)
    pos_test = (3, 4, 0)
    pos_error = ("abc", "def", "ghi")

    print("=== Game Coordinate System ===\n")
    print(f"Position created: {pos_base}")
    res = Pythagorean_theorem(pos_base, pos_spawn)
    print(f"Distance between {pos_spawn} and {pos_base}: ", end="")
    print("{:.2f}\n".format(res))

    try:
        i = 0
        while i < 2:
            y = int(pos_test[i])
            i += 1
        print("Parsing coordinates: \"", end="")
        print(*pos_test, sep=",", end="\"\n")
        print(f"Parsed position: {pos_test}")
        res = Pythagorean_theorem(pos_test, pos_spawn)
        print(f"Distance between {pos_spawn} and {pos_test}: ", end="")
        print(f"{res:.1f}\n")
        last_coordonne = pos_test
    except ValueError:
        print("Parsing invalid coordinates: \"", end="")
        print(*pos_test, sep=",", end="\"\n")
        print("Error parsing coordinates: invalid literal", end=" ")
        print(f"for int() with base 10: '{pos_test[i]}'")
        print("Error details - Type: ValueError, Args: (\"", end="")
        print(f"invalid literal for int() with base 10: '{pos_test[i]}'\",)\n")

    try:
        i = 0
        while i < 2:
            y = int(pos_error[i])
            i += 1
        print("Parsing coordinates: \"", end="")
        print(*pos_error, sep=",", end="\"\n")
        print(f"Parsed position: {pos_error}")
        res = Pythagorean_theorem(pos_error, pos_spawn)
        print(f"Distance between {pos_spawn} and {pos_error}: ", end="")
        print(f"{res:.2f}\n")
        last_coordonne = pos_error
    except ValueError:
        print("Parsing invalid coordinates: \"", end="")
        print(*pos_error, sep=",", end="\"\n")
        print("Error parsing coordinates: invalid literal", end=" ")
        print(f"for int() with base 10: '{pos_error[i]}'")
        print("Error details - Type: ValueError, Args: (\"invalid", end="")
        print(f" literal for int() with base 10: '{pos_error[i]}'\",)\n")

    print("Unpacking demonstration:")
    print(f"Player at x={last_coordonne[0]}, y={last_coordonne[1]}, ", end="")
    print(f"z={last_coordonne[2]}")
    print(f"Coordinates: X={last_coordonne[0]},", end="")
    print(f" Y={last_coordonne[1]}, Z={last_coordonne[2]}")
