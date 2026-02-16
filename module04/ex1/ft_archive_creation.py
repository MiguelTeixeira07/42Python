def get_path() -> str:
    last_slash = 0
    count = 0

    for char in __file__:
        if char == "/":
            last_slash = count
        count += 1

    return __file__[:last_slash + 1]


def main() -> None:
    fname = 'new_discovery.txt'
    fpath = get_path()

    print('=== CYBER ARCHIVES - PRESERVATION SYSTEM ===\n')
    print(f'Initializing new storage unit: {fname}')

    with open(f'{fpath}{fname}', 'w') as file:
        print('Connection established...')

        try:
            file.write(
                '[ENTRY 001] New quantum algorithm discovered\n'
                '[ENTRY 002] Efficiency increased by 347%\n'
                '[ENTRY 003] Archived by Data Archivist trainee'
            )
        except Exception:
            print('Something went wrong...')
            return

    print('\nData recovery complete. Storage unit sealed.')
    print(f"Archive '{fname}' ready for long-term preservation")


if __name__ == '__main__':
    main()
