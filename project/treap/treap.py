from collections.abc import MutableMapping
import random

class TreapNode:
    def __init__(self, key, value, priority=None):
        self.key = key
        self.value = value
        self.priority = priority if priority is not None else random.randint(1, 100)
        self.left = None
        self.right = None

class Treap(MutableMapping):
    def __init__(self):
        self.root = None

    def _split(self, node, key):
        """Splits tree rooted at node into two trees based on key."""
        if not node:
            return None, None
        elif key > node.key:
            node.right, t2 = self._split(node.right, key)
            return node, t2
        else:
            t1, node.left = self._split(node.left, key)
            return t1, node

    def _merge(self, t1, t2):
        """Merges two trees t1 and t2."""
        if not t1 or not t2:
            return t1 or t2
        if t1.priority > t2.priority:
            t1.right = self._merge(t1.right, t2)
            return t1
        else:
            t2.left = self._merge(t1, t2.left)
            return t2

    def _insert(self, node, key, value):
        """Inserts a new node with key and value into the tree rooted at node."""
        if not node:
            return TreapNode(key, value)
        if key == node.key:
            node.value = value
        elif key < node.key:
            node.left = self._insert(node.left, key, value)
            if node.left and node.left.priority > node.priority:
                node = self._rotate_right(node)
        else:
            node.right = self._insert(node.right, key, value)
            if node.right and node.right.priority > node.priority:
                node = self._rotate_left(node)
        return node

    def _rotate_right(self, node):
        left = node.left
        node.left = left.right
        left.right = node
        return left

    def _rotate_left(self, node):
        right = node.right
        node.right = right.left
        right.left = node
        return right

    def __setitem__(self, key, value):
        """Implements `self[key] = value`."""
        if self.root:
            self.root = self._insert(self.root, key, value)
        else:
            self.root = TreapNode(key, value)

    def __getitem__(self, key):
        """Implements `self[key]`."""
        node = self.root
        while node:
            if key == node.key:
                return node.value
            elif key < node.key:
                node = node.left
            else:
                node = node.right
        raise KeyError(f'Key {key} not found.')

    def __delitem__(self, key):
        """Implements `del self[key]`."""
        self.root = self._delete(self.root, key)

    def _delete(self, node, key):
        if not node:
            raise KeyError(f'Key {key} not found.')
        if key < node.key:
            node.left = self._delete(node.left, key)
        elif key > node.key:
            node.right = self._delete(node.right, key)
        else:
            return self._merge(node.left, node.right)
        return node

    def __contains__(self, key):
        """Implements `key in self`."""
        try:
            self[key]
            return True
        except KeyError:
            return False

    def __iter__(self):
        """In-order traversal (direct order)."""
        yield from self._in_order_traversal(self.root)

    def __reversed__(self):
        """Reverse in-order traversal (reverse order)."""
        yield from self._reverse_in_order_traversal(self.root)

    def _in_order_traversal(self, node):
        """Helper for in-order traversal."""
        if node:
            yield from self._in_order_traversal(node.left)
            yield node.key
            yield from self._in_order_traversal(node.right)

    def _reverse_in_order_traversal(self, node):
        """Helper for reverse in-order traversal."""
        if node:
            yield from self._reverse_in_order_traversal(node.right)
            yield node.key
            yield from self._reverse_in_order_traversal(node.left)

    def __len__(self):
        """Returns the number of nodes in the treap."""
        return sum(1 for _ in self)

    def __repr__(self):
        """String representation of the treap."""
        return f'Treap({list(self)})'
