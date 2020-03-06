# myapi/urls.py
from django.urls import include, path
from rest_framework import routers
from . import views
from teacherapi.views import HandleRegisterRequest,HandleLoginRequest,HandleListRequest,RatingsOfAllProfessors,HandleLogoutRequest,AverageRatingOfProfessor,RateAProfessorGivenModule

router = routers.DefaultRouter()

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    # path('users', views.index,name='index'),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('register',HandleRegisterRequest),
    path('login',HandleLoginRequest),
    path('logout',HandleLogoutRequest),
    path('list', HandleListRequest),
    path('view',RatingsOfAllProfessors),
    path('average/<str:professor_code>/<str:module_id>',AverageRatingOfProfessor),
    path('rate',RateAProfessorGivenModule),

]
