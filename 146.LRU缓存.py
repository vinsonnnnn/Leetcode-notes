class DLinkedNode:
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.nodes = {}

        # 两个哑节点
        self.tail = DLinkedNode()
        self.head = DLinkedNode()
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node):
        before = node.prev
        after = node.next
        before.next = after
        after.prev = before
        node.prev = None
        node.next = None

    def _add_to_head(self, node):
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def _move_to_head(self, node):
        self._remove(node)
        self._add_to_head(node)

    def get(self, key: int) -> int:
        node = self.nodes.get(key)
        if node is None:
            return -1

        self._move_to_head(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        # 整体逻辑：查键 → 已有就更新并移到头部；新键就插入头部；
        # 超容量就从链表和字典中删除最旧条目。
        node = self.nodes.get(key)
        if node is not None:
            # 更新已有条目，不增加条目数量
            node.value = value
            self._move_to_head(node)
            return

        # 插入新条目，放到最近使用位置
        node = DLinkedNode(key, value)
        self.nodes[key] = node
        self._add_to_head(node)

        if len(self.nodes) > self.capacity:
            oldest = self.tail.prev
            self._remove(oldest)
            del self.nodes[oldest.key]


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
