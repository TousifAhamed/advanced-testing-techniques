def add(x,y):
    import pdb;pdb.set_trace()
    """
    This function adds two numbers together and returns the result.
    Parameters:
    x (int): The first number to add.
    y (int): The second number to add.
    Returns:
    int: The sum of x and y.
    """
    print(f"This is x: {x} and the x-type is {type(x)}")
    print(f"This is x: {y} and the y-type is {type(y)}")

    try:
        result = x + y
    except TypeError:
        print(f"The wrong type passed")
        result = int(x) + int(y)
    print(f"This is sht result {result}")
    return result

print(add("one",2))
