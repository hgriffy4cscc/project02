from pathlib import Path

class Settings:
    """class to hold settings"""

    def __init__(self) -> None:
        self.source_file = Path.cwd() / 'lps.csv'
        self.do_what: str = 'a'
        self.for_what: str = 'blue'
        self.how_many: int = 5