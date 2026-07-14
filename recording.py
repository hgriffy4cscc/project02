from abc import ABC, abstractmethod

class Recording(ABC):
    """class for a recording in any medium"""
    def __init__(self, artist, title) -> None:
        self.artist = artist
        self.title = title
    
    @abstractmethod
    def output_for_catalog(self):
        pass

    @abstractmethod
    def add_to_playlist(self, playlist):
        pass