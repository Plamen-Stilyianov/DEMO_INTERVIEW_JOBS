class Singleton:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            cls.__instance._name = 'Singleton'
            return cls.__instance
        else:
            return cls.__instance

    def __init__(self, name, *args, **kwargs):
        super(Singleton, self).__init__()
        self._name = name

    @classmethod
    def get_instance(cls):
        return cls.__instance


class Foo(Singleton):

    def __init__(self, name):
        self._name = name

