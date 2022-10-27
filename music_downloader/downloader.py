import os
from pathlib import Path

from loguru import logger
from yt_dlp import YoutubeDL

from music_downloader.simple_repr import SimpleRepr


class Downloader(SimpleRepr):
    def __init__(self, url: str, save_to: str | Path) -> None:
        self.url = url
        self.save_to_path = self._get_save_to_path(save_to=save_to)
        logger.debug(f"Starting {self.__repr__()}")

    @staticmethod
    def _get_save_to_path(save_to: str | Path) -> Path:
        save_to_path = Path(save_to)

        if not save_to_path.exists():
            logger.warning(f"'save_to_path' does not exist. {save_to_path=}")
            raise FileExistsError(f"'save_to_path' does not exist. {save_to_path=}")

        return save_to_path

    def download(self) -> bool:
        logger.info(f"Download Starting... {self.url=} {self.save_to_path=}")

        opts = {
            "outtmpl": os.path.join(f"{self.save_to_path}", "%(title).100s - %(uploader)s.%(ext)s")
        }
        with YoutubeDL(opts) as ydl:
            ydl.download(self.url)
        return True
