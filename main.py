from schedule import Schedule

def print_results(results):
    if not results:
        print("No results found.")
        return

    print(f"{'Subject':6} {'Catalog':8} {'Section':8} {'Component':10} "
          f"{'Session':8} {'Units':6} {'TotEnrl':8} {'CapEnrl':8} Instructor")
    print("-" * 90)

    for item in results:
        item.print()

def main():
    schedule = Schedule()
    schedule.load_from_file("courses.csv")

    while True:
        print("\n--- COURSE SCHEDULE SYSTEM ---")
        print("1. Display all courses")
        print("2. Search by subject")
        print("3. Search by subject + catalog")
        print("4. Search by instructor last name")
        print("5. Quit")

        choice = input("Enter choice: ")

        if choice == "1":
            schedule.print()

        elif choice == "2":
            subject = input("Enter subject (e.g., BIO): ")
            results = schedule.find_by_subject(subject)
            print_results(results)

        elif choice == "3":
            subject = input("Enter subject: ")
            catalog = input("Enter catalog number: ")
            results = schedule.find_by_subject_catalog(subject, catalog)
            print_results(results)

        elif choice == "4":
            last_name = input("Enter instructor last name: ")
            results = schedule.find_by_instructor_last_name(last_name)
            print_results(results)

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
