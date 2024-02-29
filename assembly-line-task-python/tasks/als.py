from typing import List, Tuple


def solve_als_problem(
    start_costs: Tuple[int, int], 
    station_costs: Tuple[List[int], List[int]],
    transfer_costs: Tuple[List[int], List[int]],
    finish_costs: Tuple[int, int],
) -> Tuple[int, List[int]]:
    """
    Solves the Assembly Line Scheduling problem using dynamic programming.
    """

    num_stations = len(station_costs[0])

    cost = [[float('inf')] * num_stations for _ in range(2)]
    path = [[0] * num_stations for _ in range(2)]

    cost[0][0] = start_costs[0] + station_costs[0][0]
    cost[1][0] = start_costs[1] + station_costs[1][0]

    for i in range(1, num_stations):
        if cost[0][i-1] + station_costs[0][i] < cost[1][i-1] + transfer_costs[1][i-1] + station_costs[0][i]:
            cost[0][i] = cost[0][i-1] + station_costs[0][i]
            path[0][i] = 1
        else:
            cost[0][i] = cost[1][i-1] + transfer_costs[1][i-1] + station_costs[0][i]
            path[0][i] = 2

        if cost[1][i-1] + station_costs[1][i] < cost[0][i-1] + transfer_costs[0][i-1] + station_costs[1][i]:
            cost[1][i] = cost[1][i-1] + station_costs[1][i]
            path[1][i] = 2
        else:
            cost[1][i] = cost[0][i-1] + transfer_costs[0][i-1] + station_costs[1][i]
            path[1][i] = 1

    if cost[0][num_stations - 1] + finish_costs[0] < cost[1][num_stations - 1] + finish_costs[1]:
        final_cost = cost[0][num_stations - 1] + finish_costs[0]
        final_line = 1
    else:
        final_cost = cost[1][num_stations - 1] + finish_costs[1]
        final_line = 2

    optimal_path = [final_line]
    for i in range(num_stations - 1, 0, -1):
        final_line = path[final_line - 1][i]
        optimal_path.insert(0, final_line)

    return final_cost, optimal_path
