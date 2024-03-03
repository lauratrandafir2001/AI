import numpy as np
from math import sqrt, log
import time

from pocket_cube import cube
from pocket_cube.cube import Cube
from pocket_cube.moves import Move
from random import choice
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

def h2(a):
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
    return 20-cnt

def h3(current_cube, visited):
    if(visited.get(current_cube.hash_state(current_cube.state))):
        return visited.get(current_cube.hash_state(current_cube.state))
    else:
        return h1(current_cube.state)


CP = 1.0 / sqrt(2.0)
class Node:
   def __init__(self, parent, length):
      self.parent = parent
      self.actions = {}
      self.n = 0
      self.q = 0
      self.length = length


# Insert Node


def select_action(node, c = 0.1):
    """
    Se caută acțiunea a care maximizează expresia:
    Q_a / N_a  +  c * sqrt(2 * log(N_node) / N_a)
    """
    N_node = node.n
    max_score = -1
    best_action = None

    for a, n in node.actions.items():
        # print(a, n.n)
        crt_score = n.q / n.n + c * sqrt(2 * log(N_node) / n.n)

        if max_score < crt_score:
            max_score = crt_score
            best_action = a

    return best_action


def get_neighbours(initial_cube):
    myMoves = []
    for move in Move.get_possible_moves():
        new_cube = initial_cube.move(move)
        myMoves.append(new_cube)
    return myMoves
def is_goal_state(state, goal_state):
    current = 0
    if(np.array_equal(state, goal_state)):
        return 1
    else:
        return 0

def mcts(state0, budget, my_cube, h, visited):
    node =  Node(None, 0)
    tree = node

    for x in range(budget):
        state = state0
        node = tree

        while(is_goal_state(state, my_cube.goal_state) == 0
            and all(action in node.actions.keys() for action in Move.get_possible_moves())):
            new_action = select_action(node)
            my_cube = my_cube.move(new_action)
            state = my_cube.state
            node = node.actions[new_action]

        if is_goal_state(state, cube.goal_state) == 0:
            moves_list = Move.get_possible_moves()
            moves_not_in_action = []
            for move in moves_list:
                if move not in list(node.actions.keys()):
                    moves_not_in_action.append(move)
            new_action = choice(moves_not_in_action)
            my_cube = my_cube.move(new_action)
            state = my_cube.state
            node = Node(node, (node.length + 1))
            node.parent.actions[new_action] = node
        cnt = 0
        reward = 0
        while(cnt < 14):
             moves_lsit = Move.get_possible_moves()
             new_action = choice(moves_lsit)
             if(h == 1):
                reward = h1(my_cube.state)
             if (h == 2):
                 reward = h2(my_cube.state)
             if (h == 3):
                 reward = h3(my_cube, visited)

             my_cube = my_cube.move(new_action)
             node = Node(node, (node.length + 1))
             cnt += 1

        current_node = node
        while current_node:
            current_node.n += 1
            current_node.q += reward
            current_node = current_node.parent

    return my_cube
def main():
    cube = Cube("U' R U' F' R F F U' F U U")
    start_time = time.time()
    solution = mcts(cube.state, 20000, cube, 2, 0)
    end_time = time.time()
    print(end_time - start_time)
    print(solution.state)
if __name__ == "__main__":
    main()
