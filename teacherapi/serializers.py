#tells the rest framework how you want to represent the data from the database
#


from rest_framework import serializers

from django.contrib.auth.models import User
from teacherapi.models import Module, Professor,UserRatesProfessor,ProfessorTeachesModule


class UserSerializer(serializers.HyperlinkedModelSerializer): ##links the user with its serialiser
    class Meta:
        model=User
        fields = ('username','email','password')
