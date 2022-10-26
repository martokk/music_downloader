from abc import abstractmethod
from pathlib import Path


class MusicService:
    def __init__(self, save_to_path: str | Path) -> None:
        self.save_to_path = Path(save_to_path)

    @abstractmethod
    def download_url(self, url: str) -> bool:
        return False

    @abstractmethod
    def download_playlist_url(self, url: str) -> bool:
        return False
