student = []
course = []
marks = {}

def input_number_of_students():
    try:
        n = int(input())
        if n<0:
            print("invalid")
        continue
        return n
    except:
        print("Vui lòng nhập một số nguyên.")
def input_students():
    n = input_number("Nhập số lượng sinh viên: ")
    for i in range (n):
        sid = int(input("Ma sinh vien: "))
        name = input("Ho va ten sinh vien: ")
        dob = input("Ngay sinh: ")
        students.append({"Ho va ten: "+ str(name) + "Ma sinh vien: " + str(sid) + "Ngay sinh: "+ str(dob)})


def input_course():
    n = int(input("Nhap so luong mon hoc: "))
    for i in range(n):
        course_id = input("Nhap ma mon hoc : ")
        course_name = input("Nhap ten mon hoc: ")
        course.append({"Ten mon hoc: "+ str(course_name) + "Ma mon hoc: "+ str(course_id)})

def input_mark_for_course():
    
    
    