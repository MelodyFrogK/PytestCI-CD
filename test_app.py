# test_app.py
from app import some_function, SomeClass

def test_some_function():
    assert some_function() is None

def test_SomeClass():
    assert isinstance(SomeClass(), SomeClass)

