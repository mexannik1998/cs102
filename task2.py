class DictAttr(dict):
    """
    Dictionary class

    >>> x = DictAttr([('one', 1), ('two', 2), ('three', 3)])
    >>> x
    {'one': 1, 'two': 2, 'three': 3}
    >>> x['three']
    3
    >>> x.get('one')
    1
    >>> x.get('five', 'missing')
    'missing'
    >>> x.one
    1
    >>> x.five
    Traceback (most recent call last):
    ...
    AttributeError
    """
    def __getattr__(self, name):
        try:
            return self[name]
        except KeyError:
            raise AttributeError
