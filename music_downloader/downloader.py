from enum import Enum
from pathlib import Path

from loguru import logger


class Service(Enum):
    SOUNDCLOUD = "soundcloud"
    YOUTUBE = "youtube"
    SPOTIFY = "spotify"
    BEATPORT = "beatport"


class UrlType(Enum):
    PLAYLIST = "playlist"
    SONG = "song"


class Downloader:
    def __init__(self, service_str: str, url: str, save_to: str | Path) -> None:
        self.service = self._get_service_from_string(service_str=service_str)
        self.url = url
        self.url_type = self._get_url_type(url=self.url)
        self.save_to_path = self._get_save_to_path(save_to=save_to)
        logger.info(f"Starting {self.__repr__()=}")

    @staticmethod
    def _get_service_from_string(service_str: str) -> Service:
        return Service(service_str.lower())

    @staticmethod
    def _get_url_type(url: str) -> UrlType:
        # TODO: finish
        return UrlType.SONG

    @staticmethod
    def _get_save_to_path(save_to: str | Path) -> Path:
        save_to_path = Path(save_to)

        if not save_to_path.exists():
            logger.warning(f"'save_to_path' does not exist. {save_to_path=}")
            raise FileExistsError(f"'save_to_path' does not exist. {save_to_path=}")

        return save_to_path

    def download(self) -> bool:
        logger.info("Download Starting...")

        print(f"{self.service=} {self.url=} {self.url_type=} {self.save_to_path=}")
        return True
