import pytest

from main import BooksCollector

@pytest.fixture 
def collector(scope = 'session'):
    collector = BooksCollector()
    return collector

@pytest.fixture
def add_book():
    collector = BooksCollector()
    collector.books_genre = {
        'Гордость и предубеждение и зомби': 'Фантастика',
        'Любимая книга': '',
        'Еще одна любимая книга': '',
        'Новая книга': 'Фантастика',
        'Неизвестная книга': 'Детективы',
        'Детская книга': 'Комедии',
        'Взрослая книга': 'Детективы'
    }
    return collector