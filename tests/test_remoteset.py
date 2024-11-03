"""Tests for RemoteSet class."""

import unittest

from remotetypes import RemoteTypes
from remotetypes.remoteset import RemoteSet
from remotetypes.iterable import Iterable

class TestRemoteSet(unittest.TestCase):
    def setUp(self):
        # Instancia directamente RemoteSet en lugar de usar Ice
        self.remote_set = RemoteSet()

    def test_add_and_contains(self):
        """Checl adding an element and its existence in the RemoteSet."""
        self.remote_set.add("test")
        self.assertTrue(self.remote_set.contains("test"))

    def test_length(self):
        """Check length method after adding elements in the RemoteSet."""
        self.remote_set.add("item1")
        self.remote_set.add("item2")
        self.assertEqual(self.remote_set.length(), 2)

    def test_remove(self):
        """Check you can remove a element in the RemoteSet."""
        self.remote_set.add("remove")
        self.remote_set.remove("remove")
        self.assertFalse(self.remote_set.contains("remove"))

    def test_iter(self):
        """Check iteration functionality works in the RemoteSet."""
        self.remote_set.add("item1")
        self.remote_set.add("item2")

        iterable = Iterable(list(self.remote_set._storage_), self.remote_set.hash(), self.remote_set)
        items = []
        try:
            while True:
                items.append(iterable.next())
        except RemoteTypes.StopIteration:
            pass

        self.assertIn("item1", items)
        self.assertIn("item2", items)
        self.assertEqual(len(items), 2)

    def test_iter_cancel_iteration(self):
        """Check CancelIteration is raised when changing the set during the iteration."""
        self.remote_set.add("item")
        iterable = Iterable(list(self.remote_set._storage_), self.remote_set.hash(), self.remote_set)

        self.remote_set.add("new_item")

        with self.assertRaises(RemoteTypes.CancelIteration):
            iterable.next()