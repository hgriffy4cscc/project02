from lp import LP
from settings import Settings
import csv

class LPCollection:

    def __init__(self,settings) -> None:
        self.settings = Settings()
        self.title = ""
        self.fields: dict = {}
        self.lpcollection: list = []

    def get_the_data(self):
        """
        Extract data from a csv file and return it for processing

        Args:
            filename: optional Name of csv file to get data from.

        """
        
        with open(self.settings.source_file, 'r', encoding='cp1252') as csvfile:
            csvreader = csv.DictReader(csvfile)  # Reader object

            self.fields = next(csvreader)  # Read header
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
        matching_indexes: list[int] = []
        for i, lp in enumerate(self.lpcollection):
            # h/t https://www.geeksforgeeks.org/python/enumerate-in-python/
            if controls.for_what.lower() in getattr(lp, self.settings.field_dict[controls.do_what]).lower():
                matching_indexes.append(i)
        return matching_indexes[:controls.how_many]

    def __repr__(self) -> str:
        return f"Total no. of rows: {len(self.lpcollection)}"  # Row count
