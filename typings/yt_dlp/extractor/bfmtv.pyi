"""
This type stub file was generated by pyright.
"""

from .common import InfoExtractor

class BFMTVBaseIE(InfoExtractor):
    _VALID_URL_BASE = ...
    _VALID_URL_TMPL = ...
    _VIDEO_BLOCK_REGEX = ...
    BRIGHTCOVE_URL_TEMPLATE = ...


class BFMTVIE(BFMTVBaseIE):
    IE_NAME = ...
    _VALID_URL = ...
    _TESTS = ...


class BFMTVLiveIE(BFMTVIE):
    IE_NAME = ...
    _VALID_URL = ...
    _TESTS = ...


class BFMTVArticleIE(BFMTVBaseIE):
    IE_NAME = ...
    _VALID_URL = ...
    _TESTS = ...


