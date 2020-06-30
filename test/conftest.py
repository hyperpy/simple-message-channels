import pytest


@pytest.fixture
def smc():
    from simple_message_channels import SimpleMessageChannel

    return SimpleMessageChannel()
