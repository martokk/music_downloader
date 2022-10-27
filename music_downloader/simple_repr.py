class SimpleRepr:
    """
    A mixin implementing a simple __repr__.
    https://stackoverflow.com/questions/44595218/python-repr-for-all-member-variables
    """

    def __repr__(self) -> str:
        class_ = self.__class__.__name__
        attrs = ", ".join("{}={!r}".format(k, v) for k, v in self.__dict__.items())
        return f"{class_}({attrs})"

    def __str__(self) -> str:
        return self.__repr__()
