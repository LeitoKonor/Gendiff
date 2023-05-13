import argparse

STYLISH = 'stylish'
PLAIN = 'plain'
JSON = 'json'


def parse_input():
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.'
    )
    parser.add_argument(
        'first_file',
        type=str
    )
    parser.add_argument(
        'second_file',
        type=str
    )
    parser.add_argument(
        '-f', '--format',
        help='set format of output (default: "stylish")',
        choices=[STYLISH, PLAIN, JSON],
        default=STYLISH
    )
    args = parser.parse_args()

    return args
