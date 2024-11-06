from collections.abc import MutableMapping
import random
from typing import Optional, Generator, Tuple, Any

class TreapNode:
    def __init__(self, key: int, value: str, priority: Optional[int] = None) -> None:
        self.key: int = key
        self.value: str = value
        self.priority: int = priority if priority is not None else random.randint(1, 100)
        self.left: Optional['TreapNode'] = None
        self.right: Optional['TreapNode'] = None

class Treap(MutableMapping):
    def __init__(self) -> None:
        self.root: Optional[TreapNode] = None

    def _split(self, node: Optional[TreapNode], key: int) -> Tuple[Optional[TreapNode], Optional[TreapNode]]:
        """Splits tree rooted at node into two trees based on key."""
        if not node:
            return None, None
        elif key > node.key:
            node.right, t2 = self._split(node.right, key)
            return node, t2
        else:
            t1, node.left = self._split(node.left, key)
            return t1, node

    def _merge(self, t1: Optional[TreapNode], t2: Optional[TreapNode]) -> Optional[TreapNode]:
        """Merges two trees t1 and t2."""
        if not t1 or not t2:
            return t1 or t2
        if t1.priority > t2.priority:
            t1.right = self._merge(t1.right, t2)
            return t1
        else:
            t2.left = self._merge(t1, t2.left)
            return t2

    def _insert(self, node: Optional[TreapNode], key: int, value: str) -> TreapNode:
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

    def _rotate_right(self, node: TreapNode) -> TreapNode:
        left = node.left
        if not left:
            return node  # if there is no left child, we return the node itself
        node.left = left.right if left else node
        if left:
            left.right = node
        return left

    def _rotate_left(self, node: TreapNode) -> TreapNode:
        right = node.right
        if not right:
            return node  # if there is no right child, we return the node itself
        node.right = right.left if right else node
        if right:
            right.left = node
        return right

    def __setitem__(self, key: int, value: str) -> None:
        """Implements `self[key] = value`."""
        if self.root:
            self.root = self._insert(self.root, key, value)
        else:
            self.root = TreapNode(key, value)

    def __getitem__(self, key: int) -> str:
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

    def __delitem__(self, key: int) -> None:
        """Implements `del self[key]`."""
        self.root = self._delete(self.root, key)

    def _delete(self, node: Optional[TreapNode], key: int) -> Optional[TreapNode]:
        if not node:
            raise KeyError(f'Key {key} not found.')
        if key < node.key:
            node.left = self._delete(node.left, key)
        elif key > node.key:
            node.right = self._delete(node.right, key)
        else:
            return self._merge(node.left, node.right)
        return node

    def __contains__(self, key: Any) -> bool:
        """Implements `key in self`."""
        try:
            self[key]  # Key access
            return True
        except KeyError:
           return False



    def __iter__(self) -> Generator[int, None, None]:
        """In-order traversal (direct order)."""
        yield from self._in_order_traversal(self.root)

    def __reversed__(self) -> Generator[int, None, None]:
        """Reverse in-order traversal (reverse order)."""
        yield from self._reverse_in_order_traversal(self.root)

    def _in_order_traversal(self, node: Optional[TreapNode]) -> Generator[int, None, None]:
        """Helper for in-order traversal."""
        if node:
            yield from self._in_order_traversal(node.left)
            yield node.key
            yield from self._in_order_traversal(node.right)

    def _reverse_in_order_traversal(self, node: Optional[TreapNode]) -> Generator[int, None, None]:
        """Helper for reverse in-order traversal."""
        if node:
            yield from self._reverse_in_order_traversal(node.right)
            yield node.key
            yield from self._reverse_in_order_traversal(node.left)

    def __len__(self) -> int:
        """Returns the number of nodes in the treap."""
        return sum(1 for _ in self)

    def __repr__(self) -> str:
        """String representation of the treap."""
        return f'Treap({list(self)})'
