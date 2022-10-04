from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from .views import StudentCreation , UserCreation , TeacherCreation , TimeTableView , TeacherList , StudentList , LoginView
router = DefaultRouter()

urlpatterns = [
    url(r'^login/',LoginView.as_view()),
    url(r'^student_registration/', StudentCreation.as_view()),
    url(r'^user_create/',UserCreation.as_view()),
    url(r'^teacher_registration/',UserCreation.as_view()),
    url(r'^timetable/',TimeTableView().as_view()),
    url(r'^teacher_list/',TeacherList.as_view()),
    url(r'^student_list/',StudentList.as_view()),
    ]