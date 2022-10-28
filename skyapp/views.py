from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework.renderers import JSONRenderer
from rest_framework.viewsets import ViewSet
from rest_framework.authentication import TokenAuthentication

# Create your views here.
from .models import *
from .serializer import *
from django.contrib.auth.models import (User, Group, Permission)
from django.core.paginator import Paginator


class Testmodule(ViewSet):
    def all_Employees(self, request):
        auth_user = request.user.has_perm("skyapp.view_employee_list")
      
        if auth_user == False:
            response = {
                'message': 'You Dont have the permission to view this list',
                'status': False,
                'result': None
                }
            return Response(response,status=status.HTTP_403_FORBIDDEN)
        try:
            profiles = Employee.objects.all()
            paginator = Paginator(profiles, 10)
            query = paginator.page(int(2))
            serialized_profiles = Employee_serializer(query,many=True)

        except Exception as error:
            response = {
                'message': 'No Profiles Found',
                'status': False,
                'result': str(error)
            }
            
            return Response(response, status=status.HTTP_200_OK)

 
        
        return Response(serialized_profiles.data)
    def search_lastname(self, request,*args, **kwargs):

        lastname = kwargs['lastname']
        try:
            profiles = Employee.objects.filter(last_name=lastname).all()
            serialized_profiles = Employee_serializer(profiles,many=True)
            if not profiles:
                response = {
                    'message': 'No Profiles'
                }
                return Response(response, status=status.HTTP_200_OK)
        except Exception as error:
            response = {
                'message': 'No Profiles Found',
                'status': False,
                'result': str(error)
            }
            return Response(response, status=status.HTTP_200_OK)

        return Response(serialized_profiles.data)
    def search_by_department(self, request,*args, **kwargs):
        
        dep_id = kwargs['dep_id']
        try:
            profiles = Department.objects.filter(id=dep_id)
            serialized_profiles = Department_serializer(profiles,many=True)
            if not profiles:
                response = {
                    'message': 'No Profiles'
                }
                return Response(response, status=status.HTTP_200_OK)
        except Exception as error:
            response = {
                'message': 'No Profiles Found',
                'status': False,
                'result': str(error)
            }
            return Response(response, status=status.HTTP_200_OK)

        return Response(serialized_profiles.data)
    
class TeamMemmberView(viewsets.ModelViewSet):
    """
    Team view API viewset

    """
    queryset = Employee.objects.all()
    serializer_class = Employee_serializer


