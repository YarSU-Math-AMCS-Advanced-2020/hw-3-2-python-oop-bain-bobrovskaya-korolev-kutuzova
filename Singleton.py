class Singleton(type):
    """
    Typical singleton metaclass realization
    """
    _classes = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._classes:
            cls._classes[cls] = super(Singleton, cls).__call__(*args,
                                                               **kwargs)
        return cls._classes[cls]
