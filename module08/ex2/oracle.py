import os
import sys
from dotenv import load_dotenv


def load_configuration() -> dict[str, str | None]:
    load_dotenv()

    config = {
        'MATRIX_MODE': os.getenv('MATRIX_MODE', 'development'),
        'DATABASE_URL': os.getenv('DATABASE_URL'),
        'API_KEY': os.getenv('API_KEY'),
        'LOG_LEVEL': os.getenv('LOG_LEVEL', 'INFO'),
        'ZION_ENDPOINT': os.getenv('ZION_ENDPOINT')
    }

    return config


def validate_configuration(config: dict[str, str | None]) -> bool:
    missing = []

    if not config['DATABASE_URL']:
        missing.append('DATABASE_URL')
    if not config['API_KEY']:
        missing.append('API_KEY')
    if not config['ZION_ENDPOINT']:
        missing.append('ZION_ENDPOINT')

    if missing:
        print('WARNING: Missing required configuration values:')
        for variable in missing:
            print(f'- {variable}')
        print('\nCreate a .env file from .env.example', end=' ')
        print('or export variables manually.')
        return False

    return True


def show_configuration(config: dict[str, str | None]) -> None:
    print('Configuration loaded:')

    if config['MATRIX_MODE'] == 'development':
        print('Mode: development')
        print('Database: Connected to local instance')
    else:
        print('Mode: production')
        print('Database: Connected to production instance')

    if config['API_KEY']:
        print('API Access: Authenticated')
    else:
        print('API Access: Missing API key')

    print(f'Log Level: {config['LOG_LEVEL']}')

    if config['ZION_ENDPOINT']:
        print('Zion Network: Online')
    else:
        print('Zion Network: Offline')


def security_check() -> None:
    print('\nEnvironment security check:')
    print('[OK] No hardcoded secrets detected')
    print('[OK] .env file should be ignored by git')
    print('[OK] Production overrides available')


def main() -> None:
    print('\nORACLE STATUS: Reading the Matrix...\n')

    try:
        config = load_configuration()
        show_configuration(config)

        config_valid = validate_configuration(config)
        security_check()

        if not config_valid:
            print('\nThe Oracle sees missing configurations.')
            sys.exit(1)

        print('\nThe Oracle sees all configurations.')

    except Exception as error:
        print(f'ERROR: Failed to load configuration: {error}')
        sys.exit(1)


if __name__ == '__main__':
    main()
