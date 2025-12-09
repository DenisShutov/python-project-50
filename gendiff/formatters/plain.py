def plain(data, path=''):  # noqa: C901
    res = []
    for key, value in data.items():
        current_path = f'{path}.{key[2:]}' if path else key[2:]
        if not isinstance(value, dict):
            if key.startswith('-'):
                if f'+ {key[2:]}' in data:
                    new_value = data[f'+ {key[2:]}']
                    res.append(f'Property \'{current_path}\' was updated. '
                               f'From {format_value(value)} '
                               f'to {format_value(new_value)}')
                else:
                    res.append(f'Property \'{current_path}\' was removed')
            elif key.startswith('+'):
                if f'- {key[2:]}' not in data:
                    res.append(f'Property \'{current_path}\' was added '
                               f'with value: {format_value(value)}')
        else:
            if key.startswith('-') and f'+ {key[2:]}' in data:
                new_value = data[f'+ {key[2:]}']
                res.append(f'Property \'{current_path}\' was updated. '
                           f'From [complex value] to {format_value(new_value)}')
            else:
                nested_result = plain(value, current_path)
                if nested_result:
                    res.extend(nested_result.split('\n'))

                if key.startswith('-'):
                    if f'+ {key[2:]}' not in data and not nested_result:
                        res.append(f'Property \'{current_path}\' was removed')

                elif key.startswith('+'):
                    if f'- {key[2:]}' not in data and not nested_result:
                        res.append(f'Property \'{current_path}\' was added '
                                   f'with value: {format_value(value)}')

    return '\n'.join(res)


def format_value(value):
    if isinstance(value, dict):
        return "[complex value]"
    elif isinstance(value, str):
        return f"'{value}'"
    elif value is True:
        return "true"
    elif value is False:
        return "false"
    elif value is None:
        return "null"
    else:
        return value