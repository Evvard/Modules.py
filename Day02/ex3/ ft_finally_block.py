def water_plants(plant_list) -> None:
    print("Testing normal watering...")
    print("Opening watering system")
    i = 0
    for i in plant_list:
        print("Watering", i)
    print("Closing watering system (cleanup)")
    print("Watering completed successfully!\n")


def test_watering_system(plant_list) -> None:
    print("Testing with error...")
    print("Opening watering system")
    try:
        for i in plant_list:
            if not i.isalpha():
                raise ValueError
            print("Watering", i)
    except ValueError:
        print(f"Error: Cannot water {i} - invalid plant!")
    finally:
        print("Closing watering system (cleanup)\n")
        print("Cleanup always happens, even with errors!")


if __name__ == "__main__":
    print("=== Garden Watering System ===\n")
    plant_list = ["tomato", "lettuce", "carrots"]
    water_plants(plant_list)
    plant_list += ["0000"]
    test_watering_system(plant_list)
