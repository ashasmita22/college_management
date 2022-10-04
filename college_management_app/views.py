from django.shortcuts import render
from rest_framework.response import Response
from django.shortcuts import render,HttpResponse, redirect,HttpResponseRedirect
from django.contrib.auth import logout, authenticate, login
from .models import Student,Teacher ,Admin
from django.contrib import messages
from rest_framework.views import APIView
from .helper import create_admin,create_student_details,create_teacher_details, retrieve_timetable,retrieve_teacher_list
from django.contrib.auth import authenticate, login , logout

def LoginView(request):
    def post(self, request, *args, **kwargs):
        username = request.data['username']
        password = request.data['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
        else :
            return "Invalid User"


class StudentCreation(APIView, BaseApiMixin):
    def post(self, request, *args, **kwargs):
        try:
            response = create_student_details(request.data)
            return Response(response)
        except Exception as e:
            return str(e)

class TeacherCreation(APIView,BaseApiMixin):
    def post(self, request, *args, **kwargs):
        try:
            response = create_student_details(request.data)
            return Response(response)
        except Exception as e:
            return str(e)

    
class UserCreation(APIView, BaseApiMixin):
    def post(self, request, *args, **kwargs):
        try:
            response = create_admin(request.data)
            return Response(response)
        except Exception as e:
            return str(e)

class TimeTableView(APIView):
    def get(self, request, *args, **kwargs):
        try :
            response = retrieve_timetable(request.data)
            return Response(response)
        except Exception as e :
            return str(e)

class TeacherList(APIView):
    def get(self, request, *args, **kwargs):
        try :
            response = retrieve_teacher_list()
            return Response(response)
        except Exception as e :
            return str(e)


class StudentList(APIView):
    def get(self, request, *args, **kwargs):
        try :
            response = retrieve_teacher_list()
            return Response(response)
        except Exception as e :
            return str(e)


class LogoutView(request):
    def post(self, request, *args, **kwargs):
        logout(request)