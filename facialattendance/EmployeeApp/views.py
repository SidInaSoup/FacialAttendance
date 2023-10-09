from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http import JsonResponse, StreamingHttpResponse
from django.core.files.storage import default_storage

from EmployeeApp.camera import VideoCamera
import cv2,os,urllib.request
import numpy as np
import csv
from EmployeeApp.models import Departments, Employees, Attendance
from EmployeeApp.serializers import DepartmentSerializer,EmployeeSerializer,AttendanceSerializer

csvPath = "Attendance.csv"

# Create your views here.

@csrf_exempt
def departmentApi(request,id=0):
    if request.method=='GET':
        departments = Departments.objects.all()
        departments_serializer = DepartmentSerializer(departments,many=True)
        return JsonResponse(departments_serializer.data,safe=False)
    elif request.method=='POST':
        department_data=JSONParser().parse(request)
        departments_serializer=DepartmentSerializer(data=department_data)
        if departments_serializer.is_valid():
            departments_serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        return JsonResponse("Failed to Add", safe=False)

    elif request.method=="PUT":
        department_data = JSONParser().parse(request)
        department=Departments.objects.get(DepartmentId=department_data['DepartmentId'])
        departments_serializer=DepartmentSerializer(department,data=department_data)
        if departments_serializer.is_valid():
            departments_serializer.save()
            return JsonResponse("Update Successful",safe=False)
        return JsonResponse("Failed to Update",safe=False)

    elif request.method=="DELETE":
        department=Departments.objects.get(DepartmentId=id)
        department.delete()
        return JsonResponse("deleted successfully",safe=False)

@csrf_exempt
def employeeApi(request, id=0):
    if request.method == 'GET':
        employees = Employees.objects.all()
        employees_serializer = EmployeeSerializer(employees, many=True)
        return JsonResponse(employees_serializer.data, safe=False)

    elif request.method == 'POST':
        employee_data = JSONParser().parse(request)
        employees_serializer = EmployeeSerializer(data=employee_data)
        if employees_serializer.is_valid():
            employees_serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        return JsonResponse("Failed to Add", safe=False)

    elif request.method == "PUT":
        employee_data = JSONParser().parse(request)
        try:
            employee = Employees.objects.get(EmployeeId=employee_data['EmployeeId'])  # Adjust the field to match your Employee model
        except:
            return JsonResponse(f"Employee not found (Id:{id})", safe=False)
        employees_serializer = EmployeeSerializer(employee, data=employee_data)
        if employees_serializer.is_valid():
            employees_serializer.save()
            return JsonResponse("Update Successful", safe=False)
        return JsonResponse("Failed to Update", safe=False)

    elif request.method == "DELETE":
        employee = Employees.objects.get(EmployeeId=id)  # Adjust the field to match your Employee model
        employee.delete()
        return JsonResponse("Deleted Successfully", safe=False)


# def csvDel(Name):
#     data = []
#     with open(csvPath, mode='r') as file:
#         reader = csv.DictReader(file)
#         for row in reader:
#             data.append(row)

#     # Initialize a flag to check if a match is found
#     match_found = False

#     # Loop through the data to find and remove the row with the specified value
#     for row in data:
#         if row['column_name_to_match'] == target_value:
#             data.remove(row)
#             match_found = True

#     # Check if a match was found
#     if match_found:
#         # Write the modified data back to the CSV file
#         with open(csv_file_path, mode='w', newline='') as file:
#             fieldnames = data[0].keys() if data else []
#             writer = csv.DictWriter(file, fieldnames=fieldnames)
            
#             # Write the header row
#             writer.writeheader()
            
#             # Write the remaining rows
#             for row in data:
#                 writer.writerow(row)
#         print(f"Row with '{target_value}' in 'column_name_to_match' deleted.")
#     else:
#         print(f"No match found for '{target_value}' in 'column_name_to_match'.")





@csrf_exempt
def AttendanceApi(request, AttendanceId=0):
    if request.method == "GET":
        with open(os.path.join(os.path.dirname(__file__), csvPath), "r+") as f:
            myDataList = f.readlines()

            for line in myDataList:
                
                entry = line.split(',')
                temp = {"AttendanceId":1, "EmployeeName":entry[0], "EmployeeTime":entry[1], "EmployeeDate":entry[2]}
                attendance = Attendance.objects.all()
                flag = True
                for employee in attendance:
                    if (employee.EmployeeName == temp["EmployeeName"]):
                        flag = False
                
                if flag:
                    attendanceSerializer = AttendanceSerializer(data=temp)
                    if attendanceSerializer.is_valid(raise_exception=True):
                        # print("Valid data")
                        attendanceSerializer.save()
              
            attendanceSerializer = AttendanceSerializer(Attendance.objects.all(), many=True)
            return JsonResponse(attendanceSerializer.data, safe=False)
             
    elif request.method == "DELETE":
        if AttendanceId != 0:
            attendance = Attendance.objects.get(AttendanceId=AttendanceId)
            print(attendance)
            # attendance = attendance.delete()
            # csvDel(EmployeeName)
        else:
            pass
        return JsonResponse("Deleted Successfully", safe=False)


@csrf_exempt
def SaveFile(request):
    file = request.FILES['file']
    file_name = default_storage.save(file.name,file)
    return JsonResponse(file_name,safe=False)


def gen(camera):
	while True:
		frame = camera.get_frame()
		yield (b'--frame\r\n'
				b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')


@csrf_exempt
def VideoFeed(request):
    

    return StreamingHttpResponse(gen(VideoCamera()),
                content_type='multipart/x-mixed-replace; boundary=frame')

@csrf_exempt
def ip(request):
    if request.method == 'POST':
        ip = JSONParser().parse(request)
        print(ip)
        try:
            return StreamingHttpResponse(gen(VideoCamera(ip.IP)),
                                        content_type='multipart/x-mixed-replace; boundary=frame')
        except:
            print("Invalid IP")
            




    
    return JsonResponse("Invalid IP?", safe=False)



@csrf_exempt
def VideoFeedStopped(request):
    return JsonResponse("Stopped", safe=False)