from datetime import datetime
from .models import Attendance

def calculate_monthly_attendance(student, month, year):
    # Attendance records ko filter karen jo given month aur year ke ho
    attendance_records = Attendance.objects.filter(
        student=student,
        date__month=month,
        date__year=year
    )
    
    # Total classes aur attended classes ko calculate karen
    total_classes = attendance_records.count()
    attended_classes = attendance_records.filter(status=True).count()

    # Percentage calculate karen
    if total_classes > 0:
        attendance_percentage = (attended_classes / total_classes) * 100
    else:
        attendance_percentage = 0.0
    
    return attendance_percentage
