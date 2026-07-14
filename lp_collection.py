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

    def __repr__(self) -> str:
        return f"Total no. of rows: {len(self.lpcollection)}"  # Row count
