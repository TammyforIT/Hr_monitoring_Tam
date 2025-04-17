def average(data: list) -> float:
    if not data:
        raise ValueError("list cannot be empty")
    return sum(data)/ len(data) #size data
    """
    Calculate average value of the list.

    Args:
        data (list[int]): list of integers representing heart rate samples
    Returns:
        float: a floating point value representing the average of this list
    """
    #average = 0
    #maximum = 0


def maximum(data: list) -> float:
    if not data:
        raise ValueError("list cannot be empty")
    return max(data)
    """sn
    INSERT DOCSTRING HERE
    """
    pass


def variance(data: list) -> float:
    if not data:
        raise ValueError("list cannot be empty")
    n = len(data)
    mean = sum(data) /n
    return sum((x-mean)**2 for x in data) /n
    """
    INSERT DOCSTRING HERE
    (calculate population variance)
    """
    pass


def standard_deviation(data: list) -> float:
    if not data:
        raise ValueError("cannot be empty")
    return variance(data)**0.5 #if less than 1 its a 0
    """
    INSERT DOCSTRING HERE
    (calculate population standard deviation)
    """
    pass
