def stylish(data, depth=1):
    indent = (depth * 4 - 2) * ' '
    res = ''
    for k, v in data.items():
        if not isinstance(v, dict):
            if v is False:
                v = 'false'
            elif v is True:
                v = 'true'
            elif v is None:
                v = 'null'
            res += f'{indent}{k}: {v}\n'
        else:
            res += f'{indent}{k}: {{\n{stylish(v, depth + 1)}{indent}}}\n'
    if depth == 1:
        res = '{\n' + res + '}'
    return res