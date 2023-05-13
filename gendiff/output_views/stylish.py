import itertools
from collections import OrderedDict

STATUS = 'status'
ADDED = 'added'
DELETED = 'deleted'
CHANGED = 'changed'
UNCHANGED = 'unchanged'

VALUE = 'value'
OLD_VALUE = 'old_value'
NEW_VALUE = 'new_value'


def stylish_output(file: dict):

    def iter_(data, depth):

        if not isinstance(data, dict):
            return str(data)

        sorted_file = OrderedDict(sorted(data.items(), key=lambda t: t[0]))

        lines = []
        spaces_count = 1
        deep_indent_size = depth + spaces_count
        condition = {
            ADDED: '  + ',
            DELETED: '  - ',
            CHANGED: '    ',
            UNCHANGED: '    '
        }
        replacer = '    '
        deep_indent = replacer * (deep_indent_size - 1)
        current_indent = replacer * depth

        for key, value in sorted_file.items():

            if not isinstance(value, dict):
                lines.append(
                    f"{deep_indent}"
                    f"{condition[UNCHANGED]}"
                    f"{key}: "
                    f"{value}"
                )

            elif value.get(VALUE):
                lines.append(
                    f"{deep_indent}"
                    f"{condition[value.get(STATUS, UNCHANGED)]}"
                    f"{key}: "
                    f"{iter_(value.get(VALUE), deep_indent_size)}"
                )

            elif value.get(STATUS) == CHANGED:

                lines.append(
                    f"{deep_indent}"
                    f"{condition[DELETED]}"
                    f"{key}: "
                    f"{iter_(value.get(OLD_VALUE), deep_indent_size)}"
                )
                lines.append(
                    f"{deep_indent}"
                    f"{condition[ADDED]}"
                    f"{key}: "
                    f"{iter_(value.get(NEW_VALUE), deep_indent_size)}"
                )

            else:
                lines.append(
                    f"{deep_indent}"
                    f"{condition[value.get(STATUS, UNCHANGED)]}"
                    f"{key}: "
                    f"{iter_(value.get(VALUE, value), deep_indent_size)}"
                )

        result = itertools.chain("{", lines, [current_indent + "}"])

        return '\n'.join(result).replace('True', 'true')\
            .replace('False', 'false').replace('None', 'null')

    return iter_(file, 0)
