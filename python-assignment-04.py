try:
    with open('python_assignment_04.txt', 'r') as file:
        for line in file:
            print(line, end='')  # end='' avoids double newlines
except FileNotFoundError:
    print("Error: The file 'python_assignment_04.txt' does not exist.")
except Exception as e:
    print(f"An error occurred: {e}")

