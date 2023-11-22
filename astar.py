from typing import Optional, List, Tuple
import random, copy, time, heapq
import matplotlib.pyplot as plt
import numpy as np


def print_board(solution):
    for i in range(8):
            row = ["Q" if j == solution[i] else "." for j in range(1,9)]
            print(" ".join(row))

class State:
    def __init__(self, N = 8) -> None:
        self.queen_positions = [random.randint(1,N) for i in range(N)]
        self.heuristic: int  = self.calculate_heuristic()
        self.g: int = 0
        self.total_cost: int = self.heuristic + self.g

    def calculate_heuristic(self) -> int:
        h: int = 0
        N: int = len(self.queen_positions)
        max_fitness: int = N*(N-1) // 2
        for i in range(N):
            fixed_queen_pos: Tuple[int, int] = (self.queen_positions[i], i) # (row, column)
            for j in range(i+1, N):
                curr_queen_pos: Tuple[int, int] = (self.queen_positions[j], j) # (row, column)
                diagonal_collision_row: int = abs(fixed_queen_pos[0]-curr_queen_pos[0])
                diagonal_collision_column: int = abs(fixed_queen_pos[1]-curr_queen_pos[1])
                # If a queen pair is not in the same row or diagonal => they are not attacking each other.
                if fixed_queen_pos[0] != curr_queen_pos[0] and diagonal_collision_row != diagonal_collision_column:
                    h += 1
        return max_fitness - h  
    
    def update_total_cost(self) -> None:

        self.g += 1
        self.total_cost = self.heuristic + self.g

    def __lt__(self, other):
        return self.total_cost < other.total_cost
    
    def __eq__(self, other):
        return self.queen_positions == other.queen_positions

    def __str__(self) -> str:
        return f'Queen Positions: {self.queen_positions} | h(n): {self.heuristic} | g(n): {self.g} | F(N): {self.total_cost}'


class AStarAlgorithm:

    @staticmethod
    def generate_random_state(N: int):
        state = State(N=N)
        state.queen_positions = [6,3,1,7,4,8,9,2]
        state.heuristic = state.calculate_heuristic()
    
        return state

    @staticmethod
    def generate_child_states(state: State, states: List[State], visited_states: List[State]) -> List[State]:
    
        queen_pos: List[int] = state.queen_positions
        size: int = len(queen_pos)
        children = []
        for i, pos in enumerate(queen_pos):
            if pos - 1 > 0: # Lower limit of the board.
                child_state_1 = copy.deepcopy(state)
                child_state_1.queen_positions[i] = pos - 1
                child_state_1.heuristic = child_state_1.calculate_heuristic()
                child_state_1.update_total_cost()
                if child_state_1 not in states and child_state_1 not in visited_states:
                    children.append(child_state_1)
            if pos + 1 <= size: # Upper limit of the board.
                child_state_2 = copy.deepcopy(state)
                child_state_2.queen_positions[i] = pos + 1
                child_state_2.heuristic = child_state_2.calculate_heuristic()
                child_state_2.update_total_cost() 
                if child_state_2 not in states and child_state_2 not in visited_states:
                    children.append(child_state_2)
        return children
    
    @staticmethod
    def is_goal_reached(state: State):

        return state.heuristic == 0


class RunAStarAlgorithm:

    @staticmethod
    def run_a_star(N_queens: Optional[int] = 8):
       
        states: List[State] = []
        visited_states: List[State] = []
        goal_reached: bool = False
        steps: int = 1
        
        start_time: float = time.time()

        initial_state: State = AStarAlgorithm.generate_random_state(N=N_queens)
        states.append(initial_state)
        heapq.heapify(states)

        while len(states) != 0 and not goal_reached:
            curr_state: State = heapq.heappop(states)
            print(f'Current state: {curr_state}')
            print_board(curr_state.queen_positions)
            visited_states.append(curr_state)

            if AStarAlgorithm.is_goal_reached(curr_state):
                print(f'GOAL STATE => {curr_state}')
                print_board(curr_state.queen_positions)
                goal_reached = True
                break
            else:
                child_states: List[State] = AStarAlgorithm.generate_child_states(curr_state, states, visited_states)
                states.extend(child_states)
                heapq.heapify(states)
            steps += 1
        else:
            print('SOLUTION NOT FOUND!')

        finish_time: float = time.time()
        time_taken: float = finish_time - start_time

        # Subtracting 1 if all states are expanded and steps increment (flow above).
        if not goal_reached:
            steps -= 1
        
        print('###########################################')
        print(f'Total Steps = {steps}')
        print(f'Solution = {curr_state}')
        print(f'Time taken = {time_taken} seconds')
        
        return [steps, time_taken, goal_reached] 
        
def show_a_star_results(self):
        """Function to display the output of the algorithm."""

        global a_star_output
        if len(a_star_output) != 0:
            output = f'Steps = {a_star_output[0]} | Time = {a_star_output[1] :.4} secs | Solution Found = {a_star_output[2]}'
            self.ui.outputLabel.setText(output)
            self.load_images_directory()
        else:
            print('Output List is Empty!')


a_star_output = RunAStarAlgorithm.run_a_star(N_queens=8)

