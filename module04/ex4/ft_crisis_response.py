def get_path() -> str:
    last_slash = 0
    slast_slash = 0
    count = 0

    for char in __file__:
        if char == "/":
            slast_slash = last_slash
            last_slash = count
        count += 1

    return __file__[:slast_slash]


def crisis_handler(filename) -> None:
    print(f"CRISIS ALERT: Attempting access to '{filename}'...")

    try:
        with open(f'{filename}', 'r') as f:
            content = f.read()

        print(f"SUCCESS: Archive recovered - ``{content}``")
        print("STATUS: Normal operations resumed")

    except FileNotFoundError:
        print("RESPONSE: Archive not found in storage matrix")
        print("STATUS: Crisis handled, system stable")

    except PermissionError:
        print("RESPONSE: Security protocols deny access")
        print("STATUS: Crisis handled, security maintained")

    except Exception as e:
        print(f"RESPONSE: Unexpected system anomaly ({type(e).__name__})")
        print("STATUS: Crisis handled, system monitored")

    print()


def main() -> None:
    print("=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===\n")

    files_to_access = [
        "lost_archive.txt",
        "classified_data.txt",  # chmod 044 this file
        "standard_archive.txt"
    ]

    for file in files_to_access:
        crisis_handler(f'{file}')

    print("All crisis scenarios handled successfully. Archives secure.")


if __name__ == "__main__":
    main()
