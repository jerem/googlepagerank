# Copyright (c) 2007 Thomas Lotze
# See also LICENSE.txt

"""Requesting a URL's page rank from Google and parsing the response.

The hash algorithm and query string assembly have been implemented after the
WWW::Google::PageRank Perl module by Yuri Karaban, who says he took the
knowledge from the pagerankstatus Mozilla extension in turn.
"""

import urllib
import re


HOST = "toolbarqueries.google.com"


def _cutoff32(value):
    """Map the value to a 32-bit positive integer.
    """
    return value % 0x100000000


def _le_encode(value):
    """Encode an integer into 4 bytes in little-endian order.
    """
    value = _cutoff32(value)
    return [value >> 8*i & 0xff for i in (0, 1, 2, 3)]


def _le_decode(value):
    """Decode 4 bytes in little-endian order into an integer.
    """
    return sum(c << 8*i for i, c in enumerate(value[:4]))


def _mix(a, b, c):
    """Transform an integer triple in an irrversible (?) way.
    """
    c = _cutoff32(c)
    a = _cutoff32(a-b-c) ^ c >> 13
    b = _cutoff32(b-c-a) ^ _cutoff32(a << 8)
    c = _cutoff32(c-a-b) ^ b >> 13
    a = _cutoff32(a-b-c) ^ c >> 12
    b = _cutoff32(b-c-a) ^ _cutoff32(a << 16)
    c = _cutoff32(c-a-b) ^ b >> 5
    a = _cutoff32(a-b-c) ^ c >> 3
    b = _cutoff32(b-c-a) ^ _cutoff32(a << 10)
    c = _cutoff32(c-a-b) ^ b >> 15
    return a, b, c


def _checksum(value):
    """Reduce a sequence of integers to a hash value.
    """
    a, b, c = 0x9e3779b9, 0x9e3779b9, 0xe6359a60

    index = 0
    while index <= len(value)-12:
        a, b, c = _mix(
            a + _le_decode(value[index:index+4]),
            b + _le_decode(value[index+4:index+8]),
            c + _le_decode(value[index+8:index+12]))
        index += 12

    a, b, c = _mix(
        a + _le_decode(value[index:index+4]),
        b + _le_decode(value[index+4:index+8]),
        c + (_le_decode(value[index+8:])<<8) + len(value))

    return c


def checksum(value):
    """Double-fold a sequence of integers into a hash value.
    """
    ch = _checksum([ord(c) for c in value])
    ch = ((ch % 0x0d) & 7) | ((ch/7) << 2)
    return _checksum(sum((_le_encode(ch-9*i) for i in xrange(20)), []))


def query_url(target):
    """Compose a query URL for target containing a computed checksum.

    target: str, a URL

    returns str
    """
    query = "info:"+target
    params = urllib.urlencode({
        "client": "navclient-auto",
        "ch": "6%s" % checksum(query),
        "ie": "UTF-8",
        "oe": "UTF-8",
        "features": "Rank",
        "q": query,
        })
    return "http://%s/search?%s" % (HOST, params)


def read_rank(response):
    """Read the pagerank from Google's response.

    response: str, HTTP response body

    returns str or raises ValueError if a pagerank wasn't found
    """
    groups = re.findall("^Rank_\d+:\d+:(\d+)$", response.strip())
    if len(groups) == 1:
        return groups[0]
    else:
        raise ValueError
