# SRMS using List of Dictionaries

students = []

def add_student():
    name = input("Enter student name: ")
    roll = input("Enter roll number: ")
    subject = input("Enter subject: ")
    marks = int(input("Enter marks: "))
    student = {"name": name, "roll": roll, "subject": subject, "marks": marks}
    students.append(student)
    print(" Student added successfully!\n")

def display_students():
    if not students:
        print(" No records found!\n")
        return
    print("\n---- Student Records ----")
    for s in students:
        print(f"Name: {s['name']}, Roll: {s['roll']}, Subject: {s['subject']}, Marks: {s['marks']}")
    print()

def search_student():
    roll = input("Enter roll number to search: ")
    for s in students:
        if s["roll"] == roll:
            print(f"Found → Name: {s['name']}, Roll: {s['roll']}, Subject: {s['subject']}, Marks: {s['marks']}\n")
            return
    print(" Student not found!\n")
def update_student():
    roll = input("Enter roll number to update marks: ")
    for s in students:
        if s["roll"] == roll:
            new_marks = int(input("Enter new marks: "))
            s["marks"] = new_marks
            print(" Marks updated successfully!\n")
            return
    print(" Student not found!\n")

def delete_student():
    roll = input("Enter roll number to delete: ")
    for s in students:
        if s["roll"] == roll:
            students.remove(s)
            print(" Record deleted successfully!\n")
            return
    print(" Student not found!\n")

def sort_students():
    if not students:
        print(" No records to sort!\n")
        return
    students.sort(key=lambda x: x["marks"], reverse=True)
    print(" Records sorted by marks (descending order)!\n")

# Menu-driven program
while True:
    print("===== SRMS (List of Dictionaries) =====")
    print("1. Add Student")
    print("2. Display Students")
    print("3. Search Student")
    print("4. Update Student Marks")
    print("5. Delete Student")
    print("6. Sort Students by Marks")
    print("7. Exit")

    choice = input("Enter choice: ")

    if choice == '1':
        add_student()
    elif choice == '2':
        display_students()
    elif choice == '3':
        search_student()
    elif choice == '4':
        update_student()
    elif choice == '5':
        delete_student()
    elif choice == '6':
        sort_students()
    elif choice == '7':
        print(" Exiting program...")
        break
    else:
        print(" Invalid choice! Try again.\n")
