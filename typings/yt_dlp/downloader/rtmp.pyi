"""
This type stub file was generated by pyright.
"""

from .common import FileDownloader

def rtmpdump_version(): # -> str | Any | Literal[False]:
    ...

class RtmpFD(FileDownloader):
    def real_download(self, filename, info_dict):
        ...
    


