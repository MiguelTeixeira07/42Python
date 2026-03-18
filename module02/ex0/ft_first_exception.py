def check_temperature(temp_str: str) -> int:
    try:
        temp_int = int(temp_str)
        if temp_int > 40:
            print(f"Error: {temp_int}°C is too hot for plants (max 40°C)")
        elif temp_int < 0:
            print(f"Error: {temp_int}°C is too cold for plants (min 0°C)")
        else:
            print(f"Temperature {temp_int}°C is perfect for plants!")
        return temp_int
    except ValueError:
        print(f"Error: '{temp_str}' is not a valid number")


def test_temperature_input() -> None:
    print('=== Garden Temperature Checker ===\n')
    temps = [25, 'abc', 100, -50]

    for temp in temps:
        print(f'Testing temperature: {temp}')
        check_temperature(temp)
        print()

    print("\nAll tests completed - program didn't crash!")


if __name__ == '__main__':
    test_temperature_input()
