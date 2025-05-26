
from django.urls import path
from .views import dashboard, academic_overview, subject_wise_performance, subject_graphs_view, attendance_view, feedback_and_meeting_view # Import both views
from django.contrib.auth import views as auth_views
app_name = "parent_dashboard"  

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('dashboard/', dashboard, name="dashboard"),  
    path('academic-overview/', academic_overview, name='academic_overview'), 
    path('subject_graphs/', subject_graphs_view, name='subject_graphs'),
    path('attendance/', attendance_view, name='attendance_view'),
    path('subject_performance/', subject_wise_performance, name='subject_performance'),
    path('feedback/', feedback_and_meeting_view, name = 'feedback_meeeting' ),
]

