"""
This type stub file was generated by pyright.
"""

from .common import InfoExtractor

class SVTBaseIE(InfoExtractor):
    _GEO_COUNTRIES = ...


class SVTIE(SVTBaseIE):
    _VALID_URL = ...
    _EMBED_REGEX = ...
    _TEST = ...


class SVTPlayBaseIE(SVTBaseIE):
    _SVTPLAY_RE = ...


class SVTPlayIE(SVTPlayBaseIE):
    IE_DESC = ...
    _VALID_URL = ...
    _TESTS = ...


class SVTSeriesIE(SVTPlayBaseIE):
    _VALID_URL = ...
    _TESTS = ...
    @classmethod
    def suitable(cls, url): # -> bool:
        ...
    


class SVTPageIE(InfoExtractor):
    _VALID_URL = ...
    _TESTS = ...
    @classmethod
    def suitable(cls, url): # -> bool:
        ...
    


