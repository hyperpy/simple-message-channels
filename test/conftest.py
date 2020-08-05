import pytest

from simple_message_channels import SimpleMessageChannel as SMC


@pytest.fixture
def smc1():
    return SMC()


@pytest.fixture
def smc2():
    return SMC()
