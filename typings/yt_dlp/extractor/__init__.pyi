"""
This type stub file was generated by pyright.
"""

from ..compat.compat_utils import passthrough_module

def gen_extractor_classes(): # -> list[Any]:
    """ Return a list of supported extractors.
    The order does matter; the first extractor matched is the one handling the URL.
    """
    ...

def gen_extractors(): # -> list[Any]:
    """ Return a list of an instance of every supported extractor.
    The order does matter; the first extractor matched is the one handling the URL.
    """
    ...

def list_extractor_classes(age_limit=...): # -> Generator[Any | Type[GenericIE], None, None]:
    """Return a list of extractors that are suitable for the given age, sorted by extractor name"""
    ...

def list_extractors(age_limit=...): # -> list[Any | GenericIE]:
    """Return a list of extractor instances that are suitable for the given age, sorted by extractor name"""
    ...

def get_info_extractor(ie_name): # -> Any:
    """Returns the info extractor class with the given ie_name"""
    ...

