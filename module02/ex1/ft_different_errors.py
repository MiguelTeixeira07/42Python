def garden_operations(error: int) -> None:
    match error:
        case 0:
            int('abc')
        case 1:
            test = 5 / 0
            print(test)
        case 2:
            file = open("test.txt")
            file.close()
        case 3:
            dict = {"num": 5, "str": "abc", "bool": True}
            print(dict["float"])
        case _:
            int('abc')

            test = 5 / 0
            print(test)

            file = open("test.txt")
            file.close()

            dict = {"num": 5, "str": "abc", "bool": True}
            print(dict["float"])


def test_error_types():
    try:
        print("Testing ValueError...")
        garden_operations(0)
    except ValueError as e:
        print(f"Caught ValueError: {e}")
    finally:
        print()

    try:
        print("Testing ZeroDivisionError...")
        garden_operations(1)
    except ZeroDivisionError as e:
        print(f"Caught ZeroDivisionError: {e}")
    finally:
        print()

    try:
        print("Testing FileNotFoundError...")
        garden_operations(2)
    except FileNotFoundError as e:
        print(f"Caught FileNorFoundError: {e}")
    finally:
        print()

    try:
        print("Testing KeyError...")
        garden_operations(3)
    except KeyError as e:
        print(f"Caught KeyError: {e}")
    finally:
        print()

    try:
        print("Testing multiple errors together")
        garden_operations(4)
    except Exception:
        print("Caught an error, but the program continues!")
    finally:
        print()

    print("All error types tested successfully!")


if __name__ == '__main__':
    test_error_types()
