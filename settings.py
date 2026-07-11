from pathlib import Path

class Settings:
    """class to hold settings"""

    def __init__(self) -> None:
        self.source_file = Path.cwd() / 'lps.csv'