import pytest

from main import BooksCollector

from data import libr

@pytest.fixture ()
def collector():
    collector = BooksCollector()
    return collector

@pytest.fixture
def add_book(collector):
    collector.books_genre = libr
    return collector