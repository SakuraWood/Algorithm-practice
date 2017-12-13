class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.cache = {}
        self.volume = capacity
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.pre = self.head

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        try:
            node = self.cache[key]
        except:
            return -1
        node.pre.next = node.next
        node.next.pre = node.pre
        self.insertNode(node)
        return node.value

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        node = self.cache.get(key)
        if node:
            self.deleteNode(node)
        node = Node()
        node.key = key
        node.value = value
        self.insertNode(node)
        self.cache[key] = node
        if len(self.cache) > self.volume:
            self.deleteNode(self.head.next)

    def deleteNode(self, node):
        node.pre.next = node.next
        node.next.pre = node.pre
        del self.cache[node.key]
        del node

    def insertNode(self, node):
        last = self.tail.pre
        last.next = node
        node.pre = last
        node.next = self.tail
        self.tail.pre = node


class Node(object):
    def __init__(self):
        self.pre = None
        self.next = None
        self.key = None
        self.value = None


def test():
    cache = LRUCache(10)
    cache.put(1, 2)
    cache.put(2, 3)
    cache.put(3, 4)
    cache.put(4, 5)
    cache.put(5, 6)
    cache.put(6, 2)
    cache.put(7, 3)
    cache.put(8, 4)
    cache.put(9, 5)
    cache.put(10, 6)

    print cache.get(10)
    print cache.get(1)
    print cache.get(2)
    cache.put(12, 12)
    print cache.get(3)


test()
