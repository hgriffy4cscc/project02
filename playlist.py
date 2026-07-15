"""class to manage playlists -- currently only built out for randomized playlist"""
from lp_collection import LPCollection

class Playlist:
    """class to manage a playlist of lps"""

    def __init__(self) -> None:
        pass

class RandomPlaylist(LPCollection):
    """class to manage random playlist of LPs"""
    def __init__(self, settings, full_collection):
        super().__init__(settings)
        self.lpcollection = full_collection.lpcollection
        self.fields = full_collection.fields

    ##### BUILD A RANDOMIZED PLAYLIST #####
    def build_random_playlist(self,controls):
        """method to generate and store a random set of LPs"""
        import random
        self.matching_indexes = []
        for _ in range(controls.how_many):
            self.matching_indexes.append(random.randrange(len(self.lpcollection)))

    ##### EXPORT TO FILE #####
    def save_results_to_file(self,controls) -> bool:
        """ method to export a random playlist to a file"""
        from pathlib import Path
        output = f"Here is a random playlist with {len(self.matching_indexes)} albums.\n"
        for i in self.matching_indexes:
            output += self.lpcollection[i].output_for_catalog(self)
        try:
            path = Path(controls.save_file_path_txt + '.txt')
        except FileNotFoundError:
            print("That file does not seem to exist. Let's try again.")
            return False
        try:
            with path.open("w",encoding="utf-8") as fil:
                fil.write(output)
        except PermissionError:
            print("Sorry, could not write to that file. Let's try again.")
            return False
        return True
