from gendiff.diff import diff
from gendiff.formatters import plain, stylish
from gendiff.parser import parsing


def generate_diff(file_path1, file_path2, format_name='stylish'):
    data1 = parsing(file_path1)
    data2 = parsing(file_path2)

    data_diff = diff(data1, data2)
    
    if format_name == 'stylish':
        return stylish(data_diff)
    if format_name == 'plain':
        return plain(data_diff)
    
    # data3 = data1 | data2
    # data_sort = dict(sorted(data3.items()))
    # data_diff = {}

    # for key, value in data_sort.items():
    #     if key in data1 and key not in data2:
    #         data_diff[f'- {key}'] = value
    #     if key in data1 and key in data2:
    #         if data1[key] != data2[key]:
    #             data_diff[f'- {key}'] = data1[key]
    #             data_diff[f'+ {key}'] = data2[key]
    #         else:
    #             data_diff[f'  {key}'] = value
    #     if key not in data1 and key in data2:
    #         data_diff[f'+ {key}'] = value
    # data_string = json.dumps(data_diff, indent=2)
    # return data_string

    # res = ''
    # for k, v in data_diff.items():
    #     if v is False:
    #         v = 'false'
    #     if v is True:
    #         v = 'true'
    #     res += f'  {k}: {v}\n'

    # return '{\n' + res + '}'
