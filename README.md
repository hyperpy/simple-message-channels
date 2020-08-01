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

smc = SimpleMessageChannel()

send = smc.send(1, 2, b"foo")
recv = smc.recv(send_payload)

print(f"send: {send}", f"recv: {recv}, sep="\n")
```

Output:

```sh

```
