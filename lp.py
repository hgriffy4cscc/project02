from recording import Recording

class LP(Recording):
    """class for individual lp albums"""

    def __init__(self, var_dict) -> None:
        super().__init__(var_dict['who'], var_dict['what'])
        # way to assign arbitrary attributes based on dictionary addapted from:
        # https://stackoverflow.com/questions/2280334/shortest-way-of-creating-an-object-with-arbitrary-attributes-in-python
        for k in var_dict:
            if k not in ('who','what'):
                setattr(self, k, var_dict[k])
    
    def output_for_catalog(self):
        return super().output_for_catalog()
    
    def add_to_playlist(self, playlist):
        return super().add_to_playlist(playlist)