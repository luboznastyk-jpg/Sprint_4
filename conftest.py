import pytest

from main import BooksCollector

from data import libr

@pytest.fixture 
def collector(scope = 'session'):
    collector = BooksCollector()
    return collector

@pytest.fixture
def add_book():
    collector.books_genre = libr
    return collector