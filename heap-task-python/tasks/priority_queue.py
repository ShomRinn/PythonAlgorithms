"""Template for programming assignment: Priority Queue."""


class PriorityQueue:
    """The basic interface for Priority Queue."""

    def __init__(self):
        self.heap = []

    def get_minimum(self) -> int:
        if self.is_empty():
            raise Exception("ПУста!!!")
        return self.heap[0]

    def pop(self) -> int:
        # Удаляет и возвращает минимальный элемент из кучи
        # Сложность: O(log N), где N - количество элементов в куче
        # Основная сложность возникает из-за операции _heapify_down
        if self.is_empty():
            raise Exception("ПУста!!!")
        min_item = self.heap[0]
        last_item = self.heap.pop()
        if self.heap:
            self.heap[0] = last_item
            self._heapify_down(0)
        return min_item

    def insert(self, value: int):
        # Вставляет новый элемент в кучу
        # Сложность: O(log N), где N - количество элементов в куче
        # Основная сложность возникает из-за операции _heapify_up
        self.heap.append(value)
        self._heapify_up(len(self.heap) - 1)

    def is_empty(self) -> bool:
        return len(self.heap) == 0

    def size(self) -> int:
        return len(self.heap)

    def _heapify_up(self, index):
        # Вспомогательная функция для поддержания свойств кучи при вставке нового элемента
        # Сложность: O(log N), так как в худшем случае элемент может быть перемещен от нижнего уровня к корню кучи
        parent_index = (index - 1) // 2
        if index > 0 and self.heap[index] < self.heap[parent_index]:
            self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
            self._heapify_up(parent_index)

    def _heapify_down(self, index):
        # Вспомогательная функция для поддержания свойств кучи после удаления элемента
        # Сложность: O(log N), так как в худшем случае элемент может быть перемещен от корня к одному из нижних уровней кучи
        smallest = index
        left_child = 2 * index + 1
        right_child = 2 * index + 2

        if left_child < len(self.heap) and self.heap[left_child] < self.heap[smallest]:
            smallest = left_child

        if right_child < len(self.heap) and self.heap[right_child] < self.heap[smallest]:
            smallest = right_child

        if smallest != index:
            self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
            self._heapify_down(smallest)