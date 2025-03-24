def get_marks():
    """Function to get marks from the user."""
    subjects = int(input("Enter the number of subjects: "))
    print(f"Number of subjects entered: {subjects}")  # Print after input
    marks = []
    for i in range(subjects):
        mark = float(input(f"Enter marks for subject {i+1}: "))
        marks.append(mark)
        print(f"Marks entered for subject {i+1}: {mark}")  # Print after each mark entry
    return marks


def calculate_average(marks):
    """Function to calculate the average of marks."""
    average = sum(marks) / len(marks)
    print(f"Calculated average marks: {average:.2f}")  # Print after calculation
    return average

def determine_grade(average):
    """Function to determine grade based on average marks."""
    if average >= 90:
        grade = "A"
    elif average >= 80:
        grade = "B"
    elif average >= 70:
        grade = "C"
    elif average >= 60:
        grade = "D"
    else:
        grade = "F"
    print(f"Determined grade: {grade}")  # Print after determining grade
    return grade

def grade_calculator():
    """Main function to run the grade calculator."""
    print("Starting Grade Calculator...\n")  # Print before execution
    marks = get_marks()
    print(f"Marks list: {marks}")  # Print after marks collection
    
    average = calculate_average(marks)
    grade = determine_grade(average)
    
    print("\n---- Grade Report ----")
    print(f"Average Marks: {average:.2f}")
    print(f"Final Grade: {grade}")
    print("Grade calculation completed!")  # Print after final output

# Run the program
if __name__ == "__main__":
    grade_calculator()
