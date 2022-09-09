from unittest.mock import Mock

import pytest
from pytest_mock import MockerFixture


def pytest_sessionfinish(session, exitstatus) -> None:
    """If pytest fails because of no tests to run, it should succeed instead"""
    if exitstatus == 5:
        session.exitstatus = 0


@pytest.fixture
def open_mock(mocker: MockerFixture) -> Mock:
    return mocker.patch("builtins.open")
