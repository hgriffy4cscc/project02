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
    def _get_do_what(self):
        is_get_do_what_valid = False
        while not is_get_do_what_valid:
            raw_do_what = input(f"What would you like to do? [enter for default {self.settings.do_what}]\n" \
                               "q to quit, a to search by artist, t to search by title: ").lower()
            if len(raw_do_what) == 0:
                self.do_what = self.settings.do_what
                is_get_do_what_valid = True
            elif len(raw_do_what) == 1 and raw_do_what in 'qat':
                self.do_what = raw_do_what
                is_get_do_what_valid = True

    def _get_for_what(self):
        self.for_what: str = input(f"Enter text to search for: [enter for default {self.settings.for_what}] ")
        if not self.for_what:
            self.for_what = self.settings.for_what

    def _get_how_many(self):
        raw_how_many = input(f"How many results would you like? [0 for all, enter for default {self.settings.how_many}]: ")
        # integer-checking code adapted from
        # https://www.geeksforgeeks.org/python/check-if-string-is-integer-in-python/
        if len(raw_how_many) == 0:
            self.how_many = self.settings.how_many
        else:
            try:
                self.how_many = int(raw_how_many)
            except ValueError:
                self.how_many = self.settings.how_many

    def do_menu_and_response(self):
        """
        Prompt user for input and return that input in variables

        """
        self._get_do_what()

        if self.do_what == 'q':  #if user quitting, don't prompt for additional input
            return False

        self._get_for_what()
        self._get_how_many()
#        print(f"Gathered values are: do_what: {self.do_what} + for_what: {self.for_what} + how_many: {self.how_many}")

