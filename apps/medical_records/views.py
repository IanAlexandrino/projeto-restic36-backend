from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import MedicalRecord, MedicalPrescription, Exam, AccessHistory, Disease, DiseaseHistory, Diagnosis
from .serializers import MedicalRecordSerializer, MedicalPrescriptionSerializer, ExamSerializer, AccessHistorySerializer, DiseaseSerializer, DiseaseHistorySerializer, DiagnosisSerializer

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


@api_view(['GET', 'POST'])
def get_all_and_post_access_histories(request):

    if request.method == 'GET':

        try:
            patient = request.GET.get('patient', None)
            practitioner = request.GET.get('practitioner', None)

            if patient:

                access_histories_by_patient = AccessHistory.objects.filter(patient=patient)

                if access_histories_by_patient.exists():
                    serializer = AccessHistorySerializer(access_histories_by_patient, many=True)
                    return Response(serializer.data)
                
                else:
                    return Response({"detail": "No access histories found for the given patient."}, status=status.HTTP_404_NOT_FOUND)
                
            elif practitioner:

                access_histories_by_practitioner = AccessHistory.objects.filter(practitioner=practitioner)

                if access_histories_by_practitioner.exists():
                    serializer = AccessHistorySerializer(access_histories_by_practitioner, many=True)
                    return Response(serializer.data)
                
                else:
                    return Response({"detail": "No access histories found for the given practitioner."}, status=status.HTTP_404_NOT_FOUND)

            access_histories = AccessHistory.objects.all()

            serializer = AccessHistorySerializer(access_histories, many=True)

            return Response(serializer.data)
        
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        
    
    if request.method == 'POST':
        new_access_history = request.data

        serializer = AccessHistorySerializer(data=new_access_history)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def get_put_and_delete_access_history_by_id(request, id):

    try:
        access_history = AccessHistory.objects.get(pk=id)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = AccessHistorySerializer(access_history)
        return Response(serializer.data)
    
    if request.method == 'PUT':
        serializer = AccessHistorySerializer(access_history, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'DELETE':

        try:
            access_history.delete()
            return Response(status=status.HTTP_202_ACCEPTED)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    
    return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def get_all_and_post_diseases(request):

    if request.method == 'GET':

        try:
            diseases = Disease.objects.all()

            serializer = DiseaseSerializer(diseases, many=True)

            return Response(serializer.data)
        
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        
    
    if request.method == 'POST':
        new_disease = request.data

        serializer = DiseaseSerializer(data=new_disease)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def get_put_and_delete_disease_by_id(request, id):

    try:
        disease = Disease.objects.get(pk=id)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = DiseaseSerializer(disease)
        return Response(serializer.data)
    
    if request.method == 'PUT':
        serializer = DiseaseSerializer(disease, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'DELETE':

        try:
            disease.delete()
            return Response(status=status.HTTP_202_ACCEPTED)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    
    return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def get_all_and_post_diseases_histories(request):

    if request.method == 'GET':

        try:

            patient = request.GET.get('patient', None)

            if patient:

                disease_history_by_patient = DiseaseHistory.objects.filter(patient=patient)

                if disease_history_by_patient.exists():
                    serializer = DiseaseHistorySerializer(disease_history_by_patient)
                    return Response(serializer.data)
                
                else:
                    return Response({"detail": "No disease history found for the given patient."}, status=status.HTTP_404_NOT_FOUND)

            diseases_histories = DiseaseHistory.objects.all()

            serializer = DiseaseHistorySerializer(diseases_histories, many=True)

            return Response(serializer.data)
        
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        
    
    if request.method == 'POST':
        new_disease_history = request.data

        serializer = DiseaseHistorySerializer(data=new_disease_history)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def get_put_and_delete_disease_history_by_id(request, id):

    try:
        disease_history = DiseaseHistory.objects.get(pk=id)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = DiseaseHistorySerializer(disease_history)
        return Response(serializer.data)
    
    if request.method == 'PUT':
        serializer = DiseaseHistorySerializer(disease_history, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'DELETE':

        try:
            disease_history.delete()
            return Response(status=status.HTTP_202_ACCEPTED)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    
    return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def get_all_and_post_diagnostics(request):

    if request.method == 'GET':

        try:

            history = request.GET.get('history', None)

            if history:

                diagnostics_by_history = Diagnosis.objects.filter(history=history)

                if diagnostics_by_history.exists():
                    serializer = DiagnosisSerializer(diagnostics_by_history, many=True)
                    return Response(serializer.data)
                
                else:
                    return Response({"detail": "No diagnostics found for the given history."}, status=status.HTTP_404_NOT_FOUND)

            diagnostics = Diagnosis.objects.all()

            serializer = DiagnosisSerializer(diagnostics, many=True)

            return Response(serializer.data)
        
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        
    
    if request.method == 'POST':
        new_diagnosis = request.data

        serializer = DiagnosisSerializer(data=new_diagnosis)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def get_put_and_delete_diagnosis_by_id(request, id):

    try:
        diagnosis = Diagnosis.objects.get(pk=id)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = DiagnosisSerializer(diagnosis)
        return Response(serializer.data)
    
    if request.method == 'PUT':
        serializer = DiagnosisSerializer(diagnosis, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'DELETE':

        try:
            diagnosis.delete()
            return Response(status=status.HTTP_202_ACCEPTED)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    
    return Response(status=status.HTTP_400_BAD_REQUEST)