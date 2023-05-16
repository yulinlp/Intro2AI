def is_valid_state(missionaries, cannibals):
    # 检查状态是否有效（没有修道士被野人吃掉）
    if missionaries < 0 or cannibals < 0:
        return False
    if missionaries > 0 and cannibals > missionaries:
        return False
    if missionaries < 3 and cannibals < missionaries:
        return False
    if missionaries > 3 or cannibals > 3:
        return False
    return True
 
def solve_river_crossing_problem():
    start_state = (3, 3, 'left')
    solutions = []
    # stack维护所有可行state和可行path
    stack = [(start_state, [start_state])]  # 使用栈进行迭代，模拟DFS

    while stack:
        
        # 弹栈
        state, path = stack.pop()
        
        missionaries, cannibals, boat = state

        # 找到一种解决方案
        if missionaries == 0 and cannibals == 0:
            solutions.append(path)
            continue

        # 尝试将一对修道士或一对野人从一岸送到另一岸
        if boat == 'left':
            directions = [(-2, 0), (0, -2), (-1, -1), (-1, 0), (0, -1)]
            next_boat = 'right'
        else:
            directions = [(2, 0), (0, 2), (1, 1), (1, 0), (0, 1)]
            next_boat = 'left'

        for d in directions:
            new_missionaries = missionaries + d[0]
            new_cannibals = cannibals + d[1]
            new_state = (new_missionaries, new_cannibals, next_boat)

            if is_valid_state(new_missionaries, new_cannibals) and new_state not in path:
                new_path = path + [new_state]
                stack.append((new_state, new_path))

    return solutions

solutions = solve_river_crossing_problem()

for i, solution in enumerate(solutions):
    print(f"Solution {i+1}:")
    for state in solution:
        print(state)
    print()
    

