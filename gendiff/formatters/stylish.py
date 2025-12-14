def stylish(data, depth=1):
    indent_prefix = (depth * 4 - 2) * ' '
    indent = (depth * 4) * ' '
    prefix = ('  ', '+ ', '- ')
    lines = []
    for k, v in data.items():
        if not isinstance(v, dict):
            if k[:2] in prefix:
                lines.append(f'{indent_prefix}{k}: {format_val(v)}')
            else:
                lines.append(f'{indent}{k}: {format_val(v)}')
        else:
            if k[:2] in prefix:
                lines.append(f'{indent_prefix}{k}: '
                             f'{{\n{stylish(v, depth + 1)}\n{indent}}}')
            else:
                lines.append(f'{indent}{k}: '
                             f'{{\n{stylish(v, depth + 1)}\n{indent}}}')
    result = '\n'.join(lines)

    if depth == 1:
        return '{\n' + result + '\n}'
    return result


def format_val(v):
    if v is False:
        v = 'false'
    elif v is True:
        v = 'true'
    elif v is None:
        v = 'null'
    return v