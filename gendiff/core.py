import json


def generate_diff(file_path1, file_path2):
    data1 = json.load(open(file_path1))
    data2 = json.load(open(file_path2))
    data3 = data1 | data2
    data_sort = dict(sorted(data3.items()))
    data_diff = {}

    for key, value in data_sort.items():
        if key in data1 and key not in data2:
            data_diff[f'- {key}'] = value
        if key in data1 and key in data2:
            if data1[key] != data2[key]:
                data_diff[f'- {key}'] = data1[key]
                data_diff[f'+ {key}'] = data2[key]
            else:
                data_diff[f'  {key}'] = value
        if key not in data1 and key in data2:
            data_diff[f'+ {key}'] = value
    # data_string = json.dumps(data_diff, indent=2)
    # return data_string

    res = ''
    for k, v in data_diff.items():
        if v is False:
            v = 'false'
        if v is True:
            v = 'true'
        res += f'  {k}: {v}\n'

    return '{\n' + res + '}'
