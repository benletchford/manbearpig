from .context import project
from project import Something


def test_greeting():
    something = Something(name='Stan Darsh')

    assert something.greet() == 'Hello there, Stan Darsh!'
