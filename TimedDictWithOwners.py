from uuid import uuid4
from datetime import datetime
from types import TracebackType
from typing import Optional, Type

class TimedDictWithOnwers:
    def __init__(self) -> None:
        self.data = {}
        self.ttl = 5000
        self.allowKeyReuse = False
        self._current_owner = None
    def __enter__(self):
        """No owner specified by default - must use with_owner() method"""
        if self._current_owner is None:
            raise ValueError("No owner specified. Use 'with_owner' method instead of direct context manager.")
        return self
    def __exit__(self, exc_type: Optional[Type[BaseException]],
                    exc_val: Optional[BaseException],
                    exc_tb: Optional[TracebackType]) -> None:
            """Reset the current owner when exiting the context"""
            self._current_owner = None
    def with_owner(self, owner: str):
        """Method to specify the owner for the context"""
        self._current_owner = owner
        return self
    def enableKeyReuse(self):
        self.allowKeyReuse = True
    def disableKeyReuse(self):
        self.allowKeyReuse = False
    def ownerPresent(self,owner:str):
        return owner in self.data
    def set(self, key: str, value: object, owner: str = None, ttl: int = None):
        # Use current_owner if no owner specified
        effective_owner = owner if owner is not None else self._current_owner
        if effective_owner is None:
            raise ValueError("No owner specified and not in an owner context")

        if self.ownerPresent(effective_owner) and key in self.data[effective_owner]["data"] and not self.allowKeyReuse:
            print("Key already in use")
            return

        if not (self.ownerPresent(effective_owner)):
            self.data[effective_owner] = {"data": {}}

        self.data[effective_owner]["data"][key] = {
            "value": value,
            "ttl": ttl if ttl is not None else self.ttl,
            "timestamp": datetime.now()
        }
    def get(self, key: str, owner: str = None):
        effective_owner = owner if owner is not None else self._current_owner
        if effective_owner is None:
            raise ValueError("No owner specified and not in an owner context")

        if self.ownerPresent(effective_owner) and key in self.data[effective_owner]["data"]:
            return self.data[effective_owner]["data"][key]["value"]
        return None
    def getOwnersKeys(self, owner: str = None):
        effective_owner = owner if owner is not None else self._current_owner
        if effective_owner is None:
            raise ValueError("No owner specified and not in an owner context")

        if self.ownerPresent(effective_owner):
            return [x for x in self.data[effective_owner]["data"].keys()]
        return []
    def getAllOwnersData(self, owner: str = None):
        effective_owner = owner if owner is not None else self._current_owner
        if effective_owner is None:
            raise ValueError("No owner specified and not in an owner context")

        return [self.data[effective_owner]["data"][x] for x in self.getOwnersKeys(effective_owner)]
            
    def printOwners(self):
        for key in self.data:
            print(key)
    
if __name__ == '__main__':
    user1 = str(uuid4())
    user2 = str(uuid4())
    tdwo = TimedDictWithOnwers()
    tdwo.set("key1", "value1", owner=user1)
    with tdwo.with_owner(user2) as td:
        td.set("key_a","nice")
        print(td.getAllOwnersData())
    
    tdwo.printOwners()
