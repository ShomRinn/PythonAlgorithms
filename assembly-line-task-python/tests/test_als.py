"""Sample tests for 'tasks.als' module."""
from tasks.als import solve_als_problem


def test_solve_als_problem():
    """Tests for solve_als_problem function."""
    # Example 1
    optimal_time, optimal_lines_per_station = solve_als_problem(
        start_costs=[2, 3], 
        station_costs=[[5, 10], [7, 1]],
        transfer_costs=[[1], [3]],
        finish_costs=[1, 1],
    )

    assert optimal_time == 10 and optimal_lines_per_station == [1, 2]

    # Example 2
    optimal_time, optimal_lines_per_station = solve_als_problem(
        start_costs=[2, 6], 
        station_costs=[[5, 2, 9, 1], [3, 5, 2, 1]],
        transfer_costs=[[5, 2, 1], [1, 4, 2]],
        finish_costs=[2, 4],
    )

    assert optimal_time == 18 and optimal_lines_per_station == [1, 1, 2, 2]
