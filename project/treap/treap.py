from collections.abc import MutableMapping
import random
from typing import Optional, Generator, Tuple, Any


class TreapNode:
    """
    A node in the Treap data structure.

    Parameters
    ----------
    key : int
        The key for the node.
    value : str
        The value associated with the key.
    priority : int, optional
        The priority of the node, used for balancing the Treap. If not provided,
        a random priority is assigned.
    """

    def __init__(self, key: int, value: str, priority: Optional[int] = None) -> None:
        self.key: int = key
        self.value: str = value
        self.priority: int = (
            priority if priority is not None else random.randint(1, 100)
        )
        self.left: Optional["TreapNode"] = None
        self.right: Optional["TreapNode"] = None


class Treap(MutableMapping):
    """
    A Treap is a data structure that combines properties of a binary search tree
    and a heap. It is balanced using priorities assigned to nodes and maintains
    the binary search tree property for keys.

    This class implements a mutable mapping, as defined by the `collections.abc.MutableMapping` class.

    Methods
    -------
    __setitem__(key, value)
        Inserts the key-value pair into the Treap.
    __getitem__(key)
        Retrieves the value for the given key.
    __delitem__(key)
        Deletes the key-value pair.
    __contains__(key)
        Returns `True` if the key is in the Treap, otherwise `False`.
    __iter__()
        Returns an iterator for the keys in sorted order.
    __reversed__()
        Returns an iterator for the keys in reverse sorted order.
    __len__()
        Returns the number of keys in the Treap.
    """

    def __init__(self) -> None:
        self.root: Optional[TreapNode] = None

    def _split(
        self, node: Optional[TreapNode], key: int
    ) -> Tuple[Optional[TreapNode], Optional[TreapNode]]:
        """
        Splits the tree rooted at the given node into two subtrees based on the provided key.

        Parameters
        ----------
        node : TreapNode or None
            The root of the tree to split.
        key : int
            The key at which to split the tree.

        Returns
        -------
        tuple of (TreapNode or None, TreapNode or None)
            The left and right subtrees resulting from the split.
        """
        if not node:
            return None, None
        elif key > node.key:
            node.right, t2 = self._split(node.right, key)
            return node, t2
        else:
            t1, node.left = self._split(node.left, key)
            return t1, node

    def _merge(
        self, t1: Optional[TreapNode], t2: Optional[TreapNode]
    ) -> Optional[TreapNode]:
        """
        Merges two Treap subtrees into one, maintaining the heap property.

        Parameters
        ----------
        t1 : TreapNode or None
            The first subtree to merge.
        t2 : TreapNode or None
            The second subtree to merge.

        Returns
        -------
        TreapNode or None
            The root of the merged subtree.
        """
        if not t1 or not t2:
            return t1 or t2
        if t1.priority > t2.priority:
            t1.right = self._merge(t1.right, t2)
            return t1
        else:
            t2.left = self._merge(t1, t2.left)
            return t2

    def _insert(self, node: Optional[TreapNode], key: int, value: str) -> TreapNode:
        """
        Inserts a new node with the given key and value into the tree rooted at the given node.

        If a node with the same key already exists, the value is updated.

        Parameters
        ----------
        node : TreapNode or None
            The root of the subtree in which to insert the new node.
        key : int
            The key for the new node.
        value : str
            The value for the new node.

        Returns
        -------
        TreapNode
            The root of the subtree after the insertion.
        """
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
        """
        Rotates the given subtree to the right.

        Parameters
        ----------
        node : TreapNode
            The root of the subtree to rotate.

        Returns
        -------
        TreapNode
            The new root of the subtree after rotation.
        """
        left = node.left
        if not left:
            return node  # if there is no left child, we return the node itself
        node.left = left.right
        if left:
            left.right = node
        return left

    def _rotate_left(self, node: TreapNode) -> TreapNode:
        """
        Rotates the given subtree to the left.

        Parameters
        ----------
        node : TreapNode
            The root of the subtree to rotate.

        Returns
        -------
        TreapNode
            The new root of the subtree after rotation.
        """
        right = node.right
        if not right:
            return node  # if there is no right child, we return the node itself
        node.right = right.left
        if right:
            right.left = node
        return right

    def __setitem__(self, key: int, value: str) -> None:
        """
        Sets the value for the given key in the Treap.

        Parameters
        ----------
        key : int
            The key to insert or update.
        value : str
            The value associated with the key.
        """
        if self.root:
            self.root = self._insert(self.root, key, value)
        else:
            self.root = TreapNode(key, value)

    def __getitem__(self, key: int) -> str:
        """
        Retrieves the value associated with the given key.

        Parameters
        ----------
        key : int
            The key for which the value is to be retrieved.

        Returns
        -------
        str
            The value associated with the key.

        Raises
        ------
        KeyError
            If the key is not found in the Treap.
        """
        node = self.root
        while node:
            if key == node.key:
                return node.value
            elif key < node.key:
                node = node.left
            else:
                node = node.right
        raise KeyError(f"Key {key} not found.")

    def __delitem__(self, key: int) -> None:
        """
        Deletes the key-value pair associated with the given key.

        Parameters
        ----------
        key : int
            The key to delete.

        Raises
        ------
        KeyError
            If the key is not found in the Treap.
        """
        self.root = self._delete(self.root, key)

    def _delete(self, node: Optional[TreapNode], key: int) -> Optional[TreapNode]:
        """
        Deletes a node with the given key in the subtree rooted at the given node.

        Parameters
        ----------
        node : TreapNode or None
            The root of the subtree to delete the node from.
        key : int
            The key of the node to delete.

        Returns
        -------
        TreapNode or None
            The root of the subtree after the node is deleted.

        Raises
        ------
        KeyError
            If the key is not found in the subtree.
        """
        if not node:
            raise KeyError(f"Key {key} not found.")
        if key < node.key:
            node.left = self._delete(node.left, key)
        elif key > node.key:
            node.right = self._delete(node.right, key)
        else:
            return self._merge(node.left, node.right)
        return node

    def __contains__(self, key: Any) -> bool:
        """
        Checks if the given key is present in the Treap.

        Parameters
        ----------
        key : Any
            The key to check for presence.

        Returns
        -------
        bool
            `True` if the key is present, `False` otherwise.
        """
        try:
            self[key]  # Key access
            return True
        except KeyError:
            return False

    def __iter__(self) -> Generator[int, None, None]:
        """
        Performs an in-order traversal of the Treap, yielding keys in sorted order.

        Yields
        ------
        int
            The keys in sorted order.
        """
        yield from self._in_order_traversal(self.root)

    def __reversed__(self) -> Generator[int, None, None]:
        """
        Performs a reverse in-order traversal of the Treap, yielding keys in reverse sorted order.

        Yields
        ------
        int
            The keys in reverse sorted order.
        """
        yield from self._reverse_in_order_traversal(self.root)

    def _in_order_traversal(
        self, node: Optional[TreapNode]
    ) -> Generator[int, None, None]:
        """
        Helper method for in-order traversal.

        Parameters
        ----------
        node : TreapNode or None
            The root of the subtree to traverse.

        Yields
        ------
        int
            The keys of the nodes in in-order.
        """
        if node:
            yield from self._in_order_traversal(node.left)
            yield node.key
            yield from self._in_order_traversal(node.right)

    def _reverse_in_order_traversal(
        self, node: Optional[TreapNode]
    ) -> Generator[int, None, None]:
        """
        Helper method for reverse in-order traversal.

        Parameters
        ----------
        node : TreapNode or None
            The root of the subtree to traverse.

        Yields
        ------
        int
            The keys of the nodes in reverse in-order.
        """
        if node:
            yield from self._reverse_in_order_traversal(node.right)
            yield node.key
            yield from self._reverse_in_order_traversal(node.left)

    def __len__(self) -> int:
        """
        Returns the number of nodes in the Treap.

        Returns
        -------
        int
            The number of nodes in the Treap.
        """
        return sum(1 for _ in self)

    def __repr__(self) -> str:
        """
        Returns the string representation of the Treap.

        Returns
        -------
        str
            The string representation of the Treap.
        """
        return f"Treap({list(self)})"
