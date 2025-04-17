def filter_nondigits(data: list) -> list:

    """
    Filters a list to include only integers and floats, and multiplies them by 2.

    Args:
        data (list): A list of items.

    Returns:
        list: A new list containing only the integer and float elements from the input list, multiplied by 2.
    """
    new_data = []
    for d in data:
        if isinstance(d, (int, float)):
            new_data.append(d)
    return new_data