"""class to provide attributes and methods for a single lp in the collection"""
from recording import Recording

class LP(Recording):
    """class for individual lp albums"""

    def __init__(self, lp_data) -> None:
        #define core fields in abstract base class attributes
        super().__init__(lp_data['who'], lp_data['what'])
        # way to assign arbitrary attributes based on dictionary addapted from:
        # https://stackoverflow.com/questions/2280334/shortest-way-of-creating-an-object-with-arbitrary-attributes-in-python
        # defining attribute for each field in data avoids needing to update each time model changes
        for k in lp_data:
            setattr(self, k, lp_data[k])

    def output_for_catalog(self, collection) -> str:
        """method to output data about this recording.
            maybe should be repr or print but wanted to include argument"""
        output = f"{'_'*80}\n"
        for fld in collection.fields:
            if getattr(self,fld): # don't print empty fields
                output += f"{fld}: {getattr(self,fld)}\n"
        print(output)
        return output

    def add_to_playlist(self, playlist) -> None:
        """method stub for adding to non-randomized playlist"""
