
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Empty dataframe stored in memory only
students = pd.DataFrame(columns=["ID", "Name", "Branch", "Year", "Email"])


# FUNCTION: Add Student
def add_student():
    global students
    print("\n--- ADD NEW STUDENT ---")

    student_id = int(np.random.randint(1000, 9999))  # using numpy
    name = input("Enter Name: ")
    branch = input("Enter Branch: ")
    year = input("Enter Year: ")
    email = input("Enter Email: ")

    new_row = pd.DataFrame([[student_id, name, branch, year, email]],
                           columns=["ID", "Name", "Branch", "Year", "Email"])

    students = pd.concat([students, new_row], ignore_index=True)

    print(f"\nStudent added successfully with ID: {student_id}")


# FUNCTION: View all students
def view_students():
    print("\n--- STUDENT LIST ---")
    if students.empty:
        print("No students added yet.")
    else:
        print(students)


# FUNCTION: Search student by ID
def search_student():
    print("\n--- SEARCH STUDENT ---")
    sid = int(input("Enter Student ID: "))

    result = students[students["ID"] == sid]

    if not result.empty:
        print("\nStudent Found:")
        print(result)
    else:
        print("\nNo student found with this ID.")


# FUNCTION: Update student
def update_student():
    global students
    print("\n--- UPDATE STUDENT ---")
    sid = int(input("Enter Student ID: "))

    if sid in students["ID"].values:
        idx = students[students["ID"] == sid].index[0]

        print("\nLeave blank if you want to keep old value:")

        new_name = input("New Name: ")
        new_branch = input("New Branch: ")
        new_year = input("New Year: ")
        new_email = input("New Email: ")

        if new_name: students.at[idx, "Name"] = new_name
        if new_branch: students.at[idx, "Branch"] = new_branch
        if new_year: students.at[idx, "Year"] = new_year
        if new_email: students.at[idx, "Email"] = new_email

        print("\nStudent updated successfully!")
    else:
        print("\nID not found!")


# FUNCTION: Delete Student
def delete_student():
    global students
    print("\n--- DELETE STUDENT ---")
    sid = int(input("Enter Student ID: "))

    if sid in students["ID"].values:
        students = students[students["ID"] != sid]
        print("\nStudent deleted successfully!")
    else:
        print("\nStudent not found.")


# FUNCTION: Plot Branch Graph
def plot_branch_chart():
    print("\n--- BRANCH DISTRIBUTION ---")

    if students.empty:
        print("No data to display.")
        return

    counts = students["Branch"].value_counts()

    plt.figure(figsize=(6,4))
    plt.bar(counts.index, counts.values)
    plt.title("Branch Distribution")
    plt.xlabel("Branch")
    plt.ylabel("Number of Students")
    plt.show()


# MAIN MENU
def main():
    while True:
        print("\n======= STUDENT TRACK RECORDER =======")

        options = [
            "Add Student",
            "View Students",
            "Search Student",
            "Update Student",
            "Delete Student",
            "Show Branch Chart",
            "Exit Program"
        ]

        # Display using for-loop + range
        for i in range(len(options)):
            print(f"{i+1}. {options[i]}")

        choice = input("\nEnter your choice (1-7): ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            update_student()
        elif choice == "5":
            delete_student()
        elif choice == "6":
            plot_branch_chart()
        elif choice == "7":
            print("\nExiting…")
            break
        else:
            print("\nInvalid choice, try again.")


main()



