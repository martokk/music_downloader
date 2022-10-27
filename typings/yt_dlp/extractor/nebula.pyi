"""
This type stub file was generated by pyright.
"""

from .common import InfoExtractor

_BASE_URL_RE = ...
class NebulaBaseIE(InfoExtractor):
    _NETRC_MACHINE = ...
    _nebula_api_token = ...
    _nebula_bearer_token = ...
    _zype_access_token = ...


class NebulaIE(NebulaBaseIE):
    _VALID_URL = ...
    _TESTS = ...


class NebulaSubscriptionsIE(NebulaBaseIE):
    IE_NAME = ...
    _VALID_URL = ...
    _TESTS = ...


class NebulaChannelIE(NebulaBaseIE):
    IE_NAME = ...
    _VALID_URL = ...
    _TESTS = ...


