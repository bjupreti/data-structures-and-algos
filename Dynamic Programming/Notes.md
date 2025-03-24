Framework for solving DP Problems:
1. Define the objective function
f(i) is the distinct no. of ways to reach the ith stair.

2. Identify the base cases
f(0) = 1
f(1) = 1

3. Write down a recurrence relation for the optimized objective function
f(n) = f(n - 1) + f(n - 2)

4. What's the order of execution?
top-down | bottom-up

5. Where to look for the answer?
f(n) | f(0) | ...