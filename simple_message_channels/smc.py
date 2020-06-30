"""Sans I/O wire protocol for Hypercore"""

__all__ = ["SimpleMessageChannel"]


class SimpleMessageChannel:
    """A simple message channel."""

    async def send(self, channel: int, type: int, message: bytes) -> bytes:
        pass

    # TODO(decentral1se): spec out the context manager API of recv
