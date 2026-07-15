from lp import LP
from settings import Settings
import csv

class LPCollection:

    def __init__(self,settings) -> None:
        self.settings = Settings()
        self.title = ""
        self.fields: list = []
        self.lpcollection: list = []
        self.matching_indexes: list[int] = []

    def get_the_data(self):
        """
        Extract data from a csv file and return it for processing

        Args:
            filename: optional Name of csv file to get data from.

        """
        
        with open(self.settings.source_file, 'r', encoding='cp1252') as csvfile:
            csvreader = csv.DictReader(csvfile)  # Reader object
            self.fields = csvreader.fieldnames
            for row in csvreader:     # Read rows
                self.lpcollection.append(LP(row))
            

    ###### FIND MATCHING LPS ######
    def search_lpcollection(self,controls) -> list[int]:
        """
        Return up to maximum number of lps where title matches the given search string.

        Args:
            none but uses the folling variables from outer scope(s)
            lps: list of dictionaries for dataset
            search_field: the field to be searched
            for_what: the search string provided by user
            how_many: maximum number of matches to return

        Returns:
            matching_indexes: list of indexes for matching dictionary items in lps list
        """
        for i, lp in enumerate(self.lpcollection):
            # h/t https://www.geeksforgeeks.org/python/enumerate-in-python/
            if controls.for_what.lower() in getattr(lp, self.settings.field_dict[controls.do_what]).lower():
                self.matching_indexes.append(i)

    ###### OUTPUT RESULTING MATCHES ######
    def output_results(self):
        """
        Outputs matched lps items

        Args:
            none, but uses the following variables from outer scope(s)
            matching_indexes: indexes for lps that match search
            fields: the list of fields in the dataset
            lps: dictionary of the dataset

        Side-effect:
            output to the terminal
        """
        #print(f"Responses were: {do_what} :: {for_what} :: {how_many}")
        print(f"There were {len(self.matching_indexes)} results:")
        for i in self.matching_indexes:
            self.lpcollection[i].output_for_catalog(self)

    def __repr__(self) -> str:
        return f"Total no. of rows: {len(self.lpcollection)}"  # Row count

class Playlist(LPCollection):
    """
    """
    def __init__(self, settings, full_collection):
        super().__init__(settings)
        self.lpcollection = full_collection.lpcollection
        self.fields = full_collection.fields
        
    ##### BUILD A RANDOMIZED PLAYLIST #####
    def build_random_playlist(self,controls):
        import random
        self.matching_indexes = []
        for i in range(controls.how_many):
            self.matching_indexes.append(random.randrange(len(self.lpcollection)))

    ##### EXPORT TO FILE #####
    def export_to_file(self):
        from pathlib import Path
        
