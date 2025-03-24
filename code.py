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
