from django.db import models
import datetime
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

#can define all years up to todays date
def year_choices():
    return [(r,r) for r in range(1984, datetime.date.today().year+1)]
# Create your models here.
def current_year():
    return datetime.date.today().year


class Professor(models.Model):
    prof_cod = models.CharField(max_length=10,unique=True,default='n/a')
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)

    def __str__(self):
        return self.name + " " + self.surname


class Module(models.Model):
    name = models.CharField(max_length=30)
    code = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class ProfessorTeachesModule(models.Model):#module_instance
    professor = models.ForeignKey(Professor,on_delete=models.CASCADE,default=None)
    module = models.ForeignKey(Module, on_delete=models.CASCADE,default=None)
    academic_year = models.IntegerField(validators=[MaxValueValidator(current_year),MinValueValidator(1980)])
    semester = models.IntegerField(validators=[MaxValueValidator(2),MinValueValidator(1)])


    def __str__(self):
        return self.module.code + " taught by " + self.professor.name  + "with id: "+ str(self.professor.prof_cod) +" in semester " + str(self.semester) + " in year " +  str(self.academic_year) + " instance id : " + str(self.id)

class UserRatesProfessor(models.Model):
    user = models.ForeignKey(User, blank = False, null=True, on_delete=models.SET_NULL)
    rating = models.IntegerField(default=1,validators = [MaxValueValidator(5),MinValueValidator(1)])
    module_instance = models.ForeignKey(ProfessorTeachesModule,blank=False,null=True,on_delete=models.CASCADE)


    def __str__(self):
        return self.user.username + " rates " + str(self.module_instance.professor) + " teaching " + str(self.module_instance.module) + "with professor id: " + str(self.module_instance.professor.prof_cod)+ self.module_instance.professor.name +  " in semester " + str(self.module_instance.semester) + " a " + str(self.rating) + "module code is:" + self.module_instance.module.code

# class ProfessorTeachesModule(models.Model):
#     professor = models.ForeignKey(Professor,blank = False, null=True, on_delete=models.SET_NULL)
#     module = models.ForeignKey(Module,blank = False, null=True, on_delete=models.SET_NULL)
#     academic_year = models.IntegerField()
#     semester = models.IntegerField()
