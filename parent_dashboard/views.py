#**************************** view if user student parent or teacher or !****************************************
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

@login_required
def parent_dashboard(request):
    if request.user.groups.filter(name='Parents').exists():  
        return render(request, 'parent_dashboard/dashboard.html')
    else:
        return render(request, 'error.html', {'message': 'Access Denied!'})


#*********************** View student academic overview**************************************

from django.shortcuts import render
from .models import Semester
from django.contrib.auth.decorators import login_required

@login_required
def academic_overview(request):
    semesters = Semester.objects.filter(student=request.user).order_by('-year', '-semester_name')
    return render(request, 'parent_dashboard/academic_overview.html', {'semesters': semesters})

#8888888888888888888888888888 view the end student acadenic view 88888888888888888888888888888888888

#****************************view subject-wise performance **************************************
from django.shortcuts import render
from .models import SubjectPerformance
from django.contrib.auth.decorators import login_required

#@login_required
#def subject_performance(request):
    #student = request.user  # Assuming the logged-in user is the student (adjust as needed)
    #subject_performances_data = SubjectPerformance.objects.filter(subject__student=student)
    #print("Subject Performance Data:", subject_performances_data)  # <--- ADD THIS LINE
    #context = {'subject_performances': subject_performances_data}
    #return render(request, 'parent_dashboard/subject_performance.html', context)
#8888888888888888888888888888 The end Subject wise performance 8888888888888888888888888888888888



#important function -------------------------------------------------------------------------------
from django.shortcuts import render
from django.http import HttpResponse


def subject_wise_performance(request):
    return render(request, 'parent_dashboard/subject_performance.html')
def academic_overview(request):
    dummy_semesters = [
        {'semester_name': 'Fall', 'year': 2023, 'gpa': 3.8, 'cgpa': 3.7, 'overall_grade': 'A'},
        {'semester_name': 'Spring', 'year': 2024, 'gpa': 3.9, 'cgpa': 3.8, 'overall_grade': 'A+'}
    ]
    context = {'semesters': dummy_semesters}
    return render(request, 'parent_dashboard/academic_overview.html', context)
def dashboard(request):
    return render(request, 'parent_dashboard/dashboard.html')

#------------------------------------------------------------------------------------------------------
#**************************if you need to show data for subject wise performance **********************
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import SubjectPerformance, Subject
from django.contrib.auth.models import User

@login_required
def subject_wise_performance(request):
     
    try:
        test_student = User.objects.first()  # Get the first user, adjust as needed
    except User.DoesNotExist:
        return render(request, 'error.html', {'message': 'No users found for testing.'})

    dummy_subjects = [
        Subject(student=test_student, name='Mathematics'),
        Subject(student=test_student, name='Science'),
        Subject(student=test_student, name='English'),
    ]

    dummy_performances = [
        SubjectPerformance(
            subject=dummy_subjects[0],
            assignment_marks=80,
            quiz_marks=15,
            midterm_marks=70,
            final_exam_marks=90,
            total_marks=355,
            grade='A',
            improvement_needed=False,
        ),
        SubjectPerformance(
            subject=dummy_subjects[1],
            assignment_marks=75,
            quiz_marks=12,
            midterm_marks=65,
            final_exam_marks=85,
            total_marks=337,
            grade='B',
            improvement_needed=False,
        ),
        SubjectPerformance(
            subject=dummy_subjects[2],
            assignment_marks=60,
            quiz_marks=10,
            midterm_marks=55,
            final_exam_marks=70,
            total_marks=295,
            grade='C',
            improvement_needed=True,
        ),
    ]

    context = {'subject_performances': dummy_performances}
    return render(request, 'parent_dashboard/subject_performance.html', context)

#***************************To show subject wise performance ******************************************

#*************************** View Subject_graphs ******************************************************
from django.shortcuts import render
from .models import SubjectPerformance
from django.contrib.auth.decorators import login_required
import json

@login_required
def subject_graphs_view(request):
    student = request.user
    subject_performances = SubjectPerformance.objects.filter(subject__student=student).select_related('subject')

    subject_data_for_graphs = []
    for performance in subject_performances:
        subject_data_for_graphs.append({
            'subject_name': performance.subject.name,
            'assignment_marks': performance.assignment_marks,
            'quiz_marks': performance.quiz_marks,
            'midterm_marks': performance.midterm_marks,
            'final_exam_marks': performance.final_exam_marks,
            'subject_id': performance.subject.id,  # Important for unique canvas IDs
        })

    context = {'subject_data_for_graphs': json.dumps(subject_data_for_graphs)}
    return render(request, 'parent_dashboard/subject_graphs.html', context)

#88888888888888888888888888888 The end 888888888888888888888888888888888888888888888888888