
from collections import defaultdict
# Create your views here.
import decimal
from rest_framework import viewsets
import http
from django.http import JsonResponse
from .serializers import UserSerializer
from .models import User,ProfessorTeachesModule,UserRatesProfessor
from rest_framework.response import Response
from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt,ensure_csrf_cookie
import json
from django.contrib.auth import authenticate,login,logout
from django.db.models import Avg
from django.views.decorators.csrf import ensure_csrf_cookie



@csrf_exempt
def HandleRegisterRequest(request): #receieves registration information, adds the user to the database


    if not request.user.is_authenticated:
        try:
            print(request.body)
            #loadjson databa
            user_data = json.loads(request.body)
            print(user_data)
            user = User.objects.create_user(user_data['username'],user_data['email'],user_data['password'])
            user.is_superuser = False
            user.is_staff = False
            user.save()
            return HttpResponse("you have been successfully registered, try logging in!")
        except:
            return HttpResponse("account creation has not worked, there must be a user with those account details")


    else:

        return HttpResponse("you cannot register an account whilst logged in")


def HandleLogoutRequest(request):

    if request.user.is_authenticated:
        logout(request)
        return HttpResponse("You have been logged out")
    else:
        return HttpResponse("you are not logged in")



@csrf_exempt
def HandleLoginRequest(request):

    if not request.user.is_authenticated:
        user_data = json.loads(request.body)
        user = authenticate(request,username=user_data['username'],password=user_data['password'])

        if user is not None:
            login(request,user)
            return HttpResponse("you have been successfully logged in, session set")

        else:
            return HttpResponse("there is no user with these credentials, try again")
    else:
        return HttpResponse("you are already logged in")

def HandleListRequest(request):

    list_teachers = []
    unique_module_instances = ProfessorTeachesModule.objects.values('module','module__name','semester').distinct()
    print("unique modules",unique_module_instances)

    for i in unique_module_instances:
        queryset = ProfessorTeachesModule.objects.filter(module_id=i['module'],semester=i['semester']).values('professor__name').distinct()
        print("for each i show list of teachers", queryset)
        queryset = list(queryset)
        list_of_teachers = {'module' : i['module__name'],'teachers':queryset,'semester':i['semester']}
        # list_of_teachers = [i['module__name'],[]]
        list_teachers.append(list_of_teachers)
        print(list_of_teachers, ",")

    list_teachers = tuple(list_teachers)


    return JsonResponse(list_teachers, safe=False)


def RatingsOfAllProfessors(request): #command on client application is: view

    # queryset = UserRatesProfessor.objects.values('module_instance__academic_year','module_instance','module_instance__professor__name','module_instance__module__name','module_instance__semester').annotate(Avg('rating')).distinct()
    queryset = UserRatesProfessor.objects.values('module_instance__professor__name').annotate(Avg('rating')).distinct()

    list_ratings = []
    queryset = list(queryset)

    for i in queryset:
        rounded_rating = decimal.Decimal(i['rating__avg']).quantize(decimal.Decimal('1'),
        rounding=decimal.ROUND_HALF_UP)
        professor_rating = {'rating':rounded_rating,'professor_name':i['module_instance__professor__name']}

        # professor_rating = {'rating':i['rating__avg'],'professor_name':i['module_instance__professor__name'],'module_name':i['module_instance__module__name'],'module_semester':i['module_instance__semester'],'module_year':i['module_instance__academic_year']}
        list_ratings.append(professor_rating)

    return JsonResponse(list_ratings, safe=False)



# @csrf_exempt
def AverageRatingOfProfessor(request,professor_code,module_id): #command for client application is: average

    print("inside average with parameters", professor_code,module_id)
    queryset = UserRatesProfessor.objects.filter(module_instance__professor__prof_cod=professor_code,module_instance__module__code=module_id).values('module_instance__module__name','module_instance__module','module_instance__professor__name').annotate(Avg('rating'))
    print(queryset)
    queryset = list(queryset)
    average_return = {}
    if len(queryset) != 0:
        rounded_rating = rounded_rating = decimal.Decimal(queryset[0]['rating__avg']).quantize(decimal.Decimal('1'),
        rounding=decimal.ROUND_HALF_UP)
        print(rounded_rating)
        average_return = {'professor':queryset[0]['module_instance__professor__name'],'rating':rounded_rating,'module_name':queryset[0]['module_instance__module__name']}
        return JsonResponse(average_return, safe=False)
    else:
        return JsonResponse(average_return)


@csrf_exempt #registeres a user given username email and pass
def RateAProfessorGivenModule(request):#command for client application is: rate

    print("inside rate a professor")
    module_rating = json.loads(request.body)
    print(module_rating)

    #check if module isntance exists
    if request.user.is_authenticated:
        try:
            user = User.objects.get(username=request.user.username)##put session stuff here when neeeded

            print("user is: " ,user)

            queryset = ProfessorTeachesModule.objects.get(professor__prof_cod=module_rating['professor_code'],module__code=module_rating['module_code'],academic_year=module_rating['year'],semester=module_rating['semester'])

            print("queryset is:", queryset)

            print("if valid this will not be empty", queryset)

            if queryset: # meaning the module instance exists
                rating = UserRatesProfessor.objects.create(user=user,rating=module_rating['rating'],module_instance=queryset)
                rating.save()
                print("saved the rating")
                return HttpResponse('rating has been saved!')

            else:
                print("not saved due to invalidity")
                return HttpResponse("this module instance doesn't exist")
        except:

            # print("this rating cannot be made, check that the module instance exists")
            return HttpResponse("this rating cannot be made, check that the module instance exists")

    else:
        return HttpResponse("you are not logged in, cannot rate!")
