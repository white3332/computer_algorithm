from itertools import combinations

input = {
    "A" : (10, 60),
    "B" : (20, 100),
    "C" : (30, 120)
}

solutions = list(input.keys())
combo_length = len(solutions)

best_solutions = []

for combo_length in range(1,len(solutions)+1):
    for solution in combinations(solutions, combo_length):
        cost_sum = 0
        value_sum = 0
        for i in solution:
            cost_sum += input[i][0]
            value_sum += input[i][1]
            
        if cost_sum <= 50:
            best_solutions.append((solution, cost_sum, value_sum))

best_solution = max(best_solutions, key=lambda x: x[2])          
print(f"조합: {best_solution[0]}, 무게합: {best_solution[1]}, 가치합: {best_solution[2]}")