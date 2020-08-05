def test_smc_send(smc1):
    assert smc1.send(0, 1, b"foo") == b"\x04\x01foo"


def test_smc_recv(smc1, smc2):
    payload = smc1.send(0, 1, b"foo")
    smc2.recv(payload)

    assert len(smc2.messages) == 1
    assert smc2.messages[0] == [(0, 1, b"foo")]


def test_smc_recv_multiple(smc1, smc2):
    payload = smc1.send_batch([(0, 1, b"foo"), (0, 1, b"bar"), (0, 1, b"baz")])
    smc2.recv(payload)

    assert len(smc2.messages) == 3
    assert smc2.messages[0] == [(0, 1, b"foo"), (0, 1, b"bar"), (0, 1, b"baz")]


def test_smc_recv_empty(smc1, smc2):
    payload = smc1.send(0, 1, b"")
    smc2.recv(payload)

    assert len(smc2.messages) == 1
    assert smc2.messages[0] == [(0, 1, b"")]


def test_smc_recv_chunked(smc1, smc2):
    payload = smc1.send(0, 1, b"foo")

    for idx in range(0, len(payload)):
        smc2.recv(payload[idx, idx + 1])

    assert len(smc2.messages) == 1
    assert smc2.messages[0] == [(0, 1, b"foo")]


def test_smc_recv_chunked_multiple(smc1, smc2):
    payload = smc1.send_batch([(0, 1, b"foo"), (0, 1, b"bar"), (0, 1, b"baz")])

    for idx in range(0, len(payload)):
        smc2.recv(payload[idx, idx + 1])

    assert len(smc2.messages) == 3
    assert smc2.messages[0] == [(0, 1, b"foo"), (0, 1, b"bar"), (0, 1, b"baz")]
