from collections import OrderedDict


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
                lines.append('[complex value]')

            elif value.get('status') == 'changed' and value.get('value'):
                lines.append(
                    f"{(iter_(value.get('value'), new_path))}"
                )

            elif value.get('status') == 'changed' and not value.get('value'):
                lines.append(
                    f"{path}{key}' was updated. "
                    f"From {iter_(value.get('old_value'), path)} "
                    f"to {iter_(value.get('new_value'), path)}"
                )

            elif value.get('status') == 'added':
                lines.append(
                    f"{path}{key}' was added with value: "
                    f"{iter_(value.get('value'), path)}"
                )

            elif value.get('status') == 'deleted':
                lines.append(
                    f"{path}{key}' was removed"
                )

        result = "\nProperty '".join(lines).replace('True', 'true') \
            .replace('False', 'false').replace('None', 'null')

        return result

    pre_result = iter_(file, '')

    return "Property '" + pre_result
