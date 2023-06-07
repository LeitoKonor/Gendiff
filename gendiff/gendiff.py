import json
import yaml
from gendiff.formatters.json import json_output
from gendiff.formatters.plain import plain_output
from gendiff.formatters.stylish import stylish_output


def extract_data(path, extension='json') -> dict:
    if extension == 'yml' or extension == 'yaml':
        result = yaml.safe_load(path)
    elif extension == 'json':
        result = json.load(path)
    else:
        raise ValueError('This extension is not supported!')

    return result


def make_diff(file1: dict, file2: dict) -> dict:
    keys = file1.keys() | file2.keys()
    result = {}

    for key in keys:
        if key not in file1:
            result[key] = {
                'status': 'added',
                'value': file2.get(key)
            }
        elif key not in file2:
            result[key] = {
                'status': 'deleted',
                'value': file1.get(key)
            }
        elif file1[key] == file2[key]:
            if isinstance(file1[key], dict) and \
                    isinstance(file2[key], dict):
                result[key] = {
                    'status': 'unchanged',
                    'value': make_diff(file1[key], file2[key])
                }
            else:
                result[key] = {
                    'status': 'unchanged',
                    'value': file1.get(key)
                }
        else:
            if isinstance(file1[key], dict) and \
                    isinstance(file2[key], dict):
                result[key] = {
                    'status': 'changed',
                    'value': make_diff(file1[key], file2[key])
                }
            else:
                result[key] = {
                    'status': 'changed',
                    'old_value': file1[key],
                    'new_value': file2[key]
                }

    return result


def generate_diff(
        file_path1: str,
        file_path2: str,
        format_name: str = 'stylish'
) -> str:

    file_data1 = extract_data(open(file_path1), file_path1.split('.')[-1])
    file_data2 = extract_data(open(file_path2), file_path2.split('.')[-1])
    data_diff = make_diff(file_data1, file_data2)

    if format_name == 'stylish':
        return stylish_output(data_diff)

    elif format_name == 'plain':
        return plain_output(data_diff)

    elif format_name == 'json':
        return json_output(data_diff)

    return None
