class State:
    def __init__(self, queens=None):
        self.queens = queens if queens else [-1,-1,-1,-1,-1,-1,-1,-1]  # Initialize with -1 for no queens placed

    def is_goal(self):
        return self.heuristic() == 0

    def heuristic(self):
        h = 0
        for i in range(8):
            for j in range(i + 1, 8):
                if self.queens[i] == self.queens[j] or abs(self.queens[i] - self.queens[j]) == abs(i - j):
                    h += 1
                if -1 in self.queens:
                    h += 1
        return h

    def generate_successors(self):
        successors = []
        for row in range(8):
            for col in range(8):
                if col != self.queens[row]:
                    successor_queens = self.queens[:]
                    successor_queens[row] = col
                    successors.append(State(successor_queens))
        return successors

    def __lt__(self, other):
        return self.heuristic() < other.heuristic()

def astar():
    initial_state = State()
    open_list = [initial_state]
    closed_list = set()

    while open_list:
        current_state = open_list.pop(0)
        if current_state.is_goal():
            return current_state.queens

        closed_list.add(tuple(current_state.queens))

        successors = current_state.generate_successors()
        for successor in successors:
            if tuple(successor.queens) not in closed_list:
                open_list.append(successor)
                open_list.sort()

    return None

solution = astar()
if solution:
    print("Solution found:")
    for i in range(8):
        row = ["Q" if j == solution[i] else "." for j in range(8)]
        print(" ".join(row))
else:
    print("No solution found.")
