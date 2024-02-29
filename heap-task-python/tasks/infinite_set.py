"""Template for programming assignment: Infinite Set."""


class InfiniteSet:
    """Emulates a set of all natural numbers."""

    def __init__(self):
        self.heap = []
        self.next_number = 1

    def pop_minimum(self) -> int:
        # Проверяем, есть ли числа в куче, которые меньше следующего числа
        if self.heap and self.heap[0] < self.next_number:
            return self._pop_heap()
        else:
            # Возвращаем следующее натуральное число
            self.next_number += 1
            return self.next_number - 1

    def insert(self, x: int):
        if x < self.next_number:
            # Если число меньше следующего, добавляем его в кучу
            self._insert_heap(x)
        # Иначе игнорируем, так как оно уже есть в последовательности

    def _pop_heap(self) -> int:
        # Удаляем наименьший элемент из кучи
        smallest = self.heap[0]
        last_item = self.heap.pop()
        if self.heap:
            self.heap[0] = last_item
            self._heapify_down(0)
        return smallest

    def _insert_heap(self, item: int):
        # Вставляем новый элемент в кучу
        self.heap.append(item)
        self._heapify_up(len(self.heap) - 1)

    def _heapify_up(self, index):
        # Перемещаем элемент вверх по куче
        parent_index = (index - 1) // 2
        if index > 0 and self.heap[index] < self.heap[parent_index]:
            self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
            self._heapify_up(parent_index)

    def _heapify_down(self, index):
        # Перемещаем элемент вниз по куче
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
