"""
This type stub file was generated by pyright.
"""

from .common import InfoExtractor

class AdobeTVBaseIE(InfoExtractor):
    ...


class AdobeTVEmbedIE(AdobeTVBaseIE):
    IE_NAME = ...
    _VALID_URL = ...
    _TEST = ...


class AdobeTVIE(AdobeTVBaseIE):
    IE_NAME = ...
    _VALID_URL = ...
    _TEST = ...


class AdobeTVPlaylistBaseIE(AdobeTVBaseIE):
    _PAGE_SIZE = ...


class AdobeTVShowIE(AdobeTVPlaylistBaseIE):
    IE_NAME = ...
    _VALID_URL = ...
    _TEST = ...
    _RESOURCE = ...
    _process_data = ...


class AdobeTVChannelIE(AdobeTVPlaylistBaseIE):
    IE_NAME = ...
    _VALID_URL = ...
    _TEST = ...
    _RESOURCE = ...


class AdobeTVVideoIE(AdobeTVBaseIE):
    IE_NAME = ...
    _VALID_URL = ...
    _EMBED_REGEX = ...
    _TEST = ...


