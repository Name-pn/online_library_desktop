from pprint import pprint
from API.apps import Books, Authors, Genres

if __name__ == '__main__':
    # Authors
    authors = Authors.get_all()
    pprint(authors)

    mark_luts = Authors.get_detail('mark-lutts')
    pprint(mark_luts)

    mark_luts_books = Authors.get_books(mark_luts['slug'])
    pprint(mark_luts_books)

    # Books
    books = Books.get_all()
    pprint(books)

    generaration_p = Books.get_detail('generation-p-viktor-pelevin')
    pprint(generaration_p)

    generaration_p_comments = Books.get_comments(generaration_p['slug'])
    pprint(generaration_p_comments)

    # Genres
    genres = Genres.get_all()
    pprint(genres)

    postmodernism = Genres.get_detail('postmodernizm')
    pprint(postmodernism)

    postmodernism_books = Genres.get_books('postmodernizm')
    pprint(postmodernism_books)

    postmodernism_authors = Genres.get_authors('postmodernizm')
    pprint(postmodernism_authors)
