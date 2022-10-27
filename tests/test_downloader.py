# pyright: reportPrivateUsage=false
# pylint: disable=protected-access, redefined-outer-name
from pathlib import Path

import pytest

from music_downloader.downloader import Downloader


@pytest.fixture
def downloader() -> Downloader:
    return Downloader(url="https://www.soundcloud.com", save_to=str(Path.home()))


@pytest.mark.parametrize(
    ("save_to", "expected"),
    [
        (str(Path.home()), Path.home()),
    ],
)
def test_get_save_to_path(downloader: Downloader, save_to: str, expected: Path) -> None:
    assert downloader._get_save_to_path(save_to=save_to) == expected


@pytest.mark.parametrize(
    ("save_to"),
    [
        ("/11tmp99"),
        ("/11tmp1234"),
    ],
)
def test_get_invalid_save_to_path(downloader: Downloader, save_to: str) -> None:
    with pytest.raises(FileExistsError):
        downloader._get_save_to_path(save_to=save_to)
