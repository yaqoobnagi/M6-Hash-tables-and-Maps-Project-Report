import csv
from schedule_item import ScheduleItem

class Schedule:
    def __init__(self):
        self.data = {}   # dictionary to store ScheduleItem objects

    def add_entry(self, item):
        self.data[item.get_key()] = item

    def print_header(self):
        print(f"{'Subject':6} {'Catalog':8} {'Section':8} {'Component':10} "
              f"{'Session':8} {'Units':6} {'TotEnrl':8} {'CapEnrl':8} Instructor")
        print("-" * 90)

    def print(self):
        self.print_header()
        for item in self.data.values():
            item.print()

    def load_from_file(self, filename):
        with open(filename, encoding='utf-8-sig', newline='') as file:
            reader = csv.DictReader(file)

            for row in reader:
                item = ScheduleItem(
                    subject=row["Subject"],
                    catalog=row["Catalog"],
                    section=row["Section"],
                    component=row["Component"],
                    session=row["Session"],
                    units=int(row["Units"]),
                    tot_enrl=int(row["TotEnrl"]),
                    cap_enrl=int(row["CapEnrl"]),
                    instructor=row["Instructor"]
                )
                self.add_entry(item)

    # SEARCH METHODS (use list comprehensions)

    def find_by_subject(self, subject):
        return [item for item in self.data.values()
                if item.subject.lower() == subject.lower()]

    def find_by_subject_catalog(self, subject, catalog):
        return [item for item in self.data.values()
                if item.subject.lower() == subject.lower()
                and item.catalog == catalog]

    def find_by_instructor_last_name(self, last_name):
        return [item for item in self.data.values()
                if item.instructor.split(",")[0].lower() == last_name.lower()]
