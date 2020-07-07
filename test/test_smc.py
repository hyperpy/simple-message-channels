async def test_send_produces_bytes(smc):
    channel, type, message = 0, 0, b"abc"

    payload = await smc.send(channel, type, message)
    assert isinstance(payload, bytes)
