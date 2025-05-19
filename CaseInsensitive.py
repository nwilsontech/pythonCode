from collections import OrderedDict
from typing import Any, Iterator, Optional, Tuple, Union

class CaseInsensitiveOrderedDict(OrderedDict[str, Any]):
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__()
        self.update(*args, **kwargs)

    def _lower_key(self, key: Union[str, Any]) -> Union[str, Any]:
        return key.lower() if isinstance(key, str) else key

    def __setitem__(self, key: str, value: Any) -> None:
        super().__setitem__(self._lower_key(key), value)

    def __getitem__(self, key: str) -> Any:
        return super().__getitem__(self._lower_key(key))

    def __delitem__(self, key: str) -> None:
        super().__delitem__(self._lower_key(key))

    def __contains__(self, key: object) -> bool:
        if isinstance(key, str):
            key = key.lower()
        return super().__contains__(key)

    def get(self, key: str, default: Optional[Any] = None) -> Any:
        return super().get(self._lower_key(key), default)

    def pop(self, key: str, *args: Any) -> Any:
        return super().pop(self._lower_key(key), *args)

    def setdefault(self, key: str, default: Optional[Any] = None) -> Any:
        return super().setdefault(self._lower_key(key), default)

    def update(self, *args: Any, **kwargs: Any) -> None:
        for k, v in dict(*args, **kwargs).items():
            self[k] = v

    def keys(self) -> Iterator[str]:
        return super().keys()

    def items(self) -> Iterator[Tuple[str, Any]]:
        return super().items()

    def values(self) -> Iterator[Any]:
        return super().values()
