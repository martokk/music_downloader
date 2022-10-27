"""
This type stub file was generated by pyright.
"""

import socket

__author__ = ...
SOCKS4_VERSION = ...
SOCKS4_REPLY_VERSION = ...
SOCKS4_DEFAULT_DSTIP = ...
SOCKS5_VERSION = ...
SOCKS5_USER_AUTH_VERSION = ...
SOCKS5_USER_AUTH_SUCCESS = ...
class Socks4Command:
    CMD_CONNECT = ...
    CMD_BIND = ...


class Socks5Command(Socks4Command):
    CMD_UDP_ASSOCIATE = ...


class Socks5Auth:
    AUTH_NONE = ...
    AUTH_GSSAPI = ...
    AUTH_USER_PASS = ...
    AUTH_NO_ACCEPTABLE = ...


class Socks5AddressType:
    ATYP_IPV4 = ...
    ATYP_DOMAINNAME = ...
    ATYP_IPV6 = ...


class ProxyError(socket.error):
    ERR_SUCCESS = ...
    def __init__(self, code=..., msg=...) -> None:
        ...
    


class InvalidVersionError(ProxyError):
    def __init__(self, expected_version, got_version) -> None:
        ...
    


class Socks4Error(ProxyError):
    ERR_SUCCESS = ...
    CODES = ...


class Socks5Error(ProxyError):
    ERR_GENERAL_FAILURE = ...
    CODES = ...


class ProxyType:
    SOCKS4 = ...
    SOCKS4A = ...
    SOCKS5 = ...


Proxy = ...
class sockssocket(socket.socket):
    def __init__(self, *args, **kwargs) -> None:
        ...
    
    def setproxy(self, proxytype, addr, port, rdns=..., username=..., password=...): # -> None:
        ...
    
    def recvall(self, cnt): # -> bytes:
        ...
    
    def connect(self, address): # -> None:
        ...
    
    def connect_ex(self, address): # -> int:
        ...
    


