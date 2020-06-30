"""Sans I/O wire protocol for Hypercore"""

__all__ = ["SimpleMessageChannel"]

from typing import List, Optional

import attr


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

    # TODO(decentral1se): need to lookup type of what is being passed in
    # context: ???

    # TODO(decentral1se): allow to override instead of callback interface!?
    # onmissing: ???
    # onmessage: ???

    async def send(self, channel: int, type: int, message: bytes) -> bytes:
        pass

    # TODO(decentral1se): spec out the context manager API of recv
