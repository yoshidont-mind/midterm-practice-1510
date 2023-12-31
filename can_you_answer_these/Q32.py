def double_preceding(values):
    """
    Replace each item in the list with twice the value of the preceding item, and replace the first item with 0.
    >>> L = [1, 2, 3]
    >>> double_preceding(L)
    >>> L
    [0, 2, 4]
    """

    if values:
        temp = values[0]
        values[0] = 0
        for i in range(1, len(values)):
            another_temp = values[i]
            values[i] = 2 * temp
            temp = another_temp
