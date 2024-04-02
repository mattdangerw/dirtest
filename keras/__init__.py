# Import everything from /api/ into keras.
from keras.api import *
from keras.api import __version__

import os

# Add everything in /api/ to the module search path.
__path__.append(os.path.join(os.path.dirname(__file__), "api"))

# Don't pollute namespace.
del os

# Never autocomplete `.src` or `.api` on an imported keras object.
def __dir__():
    keys = dict.fromkeys((globals().keys()))
    keys.pop("src")
    keys.pop("api")
    return list(keys)


# Never autocomplete `.src` or `.api` during an import statement.
__all__ = [
    name
    for name in globals().keys()
    if not (name.startswith("_") or name in ("src", "api"))
]
