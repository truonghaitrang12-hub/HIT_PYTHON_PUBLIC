class Employee:
    def __init__(self, name, salary, department):
        self.name = name
        self.__salary = salary
        self._department = department

    def get_salary(self):
        return self.__salary

    def increase_salary(self, amount):
        if amount > 0:
            self.__salary += amount
            print(f"Đã tăng lương cho {self.name} thêm {amount}")
        else:
            print("Số tiền phải lớn hơn không")

    def calculate_bonus(self):
        return self.__salary * 0.05

    def show_info(self):
        print(f"Tên: {self.name}")
        print(f"Lương: {self.get_salary():,.0f} VNĐ")
        print(f"Phòng ban: {self._department}")
        print(f"Tiền thưởng: {self.calculate_bonus():,.0f} VNĐ")
        print("-" * 40)


class Developer(Employee):
    def __init__(self, name, salary, department,
                 programming_language, overtime_hours):

        super().__init__(name, salary, department)

        self.programming_language = programming_language
        self.overtime_hours = overtime_hours

    def calculate_bonus(self):
        return self.get_salary() * 0.10 + self.overtime_hours * 100000

    def show_info(self):
        super().show_info()
        print(f"Ngôn ngữ lập trình: {self.programming_language}")
        print(f"Số giờ tăng ca: {self.overtime_hours}")
        print("-" * 40)


class Manager(Employee):
    def __init__(self, name, salary, department, number_of_employees):

        super().__init__(name, salary, department)

        self.number_of_employees = number_of_employees

    def calculate_bonus(self):
        return self.get_salary() * 0.15 + self.number_of_employees * 200000

    def show_info(self):
        super().show_info()
        print(f"Số nhân viên quản lý: {self.number_of_employees}")
        print("-" * 40)



employee1 = Employee("Nguyễn An", 10000000, "Nhân sự")

employee2 = Developer(
    "Trần Bình",
    15000000,
    "Công nghệ thông tin",
    "Python",
    10
)

employee3 = Developer(
    "Lê Chi",
    18000000,
    "Công nghệ thông tin",
    "Java",
    5
)

employee4 = Manager(
    "Phạm Dũng",
    25000000,
    "Quản lý",
    8
)

employees = [employee1, employee2, employee3, employee4]



print(" THÔNG TIN NHÂN VIÊN ")

for employee in employees:
    employee.show_info()



highest_salary_employee = max(
    employees,
    key=lambda employee: employee.get_salary()
)

print("NHÂN VIÊN CÓ LƯƠNG CAO NHẤT ")

print(
    highest_salary_employee.name,
    "-",
    f"{highest_salary_employee.get_salary():,.0f} VNĐ"
)


total_bonus = sum(
    employee.calculate_bonus()
    for employee in employees
)

print("\n TỔNG TIỀN THƯỞNG ")
print(f"{total_bonus:,.0f} VNĐ")


developer_count = sum(
    isinstance(employee, Developer)
    for employee in employees
)

manager_count = sum(
    isinstance(employee, Manager)
    for employee in employees
)

print("\n THỐNG KÊ ")
print("Số Developer:", developer_count)
print("Số Manager:", manager_count)



print("\n===== KIỂM TRA TĂNG LƯƠNG =====")

employee1.increase_salary(1000000)

print(
    employee1.name,
    "- Lương mới:",
    f"{employee1.get_salary():,.0f} VNĐ"
)