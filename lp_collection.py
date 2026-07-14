from lp import LP
from settings import Settings
import csv

class LPCollection:

    def __init__(self,settings) -> None:
        self.settings = Settings()
        self.title = ""
        self.fields: dict = {}
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
        #print(f"Matching indexes: {matching_indexes}")
        for i in self.matching_indexes:
            print(f"{'_'*80}")
            for f in self.fields:
                print(f"{f}: {getattr(self.lpcollection[i],f)}")

    def __repr__(self) -> str:
        return f"Total no. of rows: {len(self.lpcollection)}"  # Row count
