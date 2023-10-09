from rest_framework import serializers
from EmployeeApp.models import Departments,Employees,Attendance


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Departments
        fields=('DepartmentId','DepartmentName')

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model=Employees
        fields=('EmployeeId','EmployeeName','Department','DateOfJoining','PhotoFileName')

class AttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model=Attendance
        fields=('AttendanceId','EmployeeName', 'EmployeeTime', 'EmployeeDate')