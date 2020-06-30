def str_to_dict(some_str):  
    """
    :param some_str: str
    :return: dict
    """
    return {str:some_str.count(str) for str in set(some_str)}


print('Str to dict:', str_to_dict('dataroot_university'))