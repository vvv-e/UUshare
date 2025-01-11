# Домашнее задание по теме "Интроспекция"
import inspect
from pprint import pprint


def introspection_info(obj):
    info_dict = {}
    # type
    info_dict['type'] = type(obj)
    # attributes
    attributes = [a for a in dir(obj) if not callable(getattr(obj, a))]
    info_dict['attributes'] = attributes
    # all methods
    methods = [a for a in dir(obj) if callable(getattr(obj, a))]
    info_dict['all methods'] = methods
    # class methods
    methods = [m[0] for m in inspect.getmembers(obj, predicate=inspect.isfunction)]
    info_dict['class methods'] = methods
    # module
    info_dict['module'] = inspect.getmodule(obj)
    return info_dict


class MyClass():
    my_class_int = 0

    def __init__(self):
        self.my_int = 0

    def my_medod_one(self):
        pass

    def my_medod_two(self):
        pass


if __name__ == "__main__":
    my_class = MyClass
    number_info = introspection_info(my_class)
    pprint(number_info)
    print("-" * 120)
    number_info = introspection_info(42)
    pprint(number_info)

    # Вывод на консоль:
    # {'type': 'int', 'attributes': [...], 'methods': ['__abs__', '__add__', ...], 'module': '__main__'}
