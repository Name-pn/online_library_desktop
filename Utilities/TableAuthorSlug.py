from API.apps import Authors


class TableAuthorSlug():

    def __init__(self):
        self.table = {}
        self.prop = Authors.get_all()
        for el in self.prop:
            self.table[el['name'] + ' ' + el['surname']] = el['slug']