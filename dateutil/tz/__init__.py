from .tz import *

#: Convenience constant providing a :class:`tzutc()` instance
#:
#: .. versionadded:: 2.7.0
UTC = tzutc()

__all__ = ["tzutc", "tzoffset", "tzlocal", "tzfile", "tzrange",
           "tzstr", "tzical", "tzwin", "tzwinlocal", "gettz",
           "enfold", "datetime_ambiguous", "datetime_exists",
           "UTC"]
