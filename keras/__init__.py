# Import everything from /api/ into keras.
from keras.api import *

# Add everything in /api/ to the module search path.
import os
__path__.append(os.path.join(os.path.dirname(__file__), "api"))
del os

# Define a version string.
__version__ = "3.0.5"

def __dir__():
    keys = dict.fromkeys((globals().keys()))
    keys.pop("src")
    keys.pop("api")
    return list(keys)
