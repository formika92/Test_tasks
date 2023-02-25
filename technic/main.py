from functools import wraps

from technic.constants import BUDGET_CATEGORY, BUDGET_CATEGORY_BEFORE_PRICE, EXPENSIVE_CATEGORY
from technic.exception import NotAllowedMethod


class MetaClass(type):
    """
    Allows methods that an object has,
    attr __slots__ and methods in attr _available_methods
    """

    def __new__(cls, *args, **kwargs):
        available_methods_name = "_available_methods"

        allowed_attrs = set(object().__dir__())
        allowed_attrs.add("__slots__")
        allowed_attrs.add(available_methods_name)
        attrs = args[2]
        allowed_attrs = allowed_attrs.union(set(attrs.get(available_methods_name)))
        cls_attrs = {key for key in attrs.keys() if key not in ("__module__", "__qualname__", "__classcell__")}
        exclude_attrs = cls_attrs.difference(allowed_attrs)
        if exclude_attrs:
            raise NotAllowedMethod(exclude_attrs)

        return super().__new__(cls, *args)


class Technic(metaclass=MetaClass):
    __slots__ = ('name', 'price', 'availability', 'price_category')
    _available_methods = ('_get_category', 'len_name')

    def __init__(self, name: str, price: float, availability: bool) -> None:
        self.name = name
        self.price = price
        self.availability = availability
        self.price_category = self._get_category()

    def _get_category(self) -> bool:
        return BUDGET_CATEGORY if self.price <= BUDGET_CATEGORY_BEFORE_PRICE else EXPENSIVE_CATEGORY

    @property
    def len_name(self) -> int:
        return len(self.name)


notebook_1 = Technic("Lenovo", 15000, True)
notebook_2 = Technic("MSI", 25000, True)
notebook_3 = Technic("Huawei", 30000, False)


# сравнение с использованием магического метода
# также можно было бы определить метод __eq__ в классе Technic
# notebook_1.len_name.__eq__(notebook_2.len_name)


# тут декоратор, который проверяет длину наименований для атрибутов класса Technic
#
# def check_len_name(func):
#     @wraps(func)
#     def _wrapper(*args, **kwargs):
#         technics_args = [arg for arg in args if isinstance(arg, Technic)]
#         technics_kwargs = [kwarg for kwarg in kwargs.values() if isinstance(kwarg, Technic)]
#         technics_kwargs.extend(technics_args)
#         len_all_technics = len(technics_kwargs)
#         if len_all_technics >= 2:
#             print(
#                 all(technics_kwargs[i].len_name == technics_kwargs[i + 1].len_name for i in
#                     range(len_all_technics - 1)))
#         return func(*args, **kwargs)
#
#     return _wrapper
#
#
# @check_len_name
# def some(*args, **kwargs):
#     pass
#
#
# some(notebook_1, notebook_2, notebook_3)
