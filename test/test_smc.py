async def test_send_recv(smc):
    channel, type, message = 0, 0, b"abc"

    payload = await smc.send(channel, type, message)
    assert isinstance(payload, bytes)

    async with smc.recv(payload) as response:
        assert response.channel == channel
        assert response.type == type
        assert response.message == message
