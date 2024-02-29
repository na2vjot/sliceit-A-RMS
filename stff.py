class Staff:
    def __init__(self, staff_id, username, role, phone, salary, daysoff, joined_date):
        self.staff_id = staff_id
        self.username = username
        self.role = role
        self.phone = phone
        self.salary = salary
        self.daysoff = daysoff
        self.joined_date = joined_date

class StaffManagement:
    def __init__(self):
        self.staffs = []

    def add_staff(self, staff):
        self.staffs.append(staff)

    def find_staff_by_id(self, staff_id):
        for staff in self.staffs:
            if staff.staff_id == staff_id:
                return staff
        return None

    def remove_staff(self, staff_id):
        staff = self.find_staff_by_id(staff_id)
        if staff:
            self.staffs.remove(staff)
            print("Staff member removed successfully.")
        else:
            print("Staff member not found.")

    def display_staffs(self):
        for staff in self.staffs:
            print(f"Staff ID: {staff.staff_id}, Username: {staff.username}, Role: {staff.role}")

# Sample usage
if __name__ == "__main__":
    staff_management = StaffManagement()

    # Adding staff members
    staff1 = Staff(1, "JohnDoe", "Waiter", "123-456-7890", 2500.00, "Saturday, Sunday", "2022-01-15")
    staff2 = Staff(2, "JaneSmith", "Chef", "987-654-3210", 3500.00, "Monday, Tuesday", "2021-12-10")
    staff_management.add_staff(staff1)
    staff_management.add_staff(staff2)

    # Display all staffs
    print("All Staff Members:")
    staff_management.display_staffs()

    # Remove a staff member
    staff_management.remove_staff(1)

    # Display all staffs after removal
    print("\nAll Staff Members after removal:")
    staff_management.display_staffs()
