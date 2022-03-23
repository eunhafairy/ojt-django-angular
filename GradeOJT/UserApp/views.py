from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

from django.http.response import JsonResponse
from UserApp.models import Roles, Sections, Users
from UserApp.serializer import RoleSerializer, SectionSerializer, UserSerializer

@csrf_exempt
def roleApi(request, id=0):
    if request.method =='GET':
        roles = Roles.objects.all()
        roles_serializer = RoleSerializer(roles, many=True)
        return JsonResponse(roles_serializer.data, safe=False)
    elif request.method=='POST':
        role_data = JSONParser().parse(request)
        roles_serializer = RoleSerializer(data=role_data)
        if roles_serializer.is_valid():
            roles_serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        return JsonResponse("Failed to add", safe=False)
    elif request.method =="PUT":
        role_data = JSONParser().parse(request)
        role = Roles.objects.get(RoleId=role_data['RoleId'])
        role_serializer = RoleSerializer(role, data = role_data)
        if role_serializer.is_valid():
            role_serializer.save()
            return JsonResponse("Updated Successfully", safe=False)
        return JsonResponse("Failed to Update", safe=False)
    elif request.method=='DELETE':
        role=Roles.objects.get(RoleId = id)
        role.delete()
        return JsonResponse("Deleted successfully!", safe=False)