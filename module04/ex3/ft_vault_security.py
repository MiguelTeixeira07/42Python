def get_main_directory() -> str:
    last_slash = 0
    slast_slash = 0
    count = 0

    for char in __file__:
        if char == "/":
            slast_slash = last_slash
            last_slash = count
        count += 1

    return __file__[:slast_slash]


def get_subdirectory() -> str:
    last_slash = 0
    count = 0

    for char in __file__:
        if char == "/":
            last_slash = count
        count += 1

    return __file__[:last_slash]


def copy_content(src_path: str, dst_path: str) -> None:
    print('Vault connection established with failsafe protocols\n')

    print('SECURE EXTRACTION:')

    with open(src_path, 'r') as src_file:
        content = src_file.read()

    print('[CLASSIFIED] Quantum encryption keys recovered')
    print('[CLASSIFIED] Archive integrity: 100%')

    print('SECURE PRESERVATION:')

    with open(dst_path, 'w') as dst_file:
        dst_file.write(content)
        print('[CLASSIFIED] New security protocols archived')

    print('Vault automatically sealed upon completion\n')


def main() -> None:
    src_name = 'classified_data.txt'
    src_path = f'{get_main_directory()}/{src_name}'
    dest_name = 'cloned_data.txt'
    dest_path = f'{get_subdirectory()}/{dest_name}'

    print('=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===\n')
    print('Initiating secure vault access...')

    copy_content(src_path, dest_path)

    print('All vault operations completed with maximum security.')


if __name__ == '__main__':
    main()
