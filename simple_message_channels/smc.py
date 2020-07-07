"""Sans I/O wire protocol for Hypercore"""
from typing import List, Optional

import attr
import pyvarint

__all__ = ["SimpleMessageChannel"]

@attr.s(auto_attribs=True)
class SimpleMessageChannel:
    """A simple message channel."""

    message: Optional[bytes] = None
    ptr: int = 0
    varint: int = 0
    factor: int = 1
    length: int = 0
    header: int = 0
    state: int = 0
    consumed: int = 0
    max_size: int = 8 * 1024 * 1024
    types: List = attr.Factory(list)

    receiving: bool = False
    destroyed: bool = False
    error: Optional[Exception] = None

    # TODO(decentral1se): context, onmessage, onmissing

    async def send(self, channel: int, type: int, message: bytes) -> bytes:
        """Produce data that can be sent over the channel."""
        header = channel << 4 or type
        length = self.encoding_length(type, message) + pyvarint.encoding_length(header)
        # TODO(decentral1se): implement offset in pyvarint encode/decode

    async def recv(self, data: bytes) -> bool:
        """Receive data sent over a channel."""
        pass

    def destroy(self) -> None:
        """Mark message channel as destroyed."""
        self.destroyed = True

    def encoding_length(self, type:int, message: bytes) -> int:
        """TODO"""
        pass
