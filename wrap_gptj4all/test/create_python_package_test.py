from pathlib import PosixPath, Path
from tempfile import NamedTemporaryFile
from contextlib import contextmanager
from string import ascii_letters, digits
from random import choice, randint
from wrap_gptj4all import WrapGPTJ4All
@contextmanager

def test_init():
    gpt = WrapGPTJ4All()
    assert isinstance(gpt, WrapGPTJ4All)

def test_can_start():
    gpt = WrapGPTJ4All()
    assert not gpt.is_alive()
    gpt.start()
    assert gpt.is_alive()