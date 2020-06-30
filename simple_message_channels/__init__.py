"""simple-message-channels module."""

from simple_message_channels.smc import SimpleMessageChannel  # noqa

try:
    import pkg_resources
except ImportError:
    pass


try:
    __version__ = pkg_resources.get_distribution('simple_message_channels').version
except Exception:
    __version__ = 'unknown'
