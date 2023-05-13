import json
import os

import yaml
from gendiff.output_views.json import json_output
from gendiff.output_views.plain import plain_output
from gendiff.output_views.stylish import stylish_output

STATUS = 'status'
ADDED = 'added'
DELETED = 'deleted'
CHANGED = 'changed'
UNCHANGED = 'unchanged'

VALUE = 'value'
OLD_VALUE = 'old_value'
NEW_VALUE = 'new_value'

STYLISH = 'stylish'
PLAIN = 'plain'
JSON = 'json'


def extract_data(path: str) -> dict:
    absolute_path = os.path.abspath(path)

    with open(absolute_path) as import_file:
        if absolute_path.endswith('.yml') or absolute_path.endswith('.yaml'):
            result = yaml.safe_load(import_file)
        elif absolute_path.endswith('.json'):
            result = json.load(import_file)

    return result


def make_diff(file1: dict, file2: dict) -> dict:
    keys = file1.keys() | file2.keys()
    result = {}

    for key in keys:
        if key not in file1:
            result[key] = {
                STATUS: ADDED,
                VALUE: file2.get(key)
            }
        elif key not in file2:
            result[key] = {
                STATUS: DELETED,
                VALUE: file1.get(key)
            }
        elif file1[key] == file2[key]:
            if isinstance(file1[key], dict) and \
                    isinstance(file2[key], dict):
                result[key] = {
                    STATUS: UNCHANGED,
                    VALUE: make_diff(file1[key], file2[key])
                }
            else:
                result[key] = {
                    STATUS: UNCHANGED,
                    VALUE: file1.get(key)
                }
        else:
            if isinstance(file1[key], dict) and \
                    isinstance(file2[key], dict):
                result[key] = {
                    STATUS: CHANGED,
                    VALUE: make_diff(file1[key], file2[key])
                }
            else:
                result[key] = {
                    STATUS: CHANGED,
                    OLD_VALUE: file1[key],
                    NEW_VALUE: file2[key]
                }

    return result


def generate_diff(
        file_path1: str,
        file_path2: str,
        format_name: str = STYLISH
) -> str:

    file_data1, file_data2 = extract_data(file_path1), extract_data(file_path2)
    data_diff = make_diff(file_data1, file_data2)

    if format_name == STYLISH:
        return stylish_output(data_diff)

    elif format_name == PLAIN:
        return plain_output(data_diff)

    elif format_name == JSON:
        return json_output(data_diff)

    return None
