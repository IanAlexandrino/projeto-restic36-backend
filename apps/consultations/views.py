from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Consultation, ConsultationType
from .serializers import ConsultationSerializer, ConsultationTypeSerializer

import json

@api_view(['GET', 'POST'])
def get_all_and_post_consultation_types(request):

    if request.method == 'GET':
            consultation_types = ConsultationType.objects.all()

            serializer = ConsultationTypeSerializer(consultation_types, many=True)

            return Response(serializer.data)
    
    if request.method == 'POST':
        new_consultation_type = request.data

        serializer = ConsultationTypeSerializer(data=new_consultation_type)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
    return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def get_put_and_delete_consultation_type_by_id(request, id):

    try:
        consultation_type = ConsultationType.objects.get(pk=id)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = ConsultationTypeSerializer(consultation_type)
        return Response(serializer.data)
    
    if request.method == 'PUT':
        serializer = ConsultationTypeSerializer(consultation_type, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'DELETE':

        try:
            consultation_type.delete()
            return Response(status=status.HTTP_202_ACCEPTED)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
def get_all_and_post_consultations(request):

    if request.method == 'GET':

        try:
            consultation_type = request.GET.get('type', None)

            if consultation_type:

                consultations_by_type = Consultation.objects.filter(consultation_type=consultation_type)

                if consultations_by_type.exists():
                    serializer_by_type = ConsultationSerializer(consultations_by_type, many=True)
                    return Response(serializer_by_type.data)
                
                else:
                    return Response({"detail": "No consultations found for the given type."}, status=status.HTTP_404_NOT_FOUND)
            
            consultations = Consultation.objects.all()

            serializer = ConsultationSerializer(consultations, many=True)

            return Response(serializer.data)
        
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
                
        
    
    if request.method == 'POST':
        new_consultation = request.data

        serializer = ConsultationSerializer(data=new_consultation)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
    return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def get_put_and_delete_consultation_by_id(request, id):

    try:
        consultation = Consultation.objects.get(pk=id)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = ConsultationSerializer(consultation)
        return Response(serializer.data)
    
    if request.method == 'PUT':
        serializer = ConsultationSerializer(consultation, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'DELETE':

        try:
            consultation.delete()
            return Response(status=status.HTTP_202_ACCEPTED)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    
    return Response(status=status.HTTP_400_BAD_REQUEST)