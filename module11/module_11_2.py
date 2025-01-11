# Домашнее задание по теме "Интроспекция"
import inspect
from pprint import pprint

from Tools.scripts.make_ctype import method


def introspection_info(obj):
    info_dict = {}
    info_dict['type'] = type(obj)
    #attr = [a for a in dir(obj) if callable(getattr(obj, a))]
    #info_dict['attr'] = attr
    methods = [m[0] for m in inspect.getmembers(obj, predicate=inspect.isfunction)]
    info_dict['methods'] = methods
    info_dict['module'] = inspect.getmodule(obj)
    all_methods = [method for method in dir(obj) if callable(getattr(obj, method))]
    info_dict['all_methods'] = all_methods
    return info_dict


class MyClass():
    my_int = 0

    def my_medod_one(self):
        pass

    def my_medod_two(self):
        pass


if __name__ == "1__main__":
    number_info = introspection_info(42)
    print(number_info)
    pprint(number_info)
    my_class = MyClass
    number_info = introspection_info(my_class)
    print("-" * 120)
    print(number_info)
    pprint(number_info)

    # Вывод на консоль:
    # {'type': 'int', 'attributes': [...], 'methods': ['__abs__', '__add__', ...], 'module': '__main__'}
