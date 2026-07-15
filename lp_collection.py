"""class to manage collection of multiple lps"""
import csv
from lp import LP

class LPCollection:
    """class to manage a collection of lps"""
    def __init__(self,settings) -> None:
        self.settings = settings
        self.title = ""
        self.fields: list = []
        self.lpcollection: list = []
        self.matching_indexes: list[int] = []

    def get_the_data(self):
        """Extract data from a csv file and return it for processing
        Filename stored in settings"""

        with open(self.settings.source_file, 'r', encoding='cp1252') as csvfile:
            csvreader = csv.DictReader(csvfile)  # Reader object
            for f in csvreader.fieldnames:
                self.fields.append(f)
            for row in csvreader:     # Read rows
                # create new LP instance per lp in the collection
                # and include it in a list in the collection instance
                self.lpcollection.append(LP(row))

    ###### FIND MATCHING LPS ######
    def search_lpcollection(self,controls) -> None:
        """
        Return up to maximum number of lps where title matches the given search string.

        Args:
            * controls to provide access to user-input responses to prompts

        Returns:
            * no explicit return but...
            * stores values in attribute matching_indexes:
                list of indexes for matching dictionary items in lps list
        """
        self.matching_indexes = [] # reset for new search
        for i, lp in enumerate(self.lpcollection):
            # transfer variable because line was too long
            matchfield = getattr(lp, self.settings.field_dict[controls.do_what]).lower()
            if controls.for_what.lower() in matchfield:
                self.matching_indexes.append(i)

    ###### OUTPUT RESULTING MATCHES ######
    def output_results(self):
        """
        Outputs matched lps items

        Side-effect:
            output to the terminal
        """
        #print(f"Responses were: {do_what} :: {for_what} :: {how_many}")
        print(f"There were {len(self.matching_indexes)} results:")
        for i in self.matching_indexes:
            self.lpcollection[i].output_for_catalog(self)

    def __repr__(self) -> str:
        return f"Total no. of rows: {len(self.lpcollection)}"  # Row count
