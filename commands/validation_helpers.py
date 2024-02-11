def validate_params_count(params, count):
    if len(params) != count:
        raise ValueError(
            f'Invalid number of arguments. Expected: {count}; received: {len(params)}.")')

def try_parse_int(s):
    try:
        return int(s)
    except:
        raise ValueError('Invalid value .')