from dataclasses import dataclass

@dataclass
class ScheduleItem:
    subject: str
    catalog: str
    section: str
    component: str
    session: str
    units: int
    tot_enrl: int
    cap_enrl: int
    instructor: str

    def get_key(self):
        return f"{self.subject}_{self.catalog}_{self.section}"

    def print(self):
        print(f"{self.subject:5} {self.catalog:6} {self.section:6} "
              f"{self.component:8} {self.session:6} "
              f"{self.units:5} {self.tot_enrl:7} {self.cap_enrl:7} "
              f"{self.instructor}")
