import collections
import inspect

from flask_restful import fields


class Serializer(collections.MutableMapping):

    def __init__(self, *args, **kwargs):
        self.store = dict()
        self.update(dict(*args, **kwargs))

        cls_attrs = inspect.getmembers(self, lambda attr: not (inspect.isroutine(attr)))
        attrs = [a for a in cls_attrs if not (a[0].startswith('__') and a[0].endswith('__') or a[0].startswith('_'))]
        for attr in attrs:
            self.store[attr[0]] = attr[1]

    def __getitem__(self, key):
        return self.store[self.__keytransform__(key)]

    def __setitem__(self, key, value):
        self.store[self.__keytransform__(key)] = value

    def __delitem__(self, key):
        del self.store[self.__keytransform__(key)]

    def __iter__(self):
        return iter(self.store)

    def __len__(self):
        return len(self.store)

    def __keytransform__(self, key):
        return key


class IPv4Serializer(Serializer):
    name = fields.String
    value = fields.String
