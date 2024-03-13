class Node:

    def __init__(self):
        self.key = None
        self.value = None
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity):
        self.head = Node()
        self.tail = Node()
        self.capacity = capacity
        self.size = 0
        self.cache = {}

        self.head.next = self.tail
        self.tail.prev = self.head

    def _move_to_head(self, node):
        node.prev = self.head
        node.next = self.head.next

        node.prev.next = node
        node.next.prev = node

    def _unlink_node(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        node = self.cache.get(key)
        if node is None:
            return -1
        self._unlink_node(node)
        self._move_to_head(node)
        return node.value

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        node = self.cache.get(key)
        if node:
            node.value = value
            self._unlink_node(node)
            self._move_to_head(node)
            return

        node = Node()
        node.key = key
        node.value = value

        self.cache[key] = node
        self._move_to_head(node)

        self.size += 1
        if self.size > self.capacity:
            outdated = self.tail.prev
            self._unlink_node(outdated)
            del self.cache[outdated.key]
            self.size -= 1
