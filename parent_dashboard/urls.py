
from django.urls import path
from .views import dashboard, academic_overview, subject_wise_performance, subject_graphs_view, attendance_view # Import both views

app_name = "parent_dashboard"  

urlpatterns = [
    path('dashboard/', dashboard, name="dashboard"),  
    path('academic-overview/', academic_overview, name='academic_overview'), 
    path('subject-performance/', subject_wise_performance, name='subject_performance'),
    path('subject-graphs/', subject_graphs_view, name='subject_graphs'),
    path('attendance/', attendance_view, name='attendance_view'),
    
]

