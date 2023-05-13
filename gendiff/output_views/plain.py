from collections import OrderedDict

STATUS = 'status'
ADDED = 'added'
DELETED = 'deleted'
CHANGED = 'changed'

VALUE = 'value'
OLD_VALUE = 'old_value'
NEW_VALUE = 'new_value'
COMPLEX_VALUE = '[complex value]'


def plain_output(file: dict):
    def iter_(value, path):

        if not isinstance(value, dict):
            if isinstance(value, bool) or isinstance(value, int) \
                    or value is None:
                return str(value)
            else:
                return f"'{str(value)}'"

        sorted_file = OrderedDict(sorted(value.items(), key=lambda t: t[0]))
        lines = []

        for key, value in sorted_file.items():
            new_path = path + f"{key}."

            if not isinstance(value, dict):
                lines.append(COMPLEX_VALUE)

            elif value.get(STATUS) == CHANGED and value.get(VALUE):
                lines.append(
                    f"{(iter_(value.get(VALUE), new_path))}"
                )

            elif value.get(STATUS) == CHANGED and not value.get(VALUE):
                lines.append(
                    f"{path}{key}' was updated. "
                    f"From {iter_(value.get(OLD_VALUE), path)} "
                    f"to {iter_(value.get(NEW_VALUE), path)}"
                )

            elif value.get(STATUS) == ADDED:
                lines.append(
                    f"{path}{key}' was added with value: "
                    f"{iter_(value.get(VALUE), path)}"
                )

            elif value.get(STATUS) == DELETED:
                lines.append(
                    f"{path}{key}' was removed"
                )

        result = "\nProperty '".join(lines).replace('True', 'true') \
            .replace('False', 'false').replace('None', 'null')

        return result

    pre_result = iter_(file, '')

    return "Property '" + pre_result
