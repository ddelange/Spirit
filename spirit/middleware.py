from spirit.core.middleware import PrivateForumMiddleware, XForwardedForMiddleware
from spirit.user.middleware import (
    ActiveUserMiddleware,
    LastIPMiddleware,
    LastSeenMiddleware,
    TimezoneMiddleware,
)

from .core.utils.deprecations import warn

warn(
    "This will get removed in Spirit 0.7. "
    "Use spirit.core.middleware.XForwardedForMiddleware, "
    "spirit.core.middleware.PrivateForumMiddleware, "
    "spirit.user.middleware.TimezoneMiddleware, "
    "spirit.user.middleware.LastIPMiddleware, "
    "spirit.user.middleware.LastSeenMiddleware and "
    "spirit.user.middleware.ActiveUserMiddleware instead"
)


__all__ = [
    "XForwardedForMiddleware",
    "PrivateForumMiddleware",
    "TimezoneMiddleware",
    "LastIPMiddleware",
    "LastSeenMiddleware",
    "ActiveUserMiddleware",
]
