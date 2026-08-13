# class Person :
#     def __init__(self,name, age):
#         self.name=name
#         self.age=age

#     def introduce(self):
#         print(f"toi ten la:{self.name}")
#         print(f"tuoi:{self.age}")


# class Student(Person):
#     def __init__(self, name, age, student_id):
#         super().__init__(name, age)
#         self.student_id = student_id

#     def introduce(self):
#         print(
#             f"Tôi tên là {self.name}, {self.age} tuổi, "
#             f"mã sinh viên là {self.student_id}."
#         )


# class Teacher(Person):
#     def __init__(self, name, age,subject):
#         super().__init__(name, age)
#         self.subject=subject

#     def introduce(self):
#         print(f"toi la giao vien dạy mon{self.subject}")

# student1= Student("Vu cao hong phuc",20,1234)
# student1.introduce()

# teacher1= Teacher("a",60,"ktmt")
# teacher1.introduce()
class vehicle :
    def __init__(self, brand, speed):
        self.brand=brand
        self.speed=speed


    def checkspeed(self,speed):
        if speed<0:
            print("toc do ko hop le")
            return
        print()