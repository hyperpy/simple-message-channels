"""simple-message-channels module."""

try:
    import pkg_resources
except ImportError:
    pass


try:
    __version__ = pkg_resources.get_distribution('simple-message-channels').version
except Exception:
    __version__ = 'unknown'
