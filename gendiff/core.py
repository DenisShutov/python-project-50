from gendiff.diff import diff
from gendiff.formatters import json, plain, stylish
from gendiff.parser import parsing


def generate_diff(file_path1, file_path2, format_name='stylish'):
    data1 = parsing(file_path1)
    data2 = parsing(file_path2)

    data_diff = diff(data1, data2)
    
    if format_name == 'stylish':
        return stylish(data_diff)
    if format_name == 'plain':
        return plain(data_diff)
    if format_name == 'json':
        return json(data_diff)