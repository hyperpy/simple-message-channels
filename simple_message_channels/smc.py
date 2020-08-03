"""Sans I/O wire protocol for Hypercore"""
from typing import List, Tuple

import attr
from pyvarint import encode, encoding_length

__all__ = ["SimpleMessageChannel"]


@attr.s(auto_attribs=True)
class SimpleMessageChannel:
    """A simple message channel."""

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

    def recv(self, data: bytes) -> Tuple[int, int, bytes]:
        """Encode a channel, type, message to be sent.

        :param data: the message data
        """
        pass
