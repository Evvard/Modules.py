def check_plant_health(plant_name, water_level, sunlight_hours) -> None:
    print("Testing good values...")
    for i in plant_name:
        try:
            if not i:
                raise BaseException
            print(f"Plant '{i}' is healthy!")
        except BaseException:
            print("\nTesting empty plant name...")
            print("Error: Plant name cannot be empty!")
            break
    try:
        print("\nTesting bad water level...")
        if int(water_level) < 1:
            raise Exception
        elif int(water_level) > 10:
            raise AssertionError
    except Exception:
        print(f"Error: Water level {water_level} is too low (min 1)")
    except AssertionError:
        print(f"Error: Water level {water_level} is too high (max 10)")
    print("\nTesting bad sunlight hours...")
    try:
        if int(sunlight_hours) < 2:
            raise Exception
        elif int(sunlight_hours) > 12:
            raise AssertionError
    except Exception:
        print(f"Error: Sunlight hours {sunlight_hours} is too low (min 2)")
    except AssertionError:
        print(f"Error: Sunlight hours {sunlight_hours} is too hight (min 12)")
    print("\nAll error raising tests completed!")


def test_plant_checks() -> None:
    print("=== Garden Plant Health Checker ===")
    plant_name = ["tomato", "salad", "", "rest"]
    check_plant_health(plant_name, 15, 0)


if __name__ == "__main__":
    test_plant_checks()
