import pytest

from main import BooksCollector

from data import my_books, genre, parametres, favorites, libr

class TestBooksCollector:

    @pytest.mark.parametrize("book_names", [list(libr.keys()),favorites])
    def test_add_new_book_name(self, collector, book_names):
        
        for book_name in book_names:
            collector.add_new_book(book_name)
        assert len(list(collector.books_genre.keys()))  == len(book_names)


    def test_set_book_genre_book_in_books_genre(self, add_book):

        add_book.set_book_genre(my_books[0], genre[0])
        assert add_book.books_genre[my_books[0]] == genre[0]

    @pytest.mark.parametrize("book_name, genre", parametres)
    def test_get_book_genre_name(self, collector, book_name, genre):
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, genre)
        assert collector.get_book_genre(book_name) == genre

    
    @pytest.mark.parametrize("book_name, genre", parametres)
    def test_get_books_with_specific_genre_list(self, collector, book_name, genre):
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, genre)
        assert collector.get_books_with_specific_genre(genre) == [book_name]

    def test_get_books_genre_dict(self, add_book):

        assert add_book.get_books_genre() == libr


    def test_get_books_for_children(self, add_book):

        assert "Детская книга" in add_book.get_books_for_children()
        assert "Взрослая книга" not in add_book.get_books_for_children()


    @pytest.mark.parametrize("book_name", favorites)
    def test_add_book_in_favorites(self, book_name, add_book):

        add_book.add_book_in_favorites(book_name)
        assert book_name in add_book.favorites

    def test_delete_book_from_favorites(self, collector):
        
        collector.add_new_book('book_name')
        collector.add_book_in_favorites('book_name')
        collector.delete_book_from_favorites('book_name')
        assert 'book_name' not in collector.favorites

    def test_get_list_of_favorites_books(self, add_book):
        for favorite in favorites:
            add_book.add_book_in_favorites(favorite)
        assert add_book.get_list_of_favorites_books() == favorites


