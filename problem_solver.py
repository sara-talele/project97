def solve_problem():
    problem = input("Enter a math problem (e.g., '2 + 2'): ")

    try:
        result = eval(problem)
        print(f"The result is: {result}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    while True:
        solve_problem()
