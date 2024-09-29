from importlib import metadata

try:
    __version__ = metadata.version('chainlit-custom')
except metadata.PackageNotFoundError:
    # Case where package metadata is not available.
    __version__ = ""