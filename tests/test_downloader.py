# pyright: reportPrivateUsage=false
# pylint: disable=protected-access, redefined-outer-name
from pathlib import Path

import pytest

from music_downloader.downloader import Downloader, Service


@pytest.fixture
def downloader() -> Downloader:
    return Downloader(service_str="soundcloud", url="https://www.soundcloud.com", save_to="/tmp")


@pytest.mark.parametrize(
    ("service_str", "expected"),
    [
        ("soundcloud", Service.SOUNDCLOUD),
        ("Soundcloud", Service.SOUNDCLOUD),
        ("SoundCloud", Service.SOUNDCLOUD),
        ("youtube", Service.YOUTUBE),
        ("spotify", Service.SPOTIFY),
        ("beatport", Service.BEATPORT),
    ],
)
def test_get_service_from_string(
    downloader: Downloader, service_str: str, expected: Service
) -> None:
    assert downloader._get_service_from_string(service_str=service_str) == expected


@pytest.mark.parametrize(
    ("service_str", "expected"),
    [
        ("wrong_service", "'wrong_service' is not a valid Service"),
        ("soundclouds", "'soundclouds' is not a valid Service"),
    ],
)
def test_get_invalid_service_from_string(
    downloader: Downloader, service_str: str, expected: str
) -> None:
    with pytest.raises(ValueError, match=expected):
        downloader._get_service_from_string(service_str=service_str)


@pytest.mark.parametrize(
    ("save_to", "expected"),
    [
        ("/tmp", Path("/tmp")),
    ],
)
def test_get_save_to_path(downloader: Downloader, save_to: str, expected: Path) -> None:
    assert downloader._get_save_to_path(save_to=save_to) == expected


@pytest.mark.parametrize(
    ("save_to"),
    [
        ("/tmp99"),
        ("/tmp1234"),
    ],
)
def test_get_invalid_save_to_path(downloader: Downloader, save_to: str) -> None:
    with pytest.raises(FileExistsError):
        downloader._get_save_to_path(save_to=save_to)
