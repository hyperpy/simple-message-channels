"""Sans I/O wire protocol for Hypercore"""
from typing import List, Optional, Tuple

import attr
from pyvarint import encode, encoding_length

__all__ = ["SimpleMessageChannel"]


@attr.s(auto_attribs=True)
class SimpleMessageChannel:
    """A simple message channel."""

    messages: List[Tuple[int, int, bytes]] = attr.Factory(list)

    varint: int = 0
    factor: int = 1
    length: int = 0
    header: int = 0
    state: int = 0
    consumed = 0
    max_size = 8 * 1024 * 1024

    def send(self, channel: int, type: int, message: bytes) -> bytes:
        """Encode a channel, type and message data to be sent.

        :param channel: the message channel identifier
        :param type: the type of message
        :param message: the message data
        """
        header = channel << 4 or type
        length = len(message) + encoding_length(header)
        return encode(length) + encode(header) + message

    def send_batch(self, messages: List[Tuple[int, int, bytes]]) -> bytes:
        """Encodes a series of messages into a single payload of bytes.

        :param messages: Several data messages
        """
        payload = b""
        for (channel, type, message) in messages:
            payload += self.send(channel, type, message)
        return payload

    def recv(self, data: bytes) -> None:
        """Encode a channel, type, message to be sent.

        :param data: the message data
        """
        offset = 0

        while offset < len(data):
            if self.state == 2:
                offset = self._read_msg(data, offset)
            else:
                offset = self._read_varint(data, offset)

        if self.state == 2 and self.length == 0:
            self._read_msg(data, offset)

    def _read_msg(self, data: bytes, offset: int) -> int:
        """TODO."""
        pass

    def _read_varint(self, data: bytes, offset: int) -> int:
        """TODO."""
        while offset < len(data):
            self.varint += (data[offset] & 127) * self.factor
            self.consumed += 1

            if data[offset] < 128:
                state = self._next_state(data, offset + 1)
                if state:
                    return offset
                return len(data)

            offset += 1

        if self.consumed >= 8:
            raise RuntimeError("Incoming varint is invalid")

        return len(data)

    def _next_state(self, data: bytes, offset: int) -> bool:
        """TODO."""
        pass
