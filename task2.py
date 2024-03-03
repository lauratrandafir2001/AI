import time
import task1
from pocket_cube.cube import Cube
from pocket_cube.moves import Move
def h1(a):
    cnt = 0
    for i in a[0:4]:
        if(i != 0):
            cnt = cnt + 1
    for i in a[4:8]:
        if(i != 1):
            cnt = cnt + 1
    for i in a[8:12]:
        if (i != 2):
            cnt = cnt + 1
    for i in a[12:16]:
        if (i != 3):
            cnt = cnt + 1
    for i in a[16:20]:
        if (i != 4):
            cnt = cnt + 1

    return cnt/8

def h3(current_cube, visited):
    if(visited.get(current_cube.hash_state(current_cube.state))):
        return visited.get(current_cube.hash_state(current_cube.state))
    else:
        return h1(current_cube.state)

def get_neighbours(initial_cube):
    myMoves = []
    for move in Move.get_possible_moves():
        new_cube = initial_cube.move(move)
        myMoves.append(new_cube)
    return myMoves

def bfs(solved_cube, unsolved_cube):
    #dictionar cu hash si numarul de miscari
    visited = {solved_cube.hash_state(solved_cube.state): 0}
    cubes_queue = [solved_cube]
    depth_queue = [1]
    while cubes_queue:
            current_cube = cubes_queue.pop(0)
            depth = depth_queue.pop(0)
            if(visited.get(current_cube.hash_state(current_cube.state)) == 7 or
              current_cube.hash_state(current_cube.state) == unsolved_cube.hash_state(unsolved_cube.state)):
                return visited, current_cube
            for next in get_neighbours(current_cube):
                if (next.hash_state(next.state) not in visited):
                    visited[next.hash_state(next.state)] =  depth
                    cubes_queue.append(next)
                    depth_queue.append(depth + 1)
            depth = depth + 1
    return visited, current_cube


def main():
    solved_cube = Cube(scrambled=False)
    unsolved_cube = Cube("U' R U' F' R F F U' F U U")
    start_time = time.time()
    print(unsolved_cube.state)
    solution, current_cube = bfs(solved_cube, unsolved_cube)
    print(solution)
    # solution = task3.mcts(unsolved_cube.state, 1000, unsolved_cube, 3, solution)
    solution, discovered = task1.astar(unsolved_cube, h3, solution)
    finish_time = time.time()
    print("timpul de rulare este" + str(finish_time - start_time))
    print(solution.state)

if __name__ == "__main__":
    main()

