from music_downloader.services.base import MusicService


class SoundCloud(MusicService):
    def download_url(self, url: str) -> bool:
        return False

    def download_playlist_url(self, url: str) -> bool:
        return False
