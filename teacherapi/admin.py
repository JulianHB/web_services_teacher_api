#registers all the database models with the admin site so that modifications of the models
#are possible from the web ui




from django.contrib import admin

# Register your models here.
from django.contrib import admin
from teacherapi.models import Module, Professor,UserRatesProfessor,ProfessorTeachesModule

admin.site.register(Module)
admin.site.register(Professor)
admin.site.register(UserRatesProfessor)
admin.site.register(ProfessorTeachesModule)
