from collections import deque
from queue import PriorityQueue
import queue
import numpy as np
from heapq import heappop, heappush
import time

import tests
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

def astar(my_cube, h, visited):
    # Frontiera, ca listă (heap) de tupluri (cost-total-estimat, nod)
    frontier = []
    if h == 1:
        heappush(frontier, (h1(my_cube.state), my_cube))
    if h == 3:
        heappush(frontier, (h3(my_cube, visited), my_cube))

    # Nodurile descoperite ca dictionar de cub, parinte si cost pana la nod
    discovered = {my_cube.hash(): (None, 0)}
    crt_cube = my_cube
    while frontier:
        crt_cost, crt_cube = heappop(frontier)
        crt_g = discovered[crt_cube.hash()][1]
        if (np.array_equal(my_cube.goal_state, crt_cube.state)):
            break
        for next in get_neighbours(crt_cube):
            neigh_c = crt_g + 1
            if next.hash() not in discovered or neigh_c < discovered[next.hash()][1]:
                discovered[next.hash()] = (crt_cube, neigh_c)
                if h == 1:
                    heappush(frontier, (neigh_c + h1(next.state), next))
                if h == 3:
                    heappush(frontier, (neigh_c + h3(next, visited), next))
    return crt_cube, discovered


def bidirectional_bfs(my_cube):
    #coada cu cubul de start
    forward_queue = [my_cube]
    solved_cube = Cube(scrambled=False)
    #coada cu cubul de end
    backward_queue = [solved_cube]

    #dictionar cu hashurile cubului
    forward_visited = {my_cube.hash_state(my_cube.state): "empty"}
    backward_visited = {my_cube.hash_state(my_cube.goal_state): "empty"}

    while forward_queue and backward_queue:
        if(forward_queue):
            first = forward_queue.pop(0)
            if(backward_visited.get(first.hash_state(first.state))):
                return first, forward_visited, backward_visited
            for next in get_neighbours(first):
                if (next.hash_state(next.state) not in forward_visited):
                    forward_visited[next.hash_state(next.state)] =  first
                    forward_queue.append(next)

        if(backward_queue):
            first_backwards = backward_queue.pop(0)
            if(forward_visited.get(first_backwards.hash_state(first_backwards.state))):
                return first_backwards, forward_visited, backward_visited
            for next in get_neighbours(first_backwards):
                if(next.hash_state(next.state) not in backward_visited):
                    backward_visited[next.hash_state(next.state)] = first_backwards
                    backward_queue.append(next)

def rebuild_path(found_cube, forward_list, backwards_list, original_cube):
    my_list = []
    my_other_list = []
    start_cube = forward_list.get(found_cube.hash_state(found_cube.state))
    my_list.append(start_cube)

    while(start_cube.hash_state(start_cube.state) != original_cube.hash_state(original_cube.state)):
        curr  = forward_list.get(start_cube.hash_state(start_cube.state))
        my_list.append(curr)
        start_cube = curr

    end_cube = backwards_list.get(found_cube.hash_state(found_cube.state))
    my_other_list.append(end_cube)
    while(end_cube.hash_state(end_cube.state) != original_cube.hash_state(original_cube.goal_state)):
        current = backwards_list.get(end_cube.hash_state(end_cube.state))
        my_other_list.append(current)
        end_cube = current
    my_list.extend(my_other_list)
    return my_list



def main():
    print("FIRST CASE")
    start = time.time()
    cube = Cube(tests.case1)
    solution, discovered_states = astar(cube, 1, 0)
    finish = time.time()
    start_bfs = time.time()
    bfs_cube, my_forward_list, my_back_list = bidirectional_bfs(cube)
    neigh_list = rebuild_path(bfs_cube, my_forward_list, my_back_list, cube)
    finish_bfs = time.time()
    print("timp A*")
    print(finish - start)
    print("nr de stari A*")
    print(discovered_states.__sizeof__())
    print("nr de stari BFS")
    size = my_forward_list.__sizeof__() + my_back_list.__sizeof__()
    print(size)
    print("timp bfs")
    print(finish_bfs - start_bfs)


    print("SECOND CASE")
    start = time.time()
    cube = Cube(tests.case2)
    solution, discovered_states = astar(cube, 1, 0)
    finish = time.time()
    start_bfs = time.time()
    bfs_cube, my_forward_list, my_back_list = bidirectional_bfs(cube)
    neigh_list = rebuild_path(bfs_cube, my_forward_list, my_back_list, cube)
    finish_bfs = time.time()
    print("timp A*")
    print(finish - start)
    print("nr de stari A*")
    print(discovered_states.__sizeof__())
    print("nr de stari BFS")
    size = my_forward_list.__sizeof__() + my_back_list.__sizeof__()
    print(size)
    print("timp bfs")
    print(finish_bfs - start_bfs)


    print("THIRDS CASE")
    start = time.time()
    cube = Cube(tests.case3)
    solution, discovered_states = astar(cube, 1, 0)
    finish = time.time()
    start_bfs = time.time()
    bfs_cube, my_forward_list, my_back_list = bidirectional_bfs(cube)
    neigh_list = rebuild_path(bfs_cube, my_forward_list, my_back_list, cube)
    finish_bfs = time.time()
    print("timp A*")
    print(finish - start)
    print("nr de stari A*")
    print(discovered_states.__sizeof__())
    print("nr de stari BFS")
    size = my_forward_list.__sizeof__() + my_back_list.__sizeof__()
    print(size)
    print("timp bfs")
    print(finish_bfs - start_bfs)


    print("FOURTH CASE")
    start = time.time()
    cube = Cube(tests.case4)
    solution, discovered_states = astar(cube, 1, 0)
    finish = time.time()
    start_bfs = time.time()
    bfs_cube, my_forward_list, my_back_list = bidirectional_bfs(cube)
    neigh_list = rebuild_path(bfs_cube, my_forward_list, my_back_list, cube)
    finish_bfs = time.time()
    print("timp A*")
    print(finish - start)
    print("nr de stari A*")
    print(discovered_states.__sizeof__())
    print("nr de stari BFS")
    size = my_forward_list.__sizeof__() + my_back_list.__sizeof__()
    print(size)
    print("timp bfs")
    print(finish_bfs - start_bfs)


if __name__ == "__main__":
    main()
