from recording import Recording

class LP(Recording):
    """class for individual lp albums"""

    def __init__(self, lp_data) -> None:
        super().__init__(lp_data['who'], lp_data['what'])
        # way to assign arbitrary attributes based on dictionary addapted from:
        # https://stackoverflow.com/questions/2280334/shortest-way-of-creating-an-object-with-arbitrary-attributes-in-python
        for k in lp_data:
            setattr(self, k, lp_data[k])
    
    def output_for_catalog(self,lpcollection):
        print(f"{'_'*80}")
        for fld in lpcollection.fields:
            print(f"{fld}: {getattr(self,fld)}")
    
    def add_to_playlist(self, playlist):
        return super().add_to_playlist(playlist)