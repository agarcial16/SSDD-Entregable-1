"""Needed classes for implementing the Iterable interface for different types of objects."""

from typing import Optional

import RemoteTypes as rt  # noqa: F401; pylint: disable=import-error

# TODO: It's very likely that the same Iterable implementation doesn't fit
# for the 3 needed types. It is valid to implement 3 different classes implementing
# the same interface and use an object from different implementations when needed.


class Iterable(rt.Iterable):
    """Skeleton for an Iterable implementation."""

    def __init__(self, items: list[str], hash: int, remote_set) -> None:
        """Initialise the Iterable object."""
        self._buffer = items
        self._index = 0
        self._hash = hash
        self._remote_set = remote_set

    def next(self) -> str:
        """Return the next element in the buffer."""
        remoteset_hash = self._remote_set.hash()

        if remoteset_hash != self._hash:
            raise rt.CancelIteration()

        if self._index >= len(self._buffer):
            raise rt.StopIteration()
        
        item = self._buffer[self._index]
        self._index += 1
        return item
        
        

