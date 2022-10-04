from .models import Student,Teacher,User, TimeTable
from .serializer import *

def create_student_details(data):
    student_data = data.copy()
    student_data["name"] = data.get("name")
    student_data["gender"] = data.get("gender")
    student_data["address"] = data.get("address")
    student_data["standard"] = data.get("standard")
    student_data["phone_number"] = data.get("phone_number")
    student_data["class_teacher"] = data.get("class_teacher")
    student_data["father_name"] = data.get("father_name")
    student_data["email"] = data.get("email")
    student_data.save()
    return response(StudentSerializer(student_data).data, status = status.HTTP_200_OK)


def create_admin(data):
    user, is_created = User.objects.get_or_create(email=data.get("email"),
                                                     username=data.get("email"))
    if is_created :
        user["name"] = data.get("name")
        user["phone_number"] = data.get("phone_number")
        user["job_level"] =  data.get("job")
        user["address"] = data.get("address")
        user.save()
        return {"success" : True ,"data":UserSerializer(student_data).data}

def create_teacher_details(data):
    teacher_data = data.copy()
    teacher_data["name"] = data.get("name")
    teacher_data["gender"] = data.get("gender")
    teacher_data["address"] = data.get("address")
    teacher_data["phone_number"] = data.get("phone_number")
    teacher_data["subject"] = data.get("subject")
    teacher_data["email"] = data.get("email")
    teacher.save()
    return { "success" : True , "data":TeacherSerializer(student_data).data } 

def retreive_timetable(data):
    if data.get("day") == 6 or data.get("day") == 7 :
        return "please enter a valid day"
    timetable = TimeTable.objects.get(day = data.get("day"),standard = data.get("standard"))
    return { "success" : True ,"data":TimeTableSerializer(timetable).data }


def retrieve_teacher_list():
    teacher = Teacher.objects.all()
    teacher = TeacherSerializer(teacher).data
    return { "success" : True , "data":teacher}

def retrieve_student_list():
    student = Student.objects.all()
    student = StudentSerializer(teacher).data
    return { "success" : True , "data":teacher}