def get_path() -> str:
    last_slash = 0
    slast_slash = 0
    count = 0

    for char in __file__:
        if char == "/":
            slast_slash = last_slash
            last_slash = count
        count += 1

    return __file__[:slast_slash + 1]


def main() -> None:
    fname = 'ancient_fragment.txt'
    fpath = get_path()

    print('=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===\n')
    print(f'Accessing Storage Vault: {fname}')

    with open(f'{fpath}{fname}', 'r') as file:
        print('Connection established...')
        print(file.read())

    print('\nData recovery complete. Storage unit disconnected.')


if __name__ == '__main__':
    main()
