from importlib import metadata

def get_package_name():
    with open('pyproject.toml', 'r') as f:
        for line in f:
            if line.startswith('name = '):
                return line.split('=')[1].strip().strip('"')

try:
    __version__ = metadata.version('chainlit-custom')
except metadata.PackageNotFoundError:
    # Case where package metadata is not available.
    __version__ = ""