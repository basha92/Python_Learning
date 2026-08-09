#this program calls for all functionalities into one.
from patient_manager import add_patient, view_patients, search_patient


def main():
    while True:
        print("----Patient Management System----")
        choice = input("Enter your choice: ")
        print("1. Add Patient")
        print("2. View Patients")
        print("3. Search Patient")
        print("4. Exit")
        if choice == "1":
            add_patient()
        elif choice == "2":
            view_patients()
        elif choice == "3":
            search_patient()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.")


if __name__ == "__main__":
    main()