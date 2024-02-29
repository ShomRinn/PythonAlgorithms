"""Template for programming assignment:
find any eligible schedule/order of tasks taking into consideration task's dependencies."""
from typing import List, Tuple
from collections import deque


def find_task_order(num_tasks: int, dependencies: List[Tuple[int, int]]) -> List[int]:
    """
    Returns any appropriate order of tasks that complies with all dependencies.
    Tasks are enumerated from 0 to num_tasks-1.
    The dependency list consists of tuples with the numbers of two tasks, the second task can only be completed only after the first task.
    There is at least one eligible order.

    For example, you have five tasks from 0 to 4 and the dependency list [(0,1), (3,4), (4,1)].
    One of the eligible orders is [0, 3, 4, 1, 2].

    Parameters:
        num_tasks (int) : the number of tasks.
        dependencies (List[Tuple[int, int]]): the dependency list, which shows that the second task can only be done after the first.
    Returns
        List[int]: any appropriate task order that complies with the dependencies.
    """
    in_degree = [0] * num_tasks
    graph = {i: [] for i in range(num_tasks)}
    for pre, next_task in dependencies:
        graph[pre].append(next_task)
        in_degree[next_task] += 1
    
    queue = deque([i for i in range(num_tasks) if in_degree[i] == 0])
    order = []
    
    while queue:
        task = queue.popleft()
        order.append(task)
        for dependent_task in graph[task]:
            in_degree[dependent_task] -= 1
            if in_degree[dependent_task] == 0:
                queue.append(dependent_task)
    return order