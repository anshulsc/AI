from typing import List, Optional
import random
import copy
import time

class State:
    def __init__(self, word: str) -> None:
        self.word = list(word)
        self.heuristic: int = 0

    def calculate_heuristic(self, goal_word: str):
        heuristic = sum(abs(i - goal_word.index(j)) + abs(self.word.index(j) - goal_word.index(j)) for i, j in enumerate(self.word))
        self.heuristic = heuristic

    def __lt__(self, other):
        return self.heuristic < other.heuristic

    def __eq__(self, other):
        return self.word == other.word

    def __str__(self):
        return ''.join(self.word)

class SteepestAscentHillClimbing:

    goal_word = "ABCD"

    @staticmethod
    def generate_random_state(word_length: int):
        word = ''.join(random.sample(SteepestAscentHillClimbing.goal_word, word_length))
        state = State(word=word)
        state.calculate_heuristic(SteepestAscentHillClimbing.goal_word)
        return state

    @staticmethod
    def generate_neighbor_state(state: State):
        new_state = copy.deepcopy(state)
        i, j = random.sample(range(len(new_state.word)), 2)
        new_state.word[i], new_state.word[j] = new_state.word[j], new_state.word[i]
        new_state.calculate_heuristic(SteepestAscentHillClimbing.goal_word)
        return new_state



    @staticmethod
    def is_goal_reached(state: State):
        return ''.join(state.word) == SteepestAscentHillClimbing.goal_word

class RunSteepestAscentHillClimbing:

    @staticmethod
    def run_steepest_ascent_hill_climbing(word_length: Optional[int] = 6):
        current_state = SteepestAscentHillClimbing.generate_random_state(word_length)
        goal_reached = False
        steps = 1
        start_time = time.time()

        while not SteepestAscentHillClimbing.is_goal_reached(current_state):
            
            neighbor_states = [SteepestAscentHillClimbing.generate_neighbor_state(current_state) for _ in range(word_length)]
            best_neighbor_state = min(neighbor_states)
            
            if best_neighbor_state.heuristic <= current_state.heuristic:
                current_state = best_neighbor_state

            print(f'Current state  {current_state}: f(n) = {current_state.heuristic}')

            steps += 1

        finish_time = time.time()
        time_taken = finish_time - start_time

        print()
        print('###########################################')
        print(f'Total Steps = {steps}')
        print(f'Solution =\n{current_state}')
        print(f'Time taken = {time_taken} seconds')

        return [steps, time_taken, goal_reached]

# Run Steepest Ascent Hill Climbing Algorithm
steepest_ascent_output = RunSteepestAscentHillClimbing.run_steepest_ascent_hill_climbing(word_length=4)
