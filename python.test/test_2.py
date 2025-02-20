import pytest


def f():
    raise SystemExit(1)


def mytest():
    with pytest.raises(SystemExit):
        f()