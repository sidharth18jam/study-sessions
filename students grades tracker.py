def enter_data(school=None):
    if school is None:
        school = {}
    
    default_subjects = ['English', 'Hindi', 'Maths', 'Science', 'Social Studies']
    
    print("Enter data for the school's student grades tracker:")
    
    while True:
        class_name = input("Enter the name of class (or 'done' to finish): ").strip()
        if class_name.lower() == 'done':
            break

        if class_name not in school:
            school[class_name] = {}
        
        while True:
            student_name = input(f"Enter student name for class {class_name} (or 'done' to finish class): ").strip()
            if student_name.lower() == 'done':
                break

            if student_name not in school[class_name]:
                school[class_name][student_name] = {}

            print("Available subjects:")
            for i, subject in enumerate(default_subjects, 1):
                print(f"{i}. {subject}")
            print("6. Custom subject")

            while True:
                subject_choice = input("Enter subject number (or 'done' to finish student): ").strip()
                if subject_choice.lower() == 'done':
                    break

                try:
                    subject_choice = int(subject_choice)
                    if 1 <= subject_choice <= 5:
                        subject = default_subjects[subject_choice - 1]
                    elif subject_choice == 6:
                        subject = input("Enter custom subject name: ").strip()
                    else:
                        print("Invalid choice. Please enter a number between 1 and 6.")
                        continue
                except ValueError:
                    print("Invalid input. Please enter a number.")
                    continue

                if subject not in school[class_name][student_name]:
                    school[class_name][student_name][subject] = {'average': 0, 'marks': []}

                marks = input(f"Enter marks for {subject} (comma-separated, or press Enter for default 10 marks): ").strip()
                if marks:
                    try:
                        marks = [int(mark) for mark in marks.split(',')]
                    except ValueError:
                        print("Invalid input. Using default 10 marks.")
                        marks = [10] * 10
                else:
                    marks = [10] * 10

                school[class_name][student_name][subject]['marks'] = marks
                school[class_name][student_name][subject]['average'] = sum(marks) / len(marks)

    return school

def print_school_data(school):
    for class_name, students in school.items():
        print(f"\nClass: {class_name}")
        for student_name, subjects in students.items():
            print(f"  Student: {student_name}")
            for subject, data in subjects.items():
                print(f"    Subject: {subject}")
                print(f"      Average: {data['average']:.2f}")
                print(f"      Marks: {data['marks']}")

def change_marks(school):
    class_name = input("Enter class name: ").strip()
    if class_name not in school:
        print("Class not found.")
        return

    student_name = input("Enter student name: ").strip()
    if student_name not in school[class_name]:
        print("Student not found.")
        return

    subject = input("Enter subject name: ").strip()
    if subject not in school[class_name][student_name]:
        print("Subject not found.")
        return

    print(f"Current marks: {school[class_name][student_name][subject]['marks']}")
    new_marks = input("Enter new marks (comma-separated): ").strip()
    try:
        new_marks = [int(mark) for mark in new_marks.split(',')]
        school[class_name][student_name][subject]['marks'] = new_marks
        school[class_name][student_name][subject]['average'] = sum(new_marks) / len(new_marks)
        print("Marks updated successfully.")
    except ValueError:
        print("Invalid input. Please enter numbers separated by commas.")

def change_subjects(school):
    class_name = input("Enter class name: ").strip()
    if class_name not in school:
        print("Class not found.")
        return

    student_name = input("Enter student name: ").strip()
    if student_name not in school[class_name]:
        print("Student not found.")
        return

    print(f"Current subjects: {list(school[class_name][student_name].keys())}")
    action = input("Do you want to (a)dd or (r)emove a subject? ").strip().lower()

    if action == 'a':
        new_subject = input("Enter new subject name: ").strip()
        if new_subject not in school[class_name][student_name]:
            school[class_name][student_name][new_subject] = {'average': 0, 'marks': []}
            print(f"Subject '{new_subject}' added successfully.")
        else:
            print("Subject already exists.")
    elif action == 'r':
        subject_to_remove = input("Enter subject to remove: ").strip()
        if subject_to_remove in school[class_name][student_name]:
            del school[class_name][student_name][subject_to_remove]
            print(f"Subject '{subject_to_remove}' removed successfully.")
        else:
            print("Subject not found.")
    else:
        print("Invalid action.")

def add_student(school):
    class_name = input("Enter class name: ").strip()
    if class_name not in school:
        print("Class not found. Creating new class.")
        school[class_name] = {}

    student_name = input("Enter new student name: ").strip()
    if student_name not in school[class_name]:
        school[class_name][student_name] = {}
        default_subjects = ['English', 'Hindi', 'Maths', 'Science', 'Social Studies']
        for subject in default_subjects:
            school[class_name][student_name][subject] = {'average': 10, 'marks': [10] * 10}
        print(f"Student '{student_name}' added to class '{class_name}' with default subjects and marks.")
    else:
        print("Student already exists in this class.")

def top_students(school):
    class_name = input("Enter class name (or 'all' for all classes): ").strip()
    
    def calculate_average(subjects):
        total = sum(subject['average'] for subject in subjects.values())
        return total / len(subjects) if subjects else 0

    if class_name.lower() == 'all':
        for class_name, students in school.items():
            if students:
                top_student = max(students.items(), key=lambda x: calculate_average(x[1]))
                print(f"Top student in {class_name}: {top_student[0]} (Average: {calculate_average(top_student[1]):.2f})")
    elif class_name in school:
        students = school[class_name]
        if students:
            top_student = max(students.items(), key=lambda x: calculate_average(x[1]))
            print(f"Top student in {class_name}: {top_student[0]} (Average: {calculate_average(top_student[1]):.2f})")
        else:
            print(f"No students in {class_name}")
    else:
        print("Class not found.")

def main():
    school = {}
    while True:
        print("\n1. Enter/Add Data")
        print("2. Change Marks")
        print("3. Change Subjects")
        print("4. Add New Student")
        print("5. Display Top Students")
        print("6. Print School Data")
        print("7. Exit")
        
        choice = input("Enter your choice (1-7): ").strip()
        
        if choice == '1':
            school = enter_data(school)
        elif choice == '2':
            change_marks(school)
        elif choice == '3':
            change_subjects(school)
        elif choice == '4':
            add_student(school)
        elif choice == '5':
            top_students(school)
        elif choice == '6':
            print_school_data(school)
        elif choice == '7':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()