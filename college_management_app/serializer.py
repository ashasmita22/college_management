from .models import Student , Teacher , User

class StudentSerializer(serializers.ModelSerializer):

    class Meta :
        model = Student
        fields = '__all__'


class TeacherSerializer(serializers.ModelSerializer):

    class Meta :
        model = Teacher
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):

    class Meta :
        model = User()
        fields = '__all__'