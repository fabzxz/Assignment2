# Program Name: Assignment2.py
# Course: IT3883/Section XXX
# Student Name: Fabian Maqueda-MOnroy
# Assignment Number: Lab2
# Due Date: 02/14/2025
# Purpose: This program reads student names and their respective scores from an input file,
#          calculates their average score, and prints the students' names along with their
#          averages in descending order by grade.
# List Specific resources used to complete the assignment: Python Documentation

def main():
    file_name = r"C:\Users\Fabian\Downloads\Assignment2input.txt"
    student_averages = {}

    # Read the input file
    with open(file_name, 'r') as file:
        for line in file:
            parts = line.split()
            name = parts[0]
            scores = list(map(float, parts[1:]))
            student_averages[name] = sum(scores) / len(scores)  # Store name and average in a dictionary

    # Sort it by average in descending order
    sorted_students = sorted(student_averages.items(), key=lambda x: x[1], reverse=True)

    # Prints sorted results
    for name, avg in sorted_students:
        print(f"{name} {avg:.2f}")

if __name__ == "__main__":
    main()
