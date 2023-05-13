#!/usr/bin/env python
from gendiff import generate_diff
from gendiff.parser import parse_input


def main():
    args = parse_input()
    print(generate_diff(args.first_file, args.second_file, args.format))


if __name__ == '__main__':
    main()
