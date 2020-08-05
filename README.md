# simple-message-channels

[![Build Status](https://drone.autonomic.zone/api/badges/hyperpy/simple-message-channels/status.svg)](https://drone.autonomic.zone/hyperpy/simple-message-channels)

## Sans I/O wire protocol for Hypercore

## Install

```sh
$ pip install simple-message-channels
```

## Example

```python
from simple_message_channels import SimpleMessageChannel

smc1 = SimpleMessageChannel()
smc2 = SimpleMessageChannel()

payload = smc1.send(0, 1, b"foo")
print(f"sent: {payload}")

for idx in range(0, len(payload)):
    smc2.recv(payload[idx : idx + 1])
print(f"received: {smc2.messages}")
```

Output:

```sh
sent: b'\x04\x01foo'
received: [(0, 1, b'foo')]
```
