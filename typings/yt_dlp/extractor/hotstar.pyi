"""
This type stub file was generated by pyright.
"""

from .common import InfoExtractor

class HotStarBaseIE(InfoExtractor):
    _BASE_URL = ...
    _API_URL = ...
    _AKAMAI_ENCRYPTION_KEY = ...


class HotStarIE(HotStarBaseIE):
    IE_NAME = ...
    _VALID_URL = ...
    _TESTS = ...
    _GEO_BYPASS = ...
    _TYPE = ...
    _IGNORE_MAP = ...


class HotStarPrefixIE(InfoExtractor):
    """ The "hotstar:" prefix is no longer in use, but this is kept for backward compatibility """
    IE_DESC = ...
    _VALID_URL = ...
    _TESTS = ...


class HotStarPlaylistIE(HotStarBaseIE):
    IE_NAME = ...
    _VALID_URL = ...
    _TESTS = ...


class HotStarSeriesIE(HotStarBaseIE):
    IE_NAME = ...
    _VALID_URL = ...
    _TESTS = ...


