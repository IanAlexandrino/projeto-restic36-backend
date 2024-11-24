from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Institution, InstitutionType
from .serializers import InstitutionSerializer, InstitutionTypeSerializer

import json

@api_view(['GET', 'POST'])
def get_all_and_post_institution_types(request):

    if request.method == 'GET':
            intitution_types = InstitutionType.objects.all()

            serializer = InstitutionTypeSerializer(intitution_types, many=True)

            return Response(serializer.data)
    
    if request.method == 'POST':
        new_institution_type = request.data

        serializer = InstitutionTypeSerializer(data=new_institution_type)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
    return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def get_put_and_delete_institution_type_by_id(request, id):

    try:
        institution_type = InstitutionType.objects.get(pk=id)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = InstitutionTypeSerializer(institution_type)
        return Response(serializer.data)
    
    if request.method == 'PUT':
        serializer = InstitutionTypeSerializer(institution_type, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'DELETE':

        try:
            institution_type.delete()
            return Response(status=status.HTTP_202_ACCEPTED)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
def get_all_and_post_institutions(request):

    if request.method == 'GET':

        try:
            institution_type = request.GET.get('type', None)

            if institution_type:

                institutions_by_type = Institution.objects.filter(institution_type=institution_type)

                if institutions_by_type.exists():
                    serializer_by_type = InstitutionSerializer(institutions_by_type, many=True)
                    return Response(serializer_by_type.data)
                
                else:
                    return Response({"detail": "No institutions found for the given type."}, status=status.HTTP_404_NOT_FOUND)
            
            intitutions = Institution.objects.all()

            serializer = InstitutionSerializer(intitutions, many=True)

            return Response(serializer.data)
        
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
                
        
    
    if request.method == 'POST':
        new_institution = request.data

        serializer = InstitutionSerializer(data=new_institution)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
    return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def get_put_and_delete_institution_by_id(request, id):

    try:
        institution = Institution.objects.get(pk=id)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = InstitutionSerializer(institution)
        return Response(serializer.data)
    
    if request.method == 'PUT':
        serializer = InstitutionSerializer(institution, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'DELETE':

        try:
            institution.delete()
            return Response(status=status.HTTP_202_ACCEPTED)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    
    return Response(status=status.HTTP_400_BAD_REQUEST)