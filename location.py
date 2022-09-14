import inspect
from position import *
#from utility import typename

def auto_repr(cls):
    members = vars(cls)

    if "__repr__" in members:
        raise TypeError(f"{cls.__name__} already defines __repr__")

    if "__init__" not in members:
        raise TypeError(f"{cls._name__} does not override __init__")

    sig = inspect.signature(cls.__init__)
    parameter_names = list(sig.parameters)[1:]

    if not all(
        isinstance(members.get(name, None), property)
        for name in parameter_names
    ):
        raise TypeError(
            f"Cannot apply auto_repr to {cls.__name__} because not all"
            "__init__ parameters have matching properties"
        )

    def synthsized_repr(self):
        return "{typename}({args})".format(
            typename=typename(self),
            args=", ".join(
                "{name}={value!r}".format(
                    name=name,
                    value=getattr(self, name)
                ) for name in parameter_names
            )
        )

    setattr(cls, "__repr__", synthsized_repr)

    return cls

@auto_repr
class Location:

    def __init__(self, name, position):
        self._name = name
        self._position = position

    @property
    def name(self):
        return self._name

    @property
    def position(self):
        return self._position

    def __str__(self):
        return self.name

hong_kong = Location("Hong Kong", Position(22.29, 114.16))
stockholm = Location("Stockholm", Position(59.33, 18.06))
cape_town = Location("Cape Town", Position(-33.93, 18.42))
rotterdam = Location("Rotterdam", Position(51.96, 4.47))
maracaibo = Location("Maracaibo", Position(10.65, -71.65))