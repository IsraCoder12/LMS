from django.db import models
from django.contrib.auth.models import User  
#import semester model in Student academic overview ***************************************
#shows semester grades in summary format and shows gpa and cga 
class Semester(models.Model):
    SEMESTER_CHOICES = [
        ('Spring', 'Spring'),
        ('Fall', 'Fall'),
        ('Summer', 'Summer'),
    ]

    student = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'groups__name': 'Students'})
    semester_name = models.CharField(max_length=10, choices=SEMESTER_CHOICES)  # "Spring", "Fall", or "Summer"
    year = models.IntegerField()  # Stores 2025, 2024, etc.
    gpa = models.FloatField(default=0.0)
    cgpa = models.FloatField(default=0.0)
    overall_grade = models.CharField(max_length=2)  # e.g. 'A', 'B', 'C'

    class Meta:
        unique_together = ('student', 'semester_name', 'year')  # Ensures uniqueness per student

    def __str__(self):
        return f"{self.semester_name} {self.year} - {self.student.username}"

    
#********************The End Student Academic view **************************************************

#Model Subject Wise performance Difference subject show individual data *****************
from django.db import models
from django.contrib.auth.models import User  

class Subject(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)  # Each subject is linked to a student
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE, related_name="subjects")
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return f"{self.name} - {self.semester.name} - {self.student.username}"

class SubjectPerformance(models.Model):
    subject = models.OneToOneField(Subject, on_delete=models.CASCADE, related_name="performance")
    assignment_marks = models.IntegerField() 
    quiz_marks = models.IntegerField()         
    midterm_marks = models.IntegerField()     
    final_exam_marks = models.IntegerField() 
    total_marks = models.IntegerField(blank=True, null=True)  
    grade = models.CharField(max_length=2, blank=True, null=True)
    improvement_needed = models.BooleanField(default=False)

    def calculate_total_marks(self):  
        return self.assignment_marks + self.quiz_marks + self.midterm_marks + self.final_exam_marks

    def calculate_grade(self):
        if self.total_marks >= 85:
            return "A"
        elif self.total_marks >= 75:
            return "B"
        elif self.total_marks >= 65:
            return "C"
        elif self.total_marks >= 50:
            return "D"
        else:
            return "F"

    def check_improvement(self):
        return self.grade in ["D", "F"]  # Improvement needed for low grades

    def save(self, *args, **kwargs):
        self.total_marks = self.calculate_total_marks()
        self.grade = self.calculate_grade()
        self.improvement_needed = self.check_improvement()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Performance of {self.subject.name} ({self.subject.student.username})"
#********************The End Subject wise performance tracking **************************************************



#import parent.profile model*************************************
class ParentProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=15, blank=True, null=True)
    address = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.user.username

#*******************model for filter student data in ascending step by step***************************

from django.shortcuts import render
from parent_dashboard.models import Semester

def student_academic_overview(request):
    student_data = Semester.objects.filter(student=request.user).prefetch_related("subjects")

    # Filter by Semester if requested
    semester_filter = request.GET.get("semester")
    if semester_filter:
        student_data = student_data.filter(semester_number=semester_filter)

    # Sorting by GPA
    sort_by_gpa = request.GET.get("sort_gpa")
    if sort_by_gpa == "asc":
        student_data = student_data.order_by("gpa")
    elif sort_by_gpa == "desc":
        student_data = student_data.order_by("-gpa")

    return render(request, "parent_dashboard/academic_overview.html", {"student_data": student_data})

#Suceessfully completed.................

#new model graphical representation subject wise performance dont need this model at a time .............................................
#******************************* Attendance model ***************************************************

from django.db import models
from django.contrib.auth.models import User

class Attendance(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)  
    date = models.DateField() 
    status = models.BooleanField(default=False) 
    class_name = models.CharField(max_length=100)  # Optional: to track the class name

    def __str__(self):
        return f"{self.student} - {self.date} - {'Present' if self.status else 'Absent'}"
 
