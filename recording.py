"""define abstract base class Recording -- for use by LP class"""
from abc import ABC, abstractmethod

class Recording(ABC):
    """class for a recording in any medium"""
    def __init__(self, artist, title) -> None:
        self.artist = artist
        self.title = title

    @abstractmethod
    def output_for_catalog(self, collection) -> str:
        """method to output data about this recording.
            maybe should be repr or print but wanted to include argument"""

    @abstractmethod
    def add_to_playlist(self, playlist) -> None:
        """ method to add this recording to a playlist"""
