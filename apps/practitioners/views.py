from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Practitioner, PractitionerType
from .serializers import PractitionerSerializer, PractitionerTypeSerializer

import json

@api_view(['GET', 'POST'])
def get_all_and_post_practitioner_types(request):

    if request.method == 'GET':
            practitioner_types = PractitionerType.objects.all()

            serializer = PractitionerTypeSerializer(practitioner_types, many=True)

            return Response(serializer.data)
    
    if request.method == 'POST':
        new_practitioner_type = request.data

        serializer = PractitionerTypeSerializer(data=new_practitioner_type)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
    return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def get_put_and_delete_practitioner_type_by_id(request, id):

    try:
        practitioner_type = PractitionerType.objects.get(pk=id)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = PractitionerTypeSerializer(practitioner_type)
        return Response(serializer.data)
    
    if request.method == 'PUT':
        serializer = PractitionerTypeSerializer(practitioner_type, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'DELETE':

        try:
            practitioner_type.delete()
            return Response(status=status.HTTP_202_ACCEPTED)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
def get_all_and_post_practitioners(request):

    if request.method == 'GET':

        try:
            practitioner_type = request.GET.get('type', None)
            practitioner_institution = request.GET.get('institution', None)

            if practitioner_type and practitioner_institution:

                practitioners_by_type_and_institution = Practitioner.objects.filter(practitioner_type=practitioner_type, practitioner_institution=practitioner_institution)

                if practitioners_by_type_and_institution.exists():
                    serializer = PractitionerSerializer(practitioners_by_type_and_institution, many=True)
                    return Response(serializer.data)
                
                else:
                    return Response({"detail": "No Practitioner found for the given type or institution."}, status=status.HTTP_404_NOT_FOUND)
                
            elif practitioner_type:

                practitioners_by_type = Practitioner.objects.filter(practitioner_type=practitioner_type)

                if practitioners_by_type.exists():
                    serializer = PractitionerSerializer(practitioners_by_type, many=True)
                    return Response(serializer.data)
                
                else:
                    return Response({"detail": "No Practitioner found for the given type."}, status=status.HTTP_404_NOT_FOUND)    
            
            elif practitioner_institution:

                practitioners_by_institution = Practitioner.objects.filter(practitioner_institution=practitioner_institution)

                if practitioners_by_institution.exists():
                    serializer = PractitionerSerializer(practitioners_by_institution, many=True)
                    return Response(serializer.data)
                
                else:
                    return Response({"detail": "No Practitioner found for the given institution."}, status=status.HTTP_404_NOT_FOUND) 

            practitioners = Practitioner.objects.all()

            serializer = PractitionerSerializer(practitioners, many=True)

            return Response(serializer.data)
        
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
                
        
    
    if request.method == 'POST':
        new_practitioner = request.data

        serializer = PractitionerSerializer(data=new_practitioner)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
    return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def get_put_and_delete_practitioner_by_id(request, id):

    try:
        practitioner = Practitioner.objects.get(pk=id)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = PractitionerSerializer(practitioner)
        return Response(serializer.data)
    
    if request.method == 'PUT':
        serializer = PractitionerSerializer(practitioner, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'DELETE':

        try:
            practitioner.delete()
            return Response(status=status.HTTP_202_ACCEPTED)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    
    return Response(status=status.HTTP_400_BAD_REQUEST)