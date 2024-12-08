from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import MedicalRecord, MedicalPrescription, Exam
from .serializers import MedicalRecordSerializer, MedicalPrescriptionSerializer, ExamSerializer
import json

@api_view(['GET', 'POST'])
def get_all_and_post_medical_records(request):

    if request.method == 'GET':
            medical_records = MedicalRecord.objects.all()

            serializer = MedicalRecordSerializer(medical_records, many=True)

            return Response(serializer.data)
    
    if request.method == 'POST':
        new_medical_record = request.data

        serializer = MedicalRecordSerializer(data=new_medical_record)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def get_put_and_delete_medical_record_by_id(request, id):

    try:
        medical_record = MedicalRecord.objects.get(pk=id)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = MedicalRecordSerializer(medical_record)
        return Response(serializer.data)
    
    if request.method == 'PUT':
        serializer = MedicalRecordSerializer(medical_record, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'DELETE':

        try:
            medical_record.delete()
            return Response(status=status.HTTP_202_ACCEPTED)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def get_all_and_post_medical_prescriptions(request):

    if request.method == 'GET':

        try:
            patient = request.GET.get('patient', None)

            if patient:

                medical_prescriptions_by_patient = MedicalPrescription.objects.filter(patient=patient)

                if medical_prescriptions_by_patient.exists():
                    serializer = MedicalPrescriptionSerializer(medical_prescriptions_by_patient, many=True)
                    return Response(serializer.data)
                
                else:
                    return Response({"detail": "No medical prescriptions found for the given patient."}, status=status.HTTP_404_NOT_FOUND)
            
            medical_prescriptions = MedicalPrescription.objects.all()

            serializer = MedicalPrescriptionSerializer(medical_prescriptions, many=True)

            return Response(serializer.data)
        
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
                
        
    
    if request.method == 'POST':
        new_medical_prescription = request.data

        serializer = MedicalPrescriptionSerializer(data=new_medical_prescription)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def get_put_and_delete_medical_prescription_by_id(request, id):

    try:
        medical_prescription = MedicalPrescription.objects.get(pk=id)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = MedicalPrescriptionSerializer(medical_prescription)
        return Response(serializer.data)
    
    if request.method == 'PUT':
        serializer = MedicalPrescriptionSerializer(medical_prescription, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'DELETE':

        try:
            medical_prescription.delete()
            return Response(status=status.HTTP_202_ACCEPTED)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    
    return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def get_all_and_post_exams(request):

    if request.method == 'GET':

        try:
            patient = request.GET.get('patient', None)

            if patient:

                exams_by_patient = Exam.objects.filter(patient=patient)

                if exams_by_patient.exists():
                    serializer = ExamSerializer(exams_by_patient, many=True)
                    return Response(serializer.data)
                
                else:
                    return Response({"detail": "No exams found for the given patient."}, status=status.HTTP_404_NOT_FOUND)
            
            exams = Exam.objects.all()

            serializer = ExamSerializer(exams, many=True)

            return Response(serializer.data)
        
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        
    
    if request.method == 'POST':
        new_exam = request.data

        serializer = ExamSerializer(data=new_exam)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def get_put_and_delete_exam_by_id(request, id):

    try:
        exam = Exam.objects.get(pk=id)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = ExamSerializer(exam)
        return Response(serializer.data)
    
    if request.method == 'PUT':
        serializer = ExamSerializer(exam, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'DELETE':

        try:
            exam.delete()
            return Response(status=status.HTTP_202_ACCEPTED)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    
    return Response(status=status.HTTP_400_BAD_REQUEST)