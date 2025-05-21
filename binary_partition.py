import random

from requests.structures import CaseInsensitiveDict
from typing import TypeVar,Any, Iterable, Callable


def binary_partition(items: Iterable[Any],
                     func: Callable[[Any], bool]) -> tuple[list[Any], list[Any]]:
    parts = ([], [])
    for item in items:
        parts[func(item)].append(item)
    return parts[1], parts[0]

class TSimulation:
    def __init__(self):
        self.alive = random.randint(1,2)%2==0
    def is_alive(self)->bool:
        return self.alive
    def __repr__(self):
        return f"TSimulation({self.alive})"

def alive_partition_func(val: Any)->bool:
    if getattr(val, 'is_alive'):
        return val.is_alive()
    else:
        return False

def binary_example()->None:
    search_space = [TSimulation() for _ in range(10)]
    ll, rr = binary_partition(search_space, alive_partition_func)
    print(ll)
    print()
    print(rr)

if __name__ == '__main__':
    binary_example()
