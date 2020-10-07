class OldClass():
    def __init__(self) -> None:
        print('it\'s old class')


class NewClass(object):
    def __init__(self) -> None:
        print('it\'s a new class')
        print('if classes loaded initially run __init__ method')


g = OldClass()
n = NewClass()


class GetItem():
    def __init__(self):
        self.info = {
            'name': 'Yasoob',
            'country': 'Pakistan',
            'number': 12345812
        }

    def __getitem__(self, i):
        return self.info[i]


foo = GetItem()
print(foo['name'])


class GetTest():
    def __init__(self):
        self.info = {
            'name': 'Yasoob',
            'country': 'Pakistan',
            'number': 12345812
        }

foo = GetTest()
#it has occur error
#print(foo['name'])