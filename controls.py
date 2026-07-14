from settings import Settings

class Controls:
    """class to handle user interactions"""

    def __init__(self, settings: Settings) -> None:
        self.settings = settings

        # menu controls
        self.do_what: str = settings.do_what
        self.for_what: str = settings.for_what
        self.how_many: int = settings.how_many

        ###### READ DATA FROM CSV ######

    ###### PROMPT USER AND GATHER INPUT ######
    def do_menu_and_response(self):
        """
        Prompt user for input and return that input in variables

        """
        is_get_do_what_valid = False
        while not is_get_do_what_valid:
            self.do_what = input("What would you like to do? q to quit, "
                                    "a to search by artist, t to search by title: ").lower()
            if len(self.do_what) == 1 and self.do_what in 'qat':
                is_get_do_what_valid = True
        if self.do_what != 'q': #if user quitting, don't prompt for additional input
            is_get_for_what_valid = False
            while not is_get_for_what_valid:
                self.for_what: str = input("Enter text to search for: ")
                if self.for_what:
                    is_get_for_what_valid = True
            raw_how_many = input("How many results would you like? (zero to display all): ")
            # integer-checking code adapted from
            # https://www.geeksforgeeks.org/python/check-if-string-is-integer-in-python/
            try:
                self.how_many = int(raw_how_many)
            except ValueError:
                self.how_many = 0