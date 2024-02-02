import os

# Import everything from /api/ into keras.
from keras.api import *

# Add everything in /api/ to the module search path.
__path__.append(os.path.join(os.path.dirname(__file__), "api"))

# Define a version string.
__version__ = "3.0.4"
