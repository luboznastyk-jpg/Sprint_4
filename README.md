# qa_python
test_add_new_book_name -- проверить добавление книг списком без указания жанра 
test_set_book_genre_book_in_books_genre -- проверить добавление жанра книги, если книга есть в словаре и её жанр входит в список genre.
test_get_book_genre_name -- проверить вывод жанра книги по её имени.
test_get_books_with_specific_genre_list-- проверить вывод списка книг с определённым жанром.
test_get_books_genre_dict -- проверить вывод текущего словаря books_genre.
test_get_books_for_children -- проверить выбор книг, которые подходят детям: у жанра книги не должно быть возрастного рейтинга, если рейтинг есть, книга не попадает в список books_for_children
test_add_book_in_favorites -- проверить добавление в избранное 2-х книг, книги были ранее добавлены.
test_delete_book_from_favorites — проверить удаление книги из избранного, книга была ранее добавлена.
test_get_list_of_favorites_books — проверить получение списка избранных книг.