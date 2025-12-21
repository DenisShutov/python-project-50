def diff(data1, data2):
    data3 = sorted(set(data1) | set(data2))
    data_diff = {}
    for key in data3:
        if key in data1 and key not in data2:
            data_diff[f'- {key}'] = data1[key]
        elif key in data2 and key not in data1:
            data_diff[f'+ {key}'] = data2[key]
        elif key in data1 and key in data2:
            if data1[key] == data2[key]:
                data_diff[f'  {key}'] = data2[key]

            elif (not isinstance(data1[key], dict)
                and not isinstance(data2[key], dict)):
                data_diff[f'- {key}'] = data1[key]
                data_diff[f'+ {key}'] = data2[key]
            elif isinstance(data1[key], dict) and isinstance(data2[key], dict):
                child_data = diff(data1[key], data2[key])
                data_diff[f'  {key}'] = child_data
            else:
                data_diff[f'- {key}'] = data1[key]
                data_diff[f'+ {key}'] = data2[key]
    
    return data_diff