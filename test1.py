class Person:
    def __init__(self, id, name, dob):
        self._id = id
        self._name = name
        self._dob = dob

    def get_id(self):
        return self._id

    def get_name(self):
        return self._name

    def get_dob(self):
        return self._dob

    def display(self):
        print(f"{self._id} - {self._name} - {self._dob}")


class Student(Person):
    def __init__(self, id, name, dob):
        super().__init__(id, name, dob)
        self._marks = {}

    def set_mark(self, course_id, mark):
        self._marks[course_id] = mark

    def get_mark(self, course_id):
        return self._marks.get(course_id, None)

    def display(self):
        marks_str = ', '.join([f"{cid}: {m}" for cid, m in self._marks.items()]) or "No marks"
        print(f"{self._id} - {self._name} - {self._dob} - Marks: {marks_str}")


class Course:
    def __init__(self, course_id, name):
        self._course_id = course_id
        self._name = name

    def get_course_id(self):
        return self._course_id

    def get_name(self):
        return self._name

    def display(self):
        print(f"{self._course_id} - {self._name}")


class MarkManager:
    def __init__(self):
        self.students = []
        self.courses = []

    def input_number(self, message):
        while True:
            try:
                n = int(input(message))
                if n > 0:
                    return n
                print("Number must be > 0.")
            except ValueError:
                print("Please enter an integer.")

    def input_students(self):
        n = self.input_number("Enter number of students: ")
        for _ in range(n):
            sid = input("Student ID: ")
            name = input("Name: ")
            dob = input("Date of birth: ")
            self.students.append(Student(sid, name, dob))

    def input_courses(self):
        n = self.input_number("Enter number of courses: ")
        for _ in range(n):
            cid = input("Course ID: ")
            name = input("Course name: ")
            self.courses.append(Course(cid, name))

    def input_marks(self):
        print("\nSelect a course to enter marks:")
        self.list_courses()
        cid = input("Enter course ID: ")
        selected_course = None
        for c in self.courses:
            if c.get_course_id() == cid:
                selected_course = c
                break
        if selected_course is None:
            print("Course not found!")
            return
        print(f"\nEntering marks for course {selected_course.get_name()}:")
        for st in self.students:
            while True:
                try:
                    mark = float(input(f"Mark for {st.get_name()}: "))
                    if 0 <= mark <= 20:
                        st.set_mark(cid, mark)
                        break
                    else:
                        print("Mark must be between 0 and 20.")
                except ValueError:
                    print("Please enter a number.")

    def list_students(self):
        print("\n--- STUDENTS ---")
        for s in self.students:
            s.display()

    def list_courses(self):
        print("\n--- COURSES ---")
        for c in self.courses:
            c.display()

    def show_marks(self):
        cid = input("Enter course ID to show marks: ")
        print(f"\n--- Marks for Course {cid} ---")
        for st in self.students:
            mark = st.get_mark(cid)
            if mark is None:
                print(f"{st.get_name()}: No mark")
            else:
                print(f"{st.get_name()}: {mark}")


def main():
    manager = MarkManager()
    manager.input_students()
    manager.input_courses()
    manager.input_marks()
    manager.list_students()
    manager.list_courses()
    manager.show_marks()


if __name__ == "__main__":
    main()