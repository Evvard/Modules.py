
def check_temperature(temp_str: str) -> str:
    try:
        x = int(temp_str)
    except ValueError:
        x = temp_str
    if type(x) is int:
        if x <= 40 and x >= 0:
            return f"Temperature {temp_str}°C is perfect for plants"
        elif x > 0:
            return f"Error: {temp_str}°C is too hot for plants (min 0°C)"
        elif x < 40:
            return f"Error: {temp_str}°C is too cold for plants (max 40°C)"
    return f"Error: '{temp_str}' is not a valid number"


def test_temperature_input() -> None:
    print("=== Garden Temperature Checker ===", "\n")
    print("Testing temperature: ")
    print(check_temperature("25"), "\n")
    print("Testing temperature: ")
    print(check_temperature("abc"), "\n")
    print("Testing temperature: ")
    print(check_temperature("100"), "\n")
    print("Testing temperature: ")
    print(check_temperature("-50"), "\n")
    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature_input()
