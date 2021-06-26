from typing import List


class dictarray(dict):
    def __getitem__(self, k: str) -> List:
        return super().__getitem__(k)

    def __setitem__(self, k: str, v: List) -> None:
        if type(v).__name__ != 'list':
            raise BaseException("dictarray only accepts List as parameter")
        return super().__setitem__(k, v)

    def add(self, key: str, val: any):
        self[key].append(val)

    def remove(self, key: str, val: any):
        self[key].remove(val)
