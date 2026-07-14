

class LP:
    """class for individual lp albums"""

    def __init__(self, var_dict) -> None:
        # way to assign arbitrary attributes based on dictionary addapted from:
        # https://stackoverflow.com/questions/2280334/shortest-way-of-creating-an-object-with-arbitrary-attributes-in-python
        for k in var_dict:
            setattr(self, k, var_dict[k])