students = {}

def add_student():
    roll = input("Enter Roll Number: ")
    name = input("Enter Student Name: ")
    age = int(input("Enter Age: "))

    marks = []
    for i in range(3):
        mark = float(input(f"Enter Subject {i+1} Marks: "))
        marks.append(mark)

    students[roll] = {
        "name": name,
        "age": age,
        "marks": marks
    }
    print("Student added successfully!")

def display_students():
    if not students:
        print("No student records found.")
        return

    for roll, data in students.items():
        total = sum(data["marks"])
        average = total / 3

        print("\n--------------------")
        print("Roll Number:", roll)
        print("Name:", data["name"])
        print("Age:", data["age"])
        print("Marks:", data["marks"])
        print("Total:", total)
        print("Average:", average)

        if average >= 90:
            grade = "A+"
        elif average >= 75:
            grade = "A"
        elif average >= 60:
            grade = "B"
        elif average >= 40:
            grade = "C"
        else:
            grade = "Fail"

        print("Grade:", grade)

def search_student():
    roll = input("Enter Roll Number to search: ")

    if roll in students:
        print("Student Found!")
        print(students[roll])
    else:
        print("Student not found.")

def delete_student():
    roll = input("Enter Roll Number to delete: ")

    if roll in students:
        del students[roll]
        print("Student deleted successfully!")
    else:
        print("Student not found.")

def main():
    while True:
        print("\n===== STUDENT MANAGEMENT SYSTEM =====")
        print("1. Add Student")
        print("2. Display Students")
        print("3. Search Student")
        print("4. Delete Student")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            display_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            delete_student()
        elif choice == "5":
            print("Thank you!")
            break
        else:
            print("Invalid choice!")

main()