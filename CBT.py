class CompleteBinaryTree:
    def __init__(self):
        self.tree = []

    def insert(self, value):
        self.tree.append(value)
        self._heapify_up()

    def pop(self):
        if not self.tree:
            return None
        if len(self.tree) == 1:
            return self.tree.pop()
        root = self.tree[0]
        self.tree[0] = self.tree.pop()
        self._heapify_down()
        return root

    def _heapify_up(self):
        index = len(self.tree) - 1
        while index > 0:
            parent_index = (index - 1) // 2
            if self.tree[index] < self.tree[parent_index]:
                self.tree[index], self.tree[parent_index] = self.tree[parent_index], self.tree[index]
                index = parent_index
            else:
                break

    def _heapify_down(self):
        index = 0
        while True:
            left_child_index = 2 * index + 1
            right_child_index = 2 * index + 2
            smallest = index

            if left_child_index < len(self.tree) and self.tree[left_child_index] < self.tree[smallest]:
                smallest = left_child_index

            if right_child_index < len(self.tree) and self.tree[right_child_index] < self.tree[smallest]:
                smallest = right_child_index

            if smallest != index:
                self.tree[index], self.tree[smallest] = self.tree[smallest], self.tree[index]
                index = smallest
            else:
                break

# 예제 사용
cbt = CompleteBinaryTree()
cbt.insert(5)
cbt.insert(3)
cbt.insert(7)
cbt.insert(2)
cbt.insert(4)

print("최소 힙에서 pop한 값:", cbt.pop())
